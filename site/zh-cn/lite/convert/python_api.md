# 模型转换器（Converter）的 Python API 指南

此页面提供了一个关于在 TensorFlow 2.0 中如何使用 
[TensorFlow Lite 转换器（TensorFlow Lite converter）](index.md) Python API 的示例。

[TOC]

## Python API

在 TensorFlow 2.0 中，用来将原始的 TensorFlow 模型格式转换为 TensorFlow Lite 的 Python API 是 `tf.lite.TFLiteConverter`。在 `TFLiteConverter` 中有以下的类方法（classmethod）：

*   `TFLiteConverter.from_saved_model()`：用来转换
    [SavedModel 格式模型](https://www.tensorflow.org/alpha/guide/saved_model)。
*   `TFLiteConverter.from_keras_model()`：用来转换
    [`tf.keras` 模型](https://www.tensorflow.org/alpha/guide/keras/overview)。
*   `TFLiteConverter.from_concrete_functions()`：用来转换
    [concrete functions](concrete_function.md)。

注意: 在 TensorFlow Lite 2.0 alpha 中有一个不同版本的
`TFLiteConverter` API， 该API只包含了
[`from_concrete_function`](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/lite/TFLiteConverter#from_concrete_function)。
本文中用到的的新版本API可以通过pip安装
[`tf-nightly-2.0-preview`](#2.0-nightly)。

本文展示了API的 [示例用法](#examples)，不同 TensorFlow 版本的API详细列表请看 [1.X 版本到 2.0 版本 API 的改变](#differences)，和
[版本说明](#versioning) 来安装和使用。

## 示例 <a name="examples"></a>

### 转换 SavedModel 格式模型 <a name="saved_model"></a>

以下示例展示了如何将一个
[SavedModel](https://www.tensorflow.org/alpha/guide/saved_model) 转换为
TensorFlow Lite 中的 [`FlatBuffer`](https://google.github.io/flatbuffers/)格式。

```python
import tensorflow as tf

# 建立一个简单的模型。
root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.)
root.v2 = tf.Variable(2.)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

# 保存模型。
export_dir = "/tmp/test_saved_model"
input_data = tf.constant(1., shape=[1, 1])
to_save = root.f.get_concrete_function(input_data)
tf.saved_model.save(root, export_dir, to_save)

# 转换模型。
converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
tflite_model = converter.convert()
```

此 API 不支持指定输入向量的维度。 如果您的模型需要指定输入向量的维度，请使用
[`from_concrete_functions`](#concrete_function) 来完成。 示例：

```python
model = tf.saved_model.load(export_dir)
concrete_func = model.signatures[
  tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
concrete_func.inputs[0].set_shape([1, 256, 256, 3])
converter = TFLiteConverter.from_concrete_functions([concrete_func])
```

### 转换 Keras 模型 <a name="keras"></a>

以下示例展示了如何将一个
[tf.keras 模型](https://www.tensorflow.org/alpha/guide/keras/overview) 转换为
TensorFlow Lite 中的 [`FlatBuffer`](https://google.github.io/flatbuffers/) 格式。

```python
import tensorflow as tf

# 创建一个简单的 Keras 模型。
x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]

model = tf.keras.models.Sequential(
    [tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=50)

# 转换模型。
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
```

### 转换 concrete function <a name="concrete_function"></a>

以下示例展示了如何将 TensorFlow 中的
[concrete function](concrete_function.md) into a 转换为TensorFlow Lite 中的
[`FlatBuffer`](https://google.github.io/flatbuffers/) 格式。

```python
import tensorflow as tf

# 建立一个模型。
root = tf.train.Checkpoint()
root.v1 = tf.Variable(3.)
root.v2 = tf.Variable(2.)
root.f = tf.function(lambda x: root.v1 * root.v2 * x)

# 生成 concrete function。
input_data = tf.constant(1., shape=[1, 1])
concrete_func = root.f.get_concrete_function(input_data)

# 转换模型。
#
# `from_concrete_function` 的传入参数被设计为一个一个 concrete function 的列表，然而
# 现阶段仅支持每次调用时仅接受一个concrete function。
# 同时转换多个concrete function的功能正在开发中。
converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_func])
tflite_model = converter.convert()
```

### 端到端 MobileNet 转换 <a name="mobilenet"></a>

以下示例展示了如何将将一个提前训练好的 
`tf.keras` MobileNet 模型转换为 TensorFlow Lite 支持的类型并运行推断 （inference）。 随机数据分别在
TensorFlow 和 TensorFlow Lite 模型中运行的结果将被比较。如果是从文件加载模型，请使用 `model_path` 来代替 `model_content`。

```python
import numpy as np
import tensorflow as tf

# 加载 MobileNet tf.keras 模型。
model = tf.keras.applications.MobileNetV2(
    weights="imagenet", input_shape=(224, 224, 3))

# 转换模型。
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 加载 TFLite 模型并分配张量（tensor）。
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# 获取输入和输出张量。
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 使用随机数据作为输入测试 TensorFlow Lite 模型。
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# 函数 `get_tensor()` 会返回一份张量的拷贝。
# 使用 `tensor()` 获取指向张量的指针。
tflite_results = interpreter.get_tensor(output_details[0]['index'])

# T使用随机数据作为输入测试 TensorFlow 模型。
tf_results = model(tf.constant(input_data))

# 对比结果。
for tf_result, tflite_result in zip(tf_results, tflite_results):
  np.testing.assert_almost_equal(tf_result, tflite_result, decimal=5)
```

## 总结 1.X 版本到 2.0 版本 API 的改变 <a name="differences"></a>

本节总结了从 1.X to 2.0 版本 Python API 的改变。
如果对某些改动有异议, 请提交
[GitHub issue](https://github.com/tensorflow/tensorflow/issues).

### `TFLite转换器` 支持的格式类型

`TFLite转换器` 在 2.0 版本中支持由 1.X 版本和 2.0 版本生成的 SavedModels 和 Keras 模型。但是，转换过程不再支持由 1.X 版本冻结的 `GraphDefs`。 开发者可通过调用 `tf.compat.v1.TFLiteConverter` 来把冻结的 `GraphDefs` 转换到
TensorFlow Lite 版本。

### 量化感知训练（Quantization-aware training）

以下与
[量化感知训练（Quantization-aware training）](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/quantize)
有关的属性和方法在 TensorFlow 2.0 中从`TFLiteConverter` 中被移除。

*   `inference_type`
*   `inference_input_type`
*   `quantized_input_stats`
*   `default_ranges_stats`
*   `reorder_across_fake_quant`
*   `change_concat_input_ranges`
*   `post_training_quantize` - 在 1.X API 中被弃用
*   `get_input_arrays()`

The rewriter function that supports quantization-aware training does not support
models generated by TensorFlow 2.0. Additionally, TensorFlow Lite’s quantization
API is being reworked and streamlined in a direction that supports
quantization-aware training through the Keras API. These attributes will be
removed in the 2.0 API until the new quantization API is launched. Users who
want to convert models generated by the rewriter function can use
`tf.compat.v1.TFLiteConverter`.

### Changes to `TFLiteConverter` attributes

The `target_ops` attribute has become an attribute of `TargetSpec` and renamed
to `supported_ops` in line with future additions to the optimization framework.

Additionally, the following attributes have been removed:

*   `drop_control_dependency` (default: `True`) - Control flow is currently not
    supported by TFLite so it is always `True`.
*   _Graph visualization_ - The recommended approach for visualizing a
    TensorFlow Lite graph in TensorFlow 2.0 will be to use
    [visualize.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/tools/visualize.py).
    Unlike GraphViz, it enables users to visualize the graph after post training
    quantization has occurred. The following attributes related to graph
    visualization will be removed:
    *   `output_format`
    *   `dump_graphviz_dir`
    *   `dump_graphviz_video`

### General API changes

#### Conversion methods

The following methods that were previously deprecated in 1.X will no longer be
exported in 2.0:

*   `lite.toco_convert`
*   `lite.TocoConverter`

#### `lite.constants`

The `lite.constants` API was removed in 2.0 in order to decrease duplication
between TensorFlow and TensorFlow Lite. The following list maps the
`lite.constant` type to the TensorFlow type:

*   `lite.constants.FLOAT`: `tf.float32`
*   `lite.constants.INT8`: `tf.int8`
*   `lite.constants.INT32`: `tf.int32`
*   `lite.constants.INT64`: `tf.int64`
*   `lite.constants.STRING`: `tf.string`
*   `lite.constants.QUANTIZED_UINT8`: `tf.uint8`

Additionally, `lite.constants.TFLITE` and `lite.constants.GRAPHVIZ_DOT` were
removed due to the deprecation of the `output_format` flag in `TFLiteConverter`.

#### `lite.OpHint`

The `OpHint` API is currently not available in 2.0 due to an incompatibility
with the 2.0 APIs. This API enables conversion of LSTM based models. Support for
LSTMs in 2.0 is being investigated. All related `lite.experimental` APIs have
been removed due to this issue.

## Installing TensorFlow <a name="versioning"></a>

### Installing the TensorFlow 2.0 nightly <a name="2.0-nightly"></a>

The TensorFlow 2.0 nightly can be installed using the following command:

```
pip install tf-nightly-2.0-preview
```

### Using TensorFlow 2.0 from a 1.X installation <a name="use-2.0-from-1.X"></a>

TensorFlow 2.0 can be enabled from recent 1.X installations using the following
code snippet.

```python
import tensorflow.compat.v2 as tf

tf.enable_v2_behavior()
```

### Build from source code <a name="latest_package"></a>

In order to run the latest version of the TensorFlow Lite Converter Python API,
either install the nightly build with
[pip](https://www.tensorflow.org/install/pip) (recommended) or
[Docker](https://www.tensorflow.org/install/docker), or
[build the pip package from source](https://www.tensorflow.org/install/source).
