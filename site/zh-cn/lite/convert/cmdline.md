# 模型转换器命令参考

本页介绍如何使用 TensorFlow 2.0 命令行工具中的[TensorFlow Lite 模型转换器](index.md)。首选的转换方法是使用 [Python API](python_api.md)。

## 综述

TensorFlow Lite 转换器命令行工具 `tflite_convert` 它支持基础模型转换。使用 `TFLiteConverter` [Python API](python_api.md) 支持任何涉及量化或其他参数的转换(例如：SavedModels 签名，或者在 Keras 模型上自定义对象).

## 使用

下列命令参数用于输入和输出文件。

*   `--output_file`. 类型: string. 指定输出文件的绝对路径。
*   --saved_model_dir. 类型: string. 指定含有 TensorFlow 1.x 或者 2.0 使用 SavedModel 生成文件的绝对路径目录。
*   --keras_model_file. Type: string. 指定含有 TensorFlow 1.x 或者 2.0 使用 tf.keras model 生成 HDF5 文件的绝对路径目录。

例如：

```
tflite_convert \
  --saved_model_dir=/tmp/mobilenet_saved_model \
  --output_file=/tmp/mobilenet.tflite
```

## 附加说明

### 从源代码构建

想要运行最新版本的 TensorFlow Lite 模型转换器可以通过 [pip](https://www.tensorflow.org/install/pip) 安装 TensorFlow 2.0 测试版或者[克隆 TensorFlow 代码库](https://www.tensorflow.org/install/source)然后使用 `bazel` 从源代码编译 TensorFlow 。下面是一个从源代码编译 TensorFlow 的例子。

```
bazel run //third_party/tensorflow/lite/python:tflite_convert -- \
  --saved_model_dir=/tmp/mobilenet_saved_model \
  --output_file=/tmp/mobilenet.tflite
```
