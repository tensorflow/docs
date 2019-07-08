# 开始使用TensorFlow Lite

TensorFlow Lite提供了转换TensorFlow模型，并在移动端(mobile)、嵌入式(embeded)和物联网(IoT)设备上运行TensorFlow模型所需的所有工具。以下指南将逐步介绍开发人员各环节的工作流程，并给出了指向更多说明的链接。

## 1. 选择一个模型

<a id="1_choose_a_model"></a>

TensorFlow Lite允许您在多种设备上运行TensorFlow模型。TensorFlow模型是一种数据结构，这种数据结构包含了在解决一个特定问题时，训练得到的机器学习网络的逻辑和知识。

有多种方式可以获得TensorFlow模型，从使用预训练模型(pre-trained models)到训练自己的模型。为了在TensorFlow Lite中使用模型，模型必须转换成一种特殊格式。这将在第二节[转换模型](#2_convert_the_model_format)中解释。

Note: 不是所有的TensorFlow模型都能在TensorFlow Lite中运行，因为解释器只支持部分(a limited subset)TensorFlow运算符(operations)。参考第二节[转换模型](#2_convert_the_model_format)来了解兼容性。

### 使用预训练模型

TensorFlow Lite团队提供了一系列预训练模型(pre-trained models)，用于解决各种机器学习问题。这些模型已经转换为能与TensorFlow Lite一起使用，且可以在您的应用程序中使用的模型。

这些预训练模型包括：

*	[图像分类(Image classification)](../models/image_classification/overview.md)
*	[物体检测(Object detection)](../models/object_detection/overview.md)
*	[智能回复(Smart reply)](../models/smart_reply/overview.md)
*	[姿态估计(Pose estimation)](../models/pose_estimation/overview.md)
*	[语义分割(Segmentation)](../models/segmentation/overview.md)

在[模型列表(Models)](../models)中查看预训练模型的完整列表。

#### 来自其他来源的模型

您还可以在其他许多地方得到预训练的TensorFlow模型，包括[TensorFlow Hub](https://www.tensorflow.org/hub)。在大多数情况下，这些模型不会以TensorFlow Lite格式提供，您必须在使用前[转换(convert)](#2_convert_the_model_format)这些模型。

### 重新训练模型(迁移学习)

迁移学习(transfer learning)允许您采用训练好的模型并重新(re-train)训练，以执行其他任务。例如，一个[图像分类](../models/image_classification/overview.md)模型可以重新训练以识别新的图像类别。与从头开始训练模型相比，重新训练花费的时间更少，所需的数据更少。

您可以使用迁移学习，根据您的应用程序定制预训练模型。在<a href="https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android">用TensorFlow识别花朵</a>的codelab中，您可以学习如何进行迁移学习。

### 训练自定义模型

如果您设计并训练了您自己的TensorFlow模型，或者您训练了从其他来源得到的模型，在使用前，您需要将此模型转换成TensorFlow Lite的格式。

## 2. 转换模型

<a id="2_convert_the_model_format"></a>

TensorFlow Lite的设计旨在在各种设备上高效执行模型。这种高效部分源于在存储模型时，采用了一种特殊的格式。TensorFlow模型在能被TensorFlow Lite使用前，必须转换成这种格式。

转换模型减小了模型文件大小，并引入了不影响准确性(accuracy)的优化措施(optimizations)。开发人员可以在进行一些取舍的情况下，选择进一步减小模型文件大小，并提高执行速度。您可以使用TensorFlow Lite转换器(converter)选择要执行的优化措施。

因为TensorFlow Lite支持部分TensorFlow运算符(operations)，所以并非所有模型都能转换。参看[Ops兼容性](#Ops兼容性)获得更多信息。

### TensorFlow Lite转换器

[TensorFlow Lite转换器](../convert)是一个将训练好的TensorFlow模型转换成TensorFlow Lite格式的工具。它还能引入优化措施(optimizations)，这将在第四节[优化您的模型](#4_optimize_your_model_optional)中介绍。

转换器以Python API的形式提供。下面的例子说明了将一个TensorFlow `SavedModel`转换成TensorFlow Lite格式的过程：

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
open("converted_model.tflite","wb").write(tflite_model)
```

您可以用类似的方法[转换TensorFlow 2.0模型](../r2/convert)

虽然也能从[命令行](../convert/cmdline_examples)使用用转换器，但是推荐用Python API进行转换。

### 选项

转换器可以从各种输入类型转换模型。

当转换[TensorFlow 1.x模型](../convert/python_api)时，这些输入类型有：

*	[SavedModel文件夹](https://www.tensorflow.org/alpha/guide/saved_model)
*	Frozen GraphDef (通过[freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py)生成的模型)
*	[Keras](https://keras.io)HDF5模型
*	从`tf.Session`得到的模型

当转换[TensorFlow 2.x模型](../r2/convert/python_api)时，这些输入类型有：

*	[SavedModel文件夹](https://www.tensorflow.org/alpha/guide/saved_model)
*	[`tf.keras`模型](https://www.tensorflow.org/alpha/guide/keras/overview)
*	[具体函数(Concrete functions)](../r2/convert/concrete_function.md)

转换器可以配置为应用各种优化措施(optimizations)，这些优化措施可以提高性能，减少文件大小。这将在第四节[优化您的模型](#4_optimize_your_model_optional)中介绍。

### Ops兼容性

TensorFlow Lite当前支持[一部分(limited subset)](ops_compatibility.md)TensorFlow运算符(operations)。长期目标是将来能支持全部的TensorFlow运算符。

如果您期望转换的模型中含有不受支持的运算符，您可以使用[TensorFlow Select](ops_select.md)包含来自TensorFlow的运算符。这会使得部署到设备上的二进制文件更大。


## 3. 使用模型进行推理

<a id="3_use_the_tensorflow_lite_model_for_inference_in_a_mobile_app"></a>

*推理(Inference)* 是通过模型(model)运行数据(data)以获得预测(predictions)的过程。这个过程需要模型(model)，解释器(interpreter)，和输入数据(input data)。

### TensorFlow Lite 解释器

[TensorFlow Lite 解释器(interpreter)](inference.md)是一个库(library)，它接受模型文件(model file)，执行模型文件在输入数据(input data)上定义的运算符(operations)，并提供对输出(output)的访问。

该解释器(interpreter)适用于多个平台，提供了一个简单的API，用于从Java, Swift, Objective-C, C++和Python运行TensorFlow Lite模型。

下面的代码显示了从Java调用解释器的方式:

```java
try (Interpreter interpreter = new Interpreter(tensorflow_lite_model_file)) {
	interpreter.run(input, output);
}
```

### GPU加速和委托

一些设备为机器学习运算符提供硬件加速(hardware acceleration)。例如，大多数移动电话有GPUs，GPU可以比CPU执行更快的浮点矩阵运算(floating point matrix operations)。

速度提升(speed-up)能有显著(substantial)效果。例如，当使用GPU加速时，MobileNet v1图像分类模型在Pixel 3手机上的运行速度提高了5.5倍。

TensorFlow Lite解释器可以配置[委托(Delegates)](../performance/delegates.md)以在不同设备上使用硬件加速。[GPU委托(GPU Delegates)](../performance/gpu.md)允许解释器在设备的GPU上运行适当的运算符。

下面的代码显示了从Java中使用GPU委托的方式:

```java
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);
try {
	interpreter.run(input, output);
}
```

要添加对新硬件加速器的支持，您可以[定义您自己的委托](../performance/delegates.md#how_to_add_a_delegate)。

### Android and iOS

TensorFlow Lite解释器在两个主要移动平台上使用方便。要入门，请浏览[Android快速入门](android.md)和[iOS快速入门](iOS.md)指南。

[示例应用程序](https://www.tensorflow.org/lite/examples)对这两个平台都可用。

要获得所需的库(libraries)，Android开发人员应该使用[TensorFlow Lite AAR](android.md#use_the_tensorflow_lite_aar_from_jcenter)。iOS开发人员应该使用[CocoaPods for Swift or Objective-C](ios.md#add_tensorflow_lite_to_your_swift_or_objective-c_project)。

### Linux

嵌入式Linux是一个部署机器学习的重要平台。我们为[Raspberry Pi](build_rpi.md) 和[基于Arm64的主板](build_arm64.md)，如Odroid C2, Pine64, 和NanoPi，提供了构建说明。

### 微控制器

[用于微控制器(Microcontrollers)的TensorFlow Lite](../microcontrollers/overview.md)是一个TensorFlow Lite的实验端口，该端口针对只有几千字节(kilobytes)内存(memory)的微控制器和其他设备。

### 运算符

如果您的模型需要TensorFlow Lite中尚未实现的TensorFlow运算符(operations)，您可以使用[TensorFlow Select](ops_select.md)在模型中使用它们。您需要构建一个包含TensorFlow运算符的自定义版本解释器。

您可以用[自定义运算符(Custom operators)](ops_custom.md)编写自己的操作，或将新操作移植到TensorFlow Lite中。

[运算符版本(Operator versions)](ops_version.md)让您能为已有的运算符添加新的功能和参数。

## 4. 优化您的模型

<a id="4_optimize_your_model_optional"></a>

TensorFlow Lite提供了优化模型大小(size)和性能(performance)的工具，通常对准确率(accuracy)影响甚微。优化模型可能需要稍微复杂的训练(training)，转换(conversion)或集成(integration)。

机器学习优化是一个不断发展的领域，TensorFlow Lite的[模型优化工具包(Model Optimization Toolkit)](#模型优化工具包)随着新技术的发展而不断发展。

### 性能

模型优化的目标是在给定设备上，实现性能(performance)，模型大小(model size)，和正确率(accuracy)的理想平衡。
[性能最佳实践(Performance best practices)](../performance/best_practices.md)能帮助您通过这个过程实现目标。

### 量化

通过降低模型中数值(values)和运算符(operations)的精度(precision)，量化(quantization)可以减小模型的大小和推理所需的时间。对很多模型，只有极小的正确率(accuracy)损失。

TensorFlow Lite转换器让量化TensorFlow模型变得简单。下面的Python代码量化了一个`SavedModel`并将其保存在硬盘中：

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_quant_model = converter.convert()
open("converted_model.tflite","wb").write(tflite_quant_model)
```

要了解有关量化的更多信息，请参阅[训练后量化(Post-training quantization)](../performance/post_training_quantization.md)。

### 模型优化工具包

[模型优化工具包(Model Optimization Toolkit)](../performance/model_optimization.md)是一套工具和技术，旨在使开发人员可以轻松优化它们的模型。其中的许多技术可以应用于所有TensorFlow模型，并非特定于TensorFlow Lite，但在资源有限的设备上进行推断时，它们特别有用。

## 下一步

既然您已经熟悉了TensorFlow Lite，请探索以下一些资源：

*	如果您是移动开发人员，请访问[Android快速入门](android.md)或[iOS快速入门](ios.md)。
*	探索我们的[预训练模型](../models)。
*	尝试我们的[示例应用](https://www.tensorflow.org/lite/examples)。
