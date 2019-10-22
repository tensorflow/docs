# TensorFlow Lite converter
TensorFlow Lite converter是用于将TensorFlow模型转化为优化过的[FlatBuffer](https://google.github.io/flatbuffers/)格式，以便让TensorFlow Lite解释器调用。

注意：此页面包含TensorFlow 1.x的converter API文档，[TensorFlow 2.0的API请点击此链接](https://www.tensorflow.org/lite/convert/)

## FlatBuffers
FlatBuffers是一个高效的开源跨平台序列化库。它类似于[protocol buffers](https://developers.google.com/protocol-buffers)，区别在于FlatBuffers在访问数据之前不需要对其次要表达进行解析/解压，从而避免对每个对象进行内存分配。FlatBuffers的代码占用空间比protocol buffers小一个数量级。

## 从模型培训到设备部署
TensorFlow Lite converter可以从TensorFlow模型中生成TensorFlow Lite [FlatBuffers](https://google.github.io/flatbuffers/)文件(.tflite)。

converter支持以下输入格式：
- [SavedModels](https://www.tensorflow.org/guide/saved_model#using_savedmodel_with_estimators)
- 变量固定为常数(Frozen)的`GraphDef`:由[freeze_graph.py](https://www.tensorflow.org/code/tensorflow/python/tools/freeze_graph.py)生成的模型
- `tf.keras` HDF5模型
- 任何从 `tf.Session`获取的模型（仅限Python API）

然后，将TensorFlow Lite FlatBuffer文件部署到客户端设备，TensorFlow Lite 解释器会使用压缩模型在设备上进行推断(inference)。该会话过程如下图所示：
![TFLite converter workflow](https://github.com/tensorflow/tensorflow/raw/master/tensorflow/lite/g3doc/images/convert/workflow.svg?sanitize=true)

## 选项

TensorFlow Lite Converter 可以通过以下两种方式使用：
- [Python](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/convert/python_api.md)（**首选方式**）：使用Python API可以更轻松地将模型转换为模型开发流(model development pipeline)的一部分，并有助于在早期开发过程中缓解[兼容性](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/tf_ops_compatibility.md)问题
- [命令行](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/convert/cmdline_examples.md)
