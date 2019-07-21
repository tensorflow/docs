# TensorFlow Lite 转换器

TensorFlow Lite 转换器将 TensorFlow 模型文件转换为 TensorFlow Lite [`FlatBuffer`](https://google.github.io/flatbuffers/) 文件
(`.tflite`)。转换器支持 [SavedModel 目录](https://www.tensorflow.org/alpha/guide/saved_model)，[`tf.keras` 模型](https://www.tensorflow.org/alpha/guide/keras/overview)，及[具体的函数](concrete_function.md)。

注意: 此页面包含的转换器 API 文档是针对 TensorFlow 2.0 所编写的。
针对 TensorFlow 1.X 的 API 可以在[这里](https://www.tensorflow.org/lite/convert/)找到。

## 在设备上部署

随后，TensorFlow Lite `FlatBuffer` 文件被部署到客户终端上 (例如
移动电话, 嵌入式设备) 并通过 TensorFlow Lite 解释器在本地运行。

转换过程如下图所示:

![TFLite converter workflow](../images/convert/workflow.svg)

## 转换模型

TensorFlow Lite 转换器应该通过 [Python API](python_api.md) 被使用。

使用 Python API 可以更容易地将模型转换为模型开发流程的一部分，并有助于尽早

发现并减轻[兼容性](../../guide/ops_compatibility.md) 问题。
作为可选方案,  [命令行工具](cmdline.md)支持一些基本的模型。
