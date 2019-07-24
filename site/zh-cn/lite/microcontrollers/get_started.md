# 微控制器入门

本文档将帮助您开始使用用于微控制器的 Tensorflow Lite。

首先请阅读并运行我们的[示例](#示例)

注意：如果您需要一个入门设备，我们建议使用 
[由 Tensorflow 提供技术支持的 SparkFun Edge](https://www.sparkfun.com/products/15170)。
它是与 Tensorflow Lite 团队合作设计的，为在微控制器上进行深度学习实验提供了灵活的平台。

有关运行推断所需代码的介绍，请参阅下文的*运行推断*部分

## 示例

下面几个示例演示了如何使用 Tensorflow Lite 构建嵌入式机器学习应用程序：

### Hello World 示例

本示例旨在演示将 Tensorflow Lite 用于微控制器的绝对基础知识。它包括了训练模型、将模型转换以供 Tensorflow Lite 使用以及在微控制器上进运行推断的完整端到端工作流程。

在这个示例中，一个模型被训练用来模拟正弦函数。部署到微控制器上时，其预测可用来闪烁 LED 或者控制动画。

<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/hello_world">Hello
World 示例</a>

示例代码包含一个演示如何训练和转换模型的 Jupyter notebook：

<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/hello_world/create_sine_model.ipynb">create_sine_model.ipynb</a>

指南[“构建与转换模型”](build_convert.md)中也介绍了构建和转换模型的流程。

要了解推断是如何执行的，请查看 [hello_world_test.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/hello_world/hello_world_test.cc)。

该示例在以下平台上进行了测试：

-   [由 Tensorflow 提供技术支持的 SparkFun Edge(Apollo3 Blue)](https://www.sparkfun.com/products/15170)
-   [Arduino MKRZERO](https://store.arduino.cc/usa/arduino-mkrzero)
-   [STM32F746G 探索板（Discovery Board）](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)
-   Mac OS X

### 微语音示例

此示例使用一个简单的
[音频识别模型](https://www.tensorflow.org/tutorials/sequences/audio_recognition)
来识别语音中的关键字。示例代码从设备的麦克风中捕获音频。模型通过对该音频进行实时分类来确定是否说过“是”或“否一词。

<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/micro_speech">微语音示例</a>

[“运行推断”](#运行推断) 部分将纵览微语音示例的代码并解释其工作原理。

该示例在以下平台上进行了测试：

-   [由 Tensorflow 提供技术支持的 SparkFun Edge(Apollo3 Blue)](https://www.sparkfun.com/products/15170)
-   [STM32F746G 探索板（Discovery Board）](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)
-   Mac OS X

注意：若要开始使用 SparkFun Edge 板，我们建议遵循[“在使用 SparkFun Tensorflow 的微控制器上进行机器学习”](https://codelabs.developers.google.com/codelabs/sparkfun-tensorflow)中所描述的流程,这是一个向您介绍开发工作流程的代码实验室（codelab）。

### 微视觉示例

本示例展示了如何使用 Tensorflow Lite 运行一个 25 万字节的神经网络来识别由摄像机拍摄的图像中的人。该示例被设计成可以在具有少量内存的系统上运行，如微控制器和 DSP。

<a class="button button-primary" href="https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples/micro_vision">微视觉示例</a>

该示例在以下平台上进行了测试：

-   [由 Tensorflow 提供技术支持的 SparkFun Edge(Apollo3 Blue)](https://www.sparkfun.com/products/15170)
-   [STM32F746G 探索板（Discovery Board）](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)
-   Mac OS X

## 运行推断

以下部分将介绍[微语音](#微语音示例)示例中的 [main.cc](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/main.cc) 文件并解释了它如何使用用于微控制器的 Tensorflow Lite 来运行推断。

### 包含项

要使用库，必须包含以下头文件：

```C++
#include "tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h"
#include "tensorflow/lite/experimental/micro/micro_error_reporter.h"
#include "tensorflow/lite/experimental/micro/micro_interpreter.h"
#include "tensorflow/lite/schema/schema_generated.h"
#include "tensorflow/lite/version.h"
```

-   [`all_ops_resolver.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h)
    提供给解释器（interpreter）用于运行模型的操作。
-   [`micro_error_reporter.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/micro_error_reporter.h)
    输出调试信息。
-   [`micro_interpreter.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/micro_interpreter.h)
    包含处理和运行模型的代码。
-   [`schema_generated.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/schema/schema_generated.h)
    包含 TensorFlow Lite
    [`FlatBuffer`](https://google.github.io/flatbuffers/) 模型文件格式的模式。
-   [`version.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/version.h)
    提供 Tensorflow Lite 架构的版本信息。

示例还包括其他一些文件。以下这些是最重要的：

```C++
#include "tensorflow/lite/experimental/micro/examples/micro_speech/feature_provider.h"
#include "tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/micro_model_settings.h"
#include "tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/tiny_conv_micro_features_model_data.h"
```

-   [`feature_provider.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/feature_provider.h)
    包含从音频流中提取要输入到模型中的特征的代码。
-   [`tiny_conv_micro_features_model_data.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/tiny_conv_micro_features_model_data.h)
    包含存储为 `char` 数组的模型。阅读
    [“构建与转换模型”](build_convert.md) 来了解如何将 Tensorflow Lite 模型转换为该格式。
-   [`micro_model_settings.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/micro_model_settings.h)
    定义与模型相关的各种常量。

### 设置日志记录

要设置日志记录，需要使用一个指向 `tflite::MicroErrorReporter` 实例的指针来创建一个 `tflite::ErrorReporter` 指针：

```C++
tflite::MicroErrorReporter micro_error_reporter;
tflite::ErrorReporter* error_reporter = &micro_error_reporter;
```
该变量被传递到解释器（interpreter）中，解释器允许它写日志。由于微控制器通常具有多种日志记录机制，`tflite::MicroErrorReporter` 的实现是为您的特定设备所定制的。

### 加载模型

在以下代码中，模型是从一个 `char` 数组中实例化的，`g_tiny_conv_micro_features_model_data` （要了解其是如何构建的，请参见[“构建与转换模型”](build_convert.md)）。 随后我们检查模型来确保其架构版本与我们使用的版本所兼容：

```C++
const tflite::Model* model =
    ::tflite::GetModel(g_tiny_conv_micro_features_model_data);
if (model->version() != TFLITE_SCHEMA_VERSION) {
  error_reporter->Report(
      "Model provided is schema version %d not equal "
      "to supported version %d.\n",
      model->version(), TFLITE_SCHEMA_VERSION);
  return 1;
}
```
### 实例化操作解析器

解释器（interpreter）需要一个 [`AllOpsResolver`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h) 实例来访问 Tensorflow 操作。可以扩展此类以向您的项目添加自定义操作：

```C++
tflite::ops::micro::AllOpsResolver resolver;
```

### 分配内存

我们需要预先为输入、输出以及中间数组分配一定的内存。该预分配的内存是一个大小为 `tensor_arena_size` 的 `uint8_t` 数组，它被传递给 `tflite::SimpleTensorAllocator` 实例：

```C++
const int tensor_arena_size = 10 * 1024;
uint8_t tensor_arena[tensor_arena_size];
tflite::SimpleTensorAllocator tensor_allocator(tensor_arena,
                                               tensor_arena_size);
```

注意：所需内存大小取决于您使用的模型，可能需要通过实验来确定。

### 实例化解释器（Interpreter）

我们创建一个 `tflite::MicroInterpreter` 实例，传递给之前创建的变量：

```C++
tflite::MicroInterpreter interpreter(model, resolver, &tensor_allocator,
                                     error_reporter);
```

### 验证输入维度

`MicroInterpreter` 实例可以通过调用 `.input(0)` 为我们提供一个指向模型输入张量的指针，其中 `0` 代表第一个（也是唯一一个）输入张量。我们检查这个张量以确认它的维度与类型是我们所期望的：

```C++
TfLiteTensor* model_input = interpreter.input(0);
if ((model_input->dims->size != 4) || (model_input->dims->data[0] != 1) ||
    (model_input->dims->data[1] != kFeatureSliceCount) ||
    (model_input->dims->data[2] != kFeatureSliceSize) ||
    (model_input->type != kTfLiteUInt8)) {
  error_reporter->Report("Bad input tensor parameters in model");
  return 1;
}
```

在这个代码段中，变量 `kFeatureSliceCount` 和 `kFeatureSliceSize` 与输入的属性相关，它们定义在 [`micro_model_settings.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/micro_model_settings.h) 中。枚举值 `kTfLiteUInt8` 是对 Tensorflow Lite 某一数据类型的引用，它定义在 [`c_api_internal.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/c/c_api_internal.h) 中。

### 生成特征

我们输入到模型中的数据必须由微控制器的音频输入生成。[`feature_provider.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/micro_features/feature_provider.h) 中定义的 `FeatureProvider` 类捕获音频并将其转换为一组将被传入模型的特征集合。当该类被实例化时，我们用之前获取的 `TfLiteTensor` 来传入一个指向输入数组的指针。`FeatureProvider` 使用它来填充将传递给模型的输入数据：

```C++
  FeatureProvider feature_provider(kFeatureElementCount,
                                   model_input->data.uint8);
```

以下代码使 `FeatureProvider` 从最近一秒的音频生成一组特征并填充进输入张量：

```C++
TfLiteStatus feature_status = feature_provider.PopulateFeatureData(
    error_reporter, previous_time, current_time, &how_many_new_slices);
```

在此例子中，特征生成和推断是在一个循环中发生的，因此设备能够不断地捕捉和处理新的音频。

当在编写自己的程序时，您可能会以其它的方式生成特征，但您总需要在运行模型之前就用数据填充输入张量。

### 运行模型

要运行模型，我们可以在 `tflite::MicroInterpreter` 实例上调用 `Invoke()`：

```C++
TfLiteStatus invoke_status = interpreter.Invoke();
if (invoke_status != kTfLiteOk) {
  error_reporter->Report("Invoke failed");
  return 1;
}
```

我们可以检查返回值 `TfLiteStatus` 以确定运行是否成功。在 [`c_api_internal.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/c/c_api_internal.h) 中定义的 `TfLiteStatus` 的可能值有 `kTfLiteOk` 和 `kTfLiteError`。

### 获取输出

模型的输出张量可以通过在 `tflite::MicroIntepreter` 上调用 `output(0)` 获得，其中 `0` 代表第一个（也是唯一一个）输出张量。

在示例中，输出是一个数组，表示输入属于不同类别（“是”（yes）、“否”（no）、“未知”（unknown）以及“静默”（silence））的概率。由于它们是按照集合顺序排列的，我们可以使用简单的逻辑来确定概率最高的类别：

```C++
    TfLiteTensor* output = interpreter.output(0);
    uint8_t top_category_score = 0;
    int top_category_index;
    for (int category_index = 0; category_index < kCategoryCount;
         ++category_index) {
      const uint8_t category_score = output->data.uint8[category_index];
      if (category_score > top_category_score) {
        top_category_score = category_score;
        top_category_index = category_index;
      }
    }
```

在示例其他部分中，使用了一个更加复杂的算法来平滑多帧的识别结果。该部分在 [recognize_commands.h](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/examples/micro_speech/recognize_commands.h) 中有所定义。在处理任何连续的数据流时，也可以使用相同的技术来提高可靠性。

## 下一步

创建并运行示例后，请阅读以下文档：

*   在[“构建与转换模型”](build_convert.md)中了解如何使用模型。
*   在[“了解C++库”](library.md)中了解更多关于 C++ 库的内容。
