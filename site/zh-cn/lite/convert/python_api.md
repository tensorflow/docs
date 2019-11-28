# 模型转换器（Converter）的 Python API 指南

此页面提供了一个关于在 TensorFlow 2.0 中如何使用 
[TensorFlow Lite 转换器（TensorFlow Lite converter）](index.md) Python API 的示例。

[TOC]

## Python API

在 TensorFlow 2.0 中，用来将原始的 TensorFlow 模型格式转换为 TensorFlow Lite 的 Python API 是 `tf.lite.TFLiteConverter`。在 `TFLiteConverter` 中有以下的类方法（classmethod）：

*   `TFLiteConverter.from_saved_model()`：用来转换
    [SavedModel 格式模型](https://www.tensorflow.org/guide/saved_model)。
*   `TFLiteConverter.from_keras_model()`：用来转换
    [`tf.keras` 模型](https://www.tensorflow.org/guide/keras/overview)。
*   `TFLiteConverter.from_concrete_functions()`：用来转换
    [concrete functions](concrete_function.md)。

注意: 在 TensorFlow Lite 2.0 中有一个不同版本的
`TFLiteConverter` API， 该 API 只包含了
[`from_concrete_function`](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/lite/TFLiteConverter#from_concrete_function)。
本文中用到的的新版本 API 可以通过 pip 安装
[`tf-nightly-2.0-preview`](#2.0-nightly)。

本文展示了 API 的 [示例用法](#examples)，不同 TensorFlow 版本的 API 详细列表请看 [1.X 版本到 2.0 版本 API 的改变](#differences)，和
[安装 TensorFlow](#versioning) 来安装和使用。

## 示例 <a name="examples"></a>

### 转换 SavedModel 格式模型 <a name="saved_model"></a>

以下示例展示了如何将一个
[SavedModel](https://www.tensorflow.org/guide/saved_model) 转换为
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
[tf.keras 模型](https://www.tensorflow.org/guide/keras/overview) 转换为
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
[concrete function](concrete_function.md) 转换为TensorFlow Lite 中的
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

# 使用随机数据作为输入测试 TensorFlow 模型。
tf_results = model(tf.constant(input_data))

# 对比结果。
for tf_result, tflite_result in zip(tf_results, tflite_results):
  np.testing.assert_almost_equal(tf_result, tflite_result, decimal=5)
```

## 总结 1.X 版本到 2.0 版本 API 的改变 <a name="differences"></a>

本节总结了从 1.X 到 2.0 版本 Python API 的改变。
如果对某些改动有异议，请提交
[GitHub issue](https://github.com/tensorflow/tensorflow/issues)。

### `TFLite转换器` 支持的格式类型

`TFLite转换器` 在 2.0 版本中支持由 1.X 版本和 2.0 版本生成的 SavedModels 和 Keras 模型。但是，转换过程不再支持由
1.X 版本冻结的 `GraphDefs`。 开发者可通过调用 `tf.compat.v1.lite.TFLiteConverter` 来把冻结的
`GraphDefs` 转换到 TensorFlow Lite 版本。

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

支持量化感知训练的重写器（rewriter）函数不支持由 TensorFlow 2.0 生成的模型。此外，TensorFlow Lite 的量化 API
已按支持 Keras 中量化感知训练 API 的思路重新设计和精简。 在新的量化 API 部署前，这些属性将不会出现在 2.0 的 API 中。开发者可以使用
`tf.compat.v1.lite.TFLiteConverter` 来转换由重写器函数生成的模型。

### 关于 `TFLiteConverter` 中属性的改变

属性 `target_ops` 已成为 `TargetSpec` 中的属性且作为未来对优化框架的补充被重命名为 `supported_ops`。

此外，以下属性被移除:

*   `drop_control_dependency` (default: `True`) - TFLite 现不支持控制流（control flow），所以此属性将恒为 `True`。
*   _Graph visualization_ - 在 TensorFlow 2.0 中，推荐使用
    [visualize.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/tools/visualize.py) 实现对 TensorFlow Lite 图（graph）的可视化。
    不同于 GraphViz, 它支持开发者对已进行过 post training 量化的图（graph）可视化。以下与图可视化的属性将被移除：
    *   `output_format`
    *   `dump_graphviz_dir`
    *   `dump_graphviz_video`

### 通用 API 的改变

#### 转换方法

以下在 1.X 中被弃用的方法不会在 2.0 中出现：

*   `lite.toco_convert`
*   `lite.TocoConverter`

#### `lite.constants`

在 2.0 中，为了减少 TensorFlow 和 TensorFlow Lite 之间的重复移除了 `lite.constants` API。以下的列表展示了
`lite.constant` 中的类型在 TensorFlow 中对应的类型：

*   `lite.constants.FLOAT`: `tf.float32`
*   `lite.constants.INT8`: `tf.int8`
*   `lite.constants.INT32`: `tf.int32`
*   `lite.constants.INT64`: `tf.int64`
*   `lite.constants.STRING`: `tf.string`
*   `lite.constants.QUANTIZED_UINT8`: `tf.uint8`

此外，`lite.constants.TFLITE` 和 `lite.constants.GRAPHVIZ_DOT` 被移除（由于 `TFLiteConverter` 中的 flage `output_format`被移除）。

#### `lite.OpHint`

由于 API `OpHint` 与 2.0 的 API 不兼容，故暂不可用。 此 API可用于转换基于 LSTM 的模型。 在 2.0 中对
LSTMs 的支持正在被探究。所有与 `lite.experimental` 有关的 API 都因此被移除。

## 安装 TensorFlow <a name="versioning"></a>

### 安装 TensorFlow 2.0 nightly <a name="2.0-nightly"></a>

可用以下命令安装 TensorFlow 2.0 nightly：

```
pip install tf-nightly-2.0-preview
```

### 在已安装的 1.X 中使用 TensorFlow 2.0 <a name="use-2.0-from-1.X"></a>

可通过以下代码片段从最近安装的 1.X 中使用 TensorFlow 2.0。

```python
import tensorflow.compat.v2 as tf

tf.enable_v2_behavior()
```

### 从源代码安装 <a name="latest_package"></a>

为使用最新版本的 TensorFlow Lite 转换器 Python API，
您可通过以下方式安装 nightly build：
[pip](https://www.tensorflow.org/install/pip) (推荐方式) 或
[Docker](https://www.tensorflow.org/install/docker), 或
[从源代码构建 pip 包](https://www.tensorflow.org/install/source).
