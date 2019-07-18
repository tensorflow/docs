# Python API 指南

本页提供了一些示例来说明如何通过Python API调用TensorFlow Lite转换器，以及解释器。

注意: 本文介绍的是Tensorflow nightly版本的转换器， 运行`pip install tf-nightly`安装此版本。
旧版文档请参考["转换TensorFlow 1.12及之前版本的模型"](#pre_tensorflow_1.12)。

[TOC]

  
## 概述

虽然也可以在命令行中调用TensorFlow Lite转换器, 但用Python脚本调用API的方式可以作为模型开发流水线的一环，通常会更加便捷，
它可以让您尽快知道您正在设计的模型能否可以针对移动设备。

## API

`tf.lite.TFLiteConverter`：用于将TensorFlow模型转换为TensorFlow Lite的API。 
`tf.lite.Interpreter`：用于调用Python解释器的API。

针对不同的模型原始格式，`TFLiteConverter` 提供了多种用于转换的类方法。
`TFLiteConverter.from_session()` 用于 GraphDefs。
`TFLiteConverter.from_saved_model()` 用于 SavedModels。
`TFLiteConverter.from_keras_model_file()` 用于`tf.Keras`文件。
[基本示例](#basic)中展示了简单浮点模型的用法。[复杂示例](#complex)展示了复杂点的模型用法。

## 基本示例 <a name="basic"></a>

以下部分显示了如何把基本浮点模型从各种原始数据格式转换成TensorFlow Lite FlatBuffers。

### 使用tf.Session转换GraphDef <a name="basic_graphdef_sess"></a>

以下示例展示了如何使用`tf.Session`对象把TensorFlow GraphDef转换成TensorFlow Lite FlatBuffer。

```python
import tensorflow as tf

img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
var = tf.get_variable("weights", dtype=tf.float32, shape=(1, 64, 64, 3))
val = img + var
out = tf.identity(val, name="out")

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  converter = tf.lite.TFLiteConverter.from_session(sess, [img], [out])
  tflite_model = converter.convert()
  open("converted_model.tflite", "wb").write(tflite_model)
```

### 使用文件转换GraphDef <a name="basic_graphdef_file"></a>

以下示例展示了当GraphDef被存成文件时，如何转换成TensorFlow Lite FlatBuffer，文件格式支持`.pb` 和`.pbtxt`。

示例中用到的文件下载包：[Mobilenet_1.0_224](https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_1.0_224_frozen.tgz)。
该函数只支持用[freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py)冻结的GraphDef。

```python
import tensorflow as tf

graph_def_file = "/path/to/Downloads/mobilenet_v1_1.0_224/frozen_graph.pb"
input_arrays = ["input"]
output_arrays = ["MobilenetV1/Predictions/Softmax"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

### 转换SavedModel <a name="basic_savedmodel"></a>

以下示例展示了如何把SavedModel转换成TensorFlow Lite FlatBuffer。

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

For more complex SavedModels, the optional parameters that can be passed into
`TFLiteConverter.from_saved_model()` are `input_arrays`, `input_shapes`,
`output_arrays`, `tag_set` and `signature_key`. Details of each parameter are
available by running `help(tf.lite.TFLiteConverter)`.
对于更复杂的SavedModel, 可以往 `TFLiteConverter.from_saved_model()` 函数中传递可选参数：
`input_arrays`，`input_shapes`， `output_arrays`， `tag_set` `signature_key`。
运行 `help(tf.lite.TFLiteConverter)` 查看参数详情。

### 转换tf.keras文件 <a name="basic_keras_file"></a>

The following example shows how to convert a `tf.keras` model into a TensorFlow
Lite FlatBuffer. This example requires
[`h5py`](http://docs.h5py.org/en/latest/build.html) to be installed.
以下示例展示如何把`tf.keras`模型转换成TensorFlow Lite FlatBuffer。示例需要先安装[`h5py`](http://docs.h5py.org/en/latest/build.html)

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file("keras_model.h5")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

`tf.keras`文件必须包含模型和权重。一个全面的包括模型构造在内的示例如下所示：

```python
import numpy as np
import tensorflow as tf

# 生成 tf.keras 模型.
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, input_shape=(3,)))
model.add(tf.keras.layers.RepeatVector(3))
model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(3)))
model.compile(loss=tf.keras.losses.MSE,
              optimizer=tf.keras.optimizers.RMSprop(lr=0.0001),
              metrics=[tf.keras.metrics.categorical_accuracy],
              sample_weight_mode='temporal')

