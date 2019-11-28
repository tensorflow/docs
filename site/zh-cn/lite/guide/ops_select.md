# 从 TensorFlow 中选择运算符

注意：该功能是实验性的。

TensorFlow Lite 已经内置了很多运算符，并且还在不断扩展，但是仍然还有一部分 TensorFlow 运算符没有被 TensorFlow Lite 原生支持。这些不被支持的运算符会给 TensorFlow Lite 的模型转换带来一些阻力。为了减少模型转换的阻力，TensorFlow Lite 开发团队最近一直致力于一个实验性功能的开发。

这篇文档简单介绍了怎样在 TensorFlow Lite 使用 TensorFlow 运算符。*注意，这只是一个实验性的功能，并且还在开发中。* 在使用该功能的时候，请记住这些[已知的局限性](#已知的局限性)，并且请将使用中遇到的问题反馈至 tflite@tensorflow.org。

TensorFlow Lite 会继续为移动设备和嵌入式设备优化[内置的运算符](ops_compatibility.md)。但是现在，当 TensorFlow Lite 内置的运算符不够的时候，TensorFlow Lite 模型可以使用部分 TensorFlow 的运算符。

TensorFlow Lite 解释器在处理转换后的包含 TensorFlow 运算符的模型的时候，会比处理只包含 TensorFlow Lite 内置运算符的模型占用更多的空间。并且，TensorFlow Lite 模型中包含的任何 TensorFlow 运算符，性能都不会被优化。

这篇文档简单介绍了怎样针对不同的平台[转换](#转换模型)和[运行](#运行模型)包含 TensorFlow 运算符的 TensorFlow Lite 模型。并且讨论了一些[已知的局限性](#已知的局限性)、为此功能制定的[未来的计划](#未来的计划)以及基本的[性能和空间指标](#性能和空间指标)。

## 转换模型

为了能够转换包含 TensorFlow 运算符的 TensorFlow Lite 模型，可使用位于 [TensorFlow Lite 转换器](../convert/) 中的 `target_spec.supported_ops` 参数。`target_spec.supported_ops` 的可选值如下：

*   `TFLITE_BUILTINS` - 使用 TensorFlow Lite 内置运算符转换模型。
*   `SELECT_TF_OPS` - 使用 TensorFlow 运算符转换模型。已经支持的 TensorFlow 运算符的完整列表可以在白名单
    `lite/delegates/flex/whitelisted_flex_ops.cc` 中查看。

注意：`target_spec.supported_ops` 是之前 Python API 中的 `target_ops`。

我们优先推荐使用 `TFLITE_BUILTINS` 转换模型，然后是同时使用 `TFLITE_BUILTINS,SELECT_TF_OPS` ，最后是只使用 `SELECT_TF_OPS`。同时使用两个选项（也就是 `TFLITE_BUILTINS,SELECT_TF_OPS`）会用 TensorFlow Lite 内置的运算符去转换支持的运算符。有些 TensorFlow 运算符 TensorFlow Lite 只支持部分用法，这时可以使用 `SELECT_TF_OPS` 选项来避免这种局限性。

下面的示例展示了通过 Python API 中的 [`TFLiteConverter`](./convert/python_api.md) 来使用该功能。

```
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,
                                       tf.lite.OpsSet.SELECT_TF_OPS]
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

下面的示例展示了在命令行工具 [`tflite_convert`](../convert/cmdline_examples.md) 中通过 `target_ops` 标记来使用该功能。

```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/foo.pb \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --target_ops=TFLITE_BUILTINS,SELECT_TF_OPS
```

如果直接使用 `bazel` 编译和运行 `tflite_convert`，请传入参数 `--define=with_select_tf_ops=true`。

```
bazel run --define=with_select_tf_ops=true tflite_convert -- \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/foo.pb \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --target_ops=TFLITE_BUILTINS,SELECT_TF_OPS
```

## 运行模型

如果 TensorFlow Lite 模型在转换的时候支持 TensorFlow select 运算符，那么在使用的时候 Tensorflow Lite 运行时必须包含 TensorFlow 运算符的库。

### Android AAR

为了便于使用，新增了一个支持 TensorFlow select 运算符的Android AAR。如果已经有了<a href="android.md">可用的 TensorFlow Lite
编译环境</a>，可以按照下面的方式编译支持使用 TensorFlow select 运算符的 Android AAR：

```sh
bazel build --cxxopt='--std=c++11' -c opt             \
  --config=android_arm --config=monolithic          \
  //tensorflow/lite/java:tensorflow-lite-with-select-tf-ops
```

上面的命令会在 `bazel-genfiles/tensorflow/lite/java/` 目录下生成一个 AAR 文件。你可以直接将这个 AAR 文件导入到项目中，也可以将其发布到本地的 Maven 仓库：

```sh
mvn install:install-file \
  -Dfile=bazel-genfiles/tensorflow/lite/java/tensorflow-lite-with-select-tf-ops.aar \
  -DgroupId=org.tensorflow \
  -DartifactId=tensorflow-lite-with-select-tf-ops -Dversion=0.1.100 -Dpackaging=aar
```

最后，在应用的 `build.gradle` 文件中需要保证有 `mavenLocal()` 依赖，并且需要用支持 TensorFlow select 运算符的 TensorFlow Lite 依赖去替换标准的 TensorFlow Lite 依赖：

```
allprojects {
    repositories {
        jcenter()
        mavenLocal()
    }
}

dependencies {
    implementation 'org.tensorflow:tensorflow-lite-with-select-tf-ops:0.1.100'
}
```

### iOS

如果安装了 XCode 命令行工具，可以用下面的命令编译支持 TensorFlow select 运算符的 TensorFlow Lite：

```sh
tensorflow/contrib/makefile/build_all_ios_with_tflite.sh
```

这条命令会在 `tensorflow/contrib/makefile/gen/lib/` 目录下生成所需要的静态链接库。

TensorFlow Lite 的相机示例应用可以用来进行测试。一个新的支持 TensorFlow select 运算符的 TensorFlow Lite XCode 项目已经添加在 `tensorflow/lite/examples/ios/camera/tflite_camera_example_with_select_tf_ops.xcodeproj` 中。

如果想要在自己的项目中使用这个功能，你可以克隆示例项目，也可以按照下面的方式对项目进行设置：

*   在 Build Phases -> Link Binary With Libraries 中，添加 `tensorflow/contrib/makefile/gen/lib/` 目录中的静态库：
    *   `libtensorflow-lite.a`
    *   `libprotobuf.a`
    *   `nsync.a`
*   在 Build Settings -> Header Search Paths 中，添加下面的路径：
    *   `tensorflow/lite/`
    *   `tensorflow/contrib/makefile/downloads/flatbuffer/include`
    *   `tensorflow/contrib/makefile/downloads/eigen`
*   在 Build Settings -> Other Linker Flags 中，添加 `-force_load
    tensorflow/contrib/makefile/gen/lib/libtensorflow-lite.a`。
    
未来还会发布支持 TensorFlow select 运算符的 CocoaPod 。

### C++

如果使用 bazel 编译 TensorFlow Lite 库，可以按照下面的方式添加和支持额外的 TensorFlow 运算符的库。

*   如果需要单体编译，可以添加 `--config=monolithic` 编译标记。
*   从下面的方案中选择一个：
    *   在用 `bazel build` 命令编译 TensorFlow Lite 时添加 `--define=with_select_tf_ops=true` 编译标记。
    *   在编译依赖中添加 TensorFlow 运算符库依赖 `tensorflow/lite/delegates/flex:delegate`。

注意，只要委托链接到了客户端库，在运行时创建解释器的时候就会自动安装所需的 `TfLiteDelegate`，而不需要像其他委托类型去显式安装委托实例。

### Python pip Package

对 Python 的支持还在开发当中。

## 性能和空间指标

### 性能

如果 TensorFlow Lite 模型是同时混合使用内置运算符和 TensorFlow select 运算符进行转换的，那么模型依然可以使用针对 TensorFlow Lite 的优化以及内置的优化内核。

下表列出了在 Pixel 2 上 MobileNet 的平均推断时间。表中的时间是 100 次运行的平均时间。在对 Android 平台编译的时候添加了 `--config=android_arm64 -c opt` 标记。

编译                               | 推断时间 (milliseconds)
------------------------------------ | -------------------
Only built-in ops (`TFLITE_BUILTIN`) | 260.7
Using only TF ops (`SELECT_TF_OPS`)  | 264.5

### 二进制文件大小

下表列出了不同编译方式生成的 TensorFlow Lite 二进制文件的大小。在对 Android 平台编译的时候添加了 `--config=android_arm -c opt` 标记。

编译                 | C++ 二进制文件大小 | Android APK 大小
--------------------- | --------------- | ----------------
Only built-in ops     | 796 KB          | 561 KB
Built-in ops + TF ops | 23.0 MB         | 8.0 MB

## 已知的局限性

下面列出了一些已知的局限性：

*   目前还不支持控制流运算符。
*   目前还不支持 TensorFlow 运算符的 [`post_training_quantization`](https://www.tensorflow.org/performance/post_training_quantization) 标记，所以不会对任何 TensorFlow 运算符进行权重量化。如果模型中既包含 TensorFlow Lite 运算符又包含 TensorFlow 运算符，那么 TensorFlow Lite 内置的运算符的权重是可以被量化的。
*   目前还不支持像 HashTableV2 这种需要显式用资源进行初始化的运算符。
*   某些 TensorFlow 操作可能不支持 TensorFlow 库中整套常规可用输入/输出操作。

## 未来的计划

下面列出了正在开发中的针对该功能的一些改进：

*   *选择性注册* - 有一项正在完成的工作是，让生成只包含特定模型集合所需的 Tensorflow 运算符的 TensorFlow Lite 二进制文件变得更简单。
*   *提升可用性* - 模型转换的过程将被简化，只需要一次性完成转换。 并且还会提供预编译的 Android AAR 和 iOS CocoaPod 二进制文件。
*   *提升性能* - 有一项正在完成的工作是，让使用 TensorFlow 运算符的 TensorFlow Lite 具有与 TensorFlow Mobile 同等的性能。