x = np.random.random((1, 3))
y = np.random.random((1, 3, 3))
model.train_on_batch(x, y)
model.predict(x)

# 将tf.keras模型保存成HDF5格式.
keras_file = "keras_model.h5"
tf.keras.models.save_model(model, keras_file)

# 转换成TensorFlow Lite模型.
converter = tf.lite.TFLiteConverter.from_keras_model_file(keras_file)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

## 复杂示例 <a name="complex"></a>

对于属性默认值不足的模型，在调用`convert()`之前应该设置属性值。
例如设置任何常量都需要使用`tf.lite.constants.<CONSTANT_NAME>`，以下示例中使用了常量`QUANTIZED_UINT8`。
您可以在Python终端中运行`help（tf.lite.TFLiteConverter）`获取有关属性的详细文档。

尽管示例中只演示了包含常量的GraphDefs，但不管什么输入数据格式都可以使用同样的逻辑。

### 转换量化GraphDef <a name="complex_quant"></a>

以下示例展示了如何把量化模型转换成TensorFlow Lite FlatBuffer。

```python
import tensorflow as tf

img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
const = tf.constant([1., 2., 3.]) + tf.constant([1., 4., 4.])
val = img + const
out = tf.fake_quant_with_min_max_args(val, min=0., max=1., name="output")

with tf.Session() as sess:
  converter = tf.lite.TFLiteConverter.from_session(sess, [img], [out])
  converter.inference_type = tf.lite.constants.QUANTIZED_UINT8
  input_arrays = converter.get_input_arrays()
  converter.quantized_input_stats = {input_arrays[0] : (0., 1.)}  # mean, std_dev
  tflite_model = converter.convert()
  open("converted_model.tflite", "wb").write(tflite_model)
```

## TensorFlow Lite Python interpreter <a name="interpreter"></a>

### Using the interpreter from a model file <a name="interpreter_file"></a>

The following example shows how to use the TensorFlow Lite Python interpreter
when provided a TensorFlow Lite FlatBuffer file. The example also demonstrates
how to run inference on random input data. Run
`help(tf.lite.Interpreter)` in the Python terminal to get detailed
documentation on the interpreter.

```python
import numpy as np
import tensorflow as tf

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="converted_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model on random input data.
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
```

### Using the interpreter from model data <a name="interpreter_data"></a>

The following example shows how to use the TensorFlow Lite Python interpreter
when starting with the TensorFlow Lite Flatbuffer model previously loaded. This
example shows an end-to-end use case, starting from building the TensorFlow
model.

```python
import numpy as np
import tensorflow as tf

img = tf.placeholder(name="img", dtype=tf.float32, shape=(1, 64, 64, 3))
const = tf.constant([1., 2., 3.]) + tf.constant([1., 4., 4.])
val = img + const
out = tf.identity(val, name="out")

with tf.Session() as sess:
  converter = tf.lite.TFLiteConverter.from_session(sess, [img], [out])
  tflite_model = converter.convert()

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()
```

## Additional instructions

### Build from source code <a name="latest_package"></a>

In order to run the latest version of the TensorFlow Lite Converter Python API,
either install the nightly build with
[pip](https://www.tensorflow.org/install/pip) (recommended) or
[Docker](https://www.tensorflow.org/install/docker), or
[build the pip package from source](https://www.tensorflow.org/install/source).

### Converting models from TensorFlow 1.12 <a name="pre_tensorflow_1.12"></a>

Reference the following table to convert TensorFlow models to TensorFlow Lite in
and before TensorFlow 1.12. Run `help()` to get details of each API.

TensorFlow Version | Python API
------------------ | ---------------------------------
1.12               | `tf.contrib.lite.TFLiteConverter`
1.9-1.11           | `tf.contrib.lite.TocoConverter`
1.7-1.8            | `tf.contrib.lite.toco_convert`