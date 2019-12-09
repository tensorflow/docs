# TensorFlow Lite for Microcontrollers

TensorFlow Lite for Microcontrollers 是 TensorFlow Lite 的一个实验性移植版本，它适用于微控制器和其他一些仅有数千字节内存的设备。

它可以直接在“裸机”上运行，不需要操作系统支持、任何标准 C/C++ 库和动态内存分配。核心运行时(core runtime)在 Cortex M3 上运行时仅需 16KB，加上足以用来运行语音关键字检测模型的操作，也只需 22KB 的空间。

## 开始

要快速入门并运行 TensorFlow Lite for Microcontrollers，请阅读[微控制器入门](get_started.md)。

## 为什么微控制器很重要

微控制器通常是小型、低能耗的计算设备，经常嵌入在只需要进行基本运算的硬件中，包括家用电器和物联网设备等。每年都有数十亿个微控制器被生产出来。

微控制器通常针对低能耗和小尺寸进行优化，但代价是降低了处理能力、内存和存储。一些微控制器具有用来优化机器学习任务性能的功能。

通过在微控制器上运行机器学习推断，开发人员可以在不依赖于网络连接的情况下将 AI 添加到各种各样的硬件设备中，这经常用来克服带宽、功率以及由它们所导致的高延迟而造成的约束。在设备上运行推断也可以帮助保护隐私，因为没有数据从设备中发送出去。

## 功能和组件

*   C++ API，其运行时(runtime)在 Cortex M3 上仅需 16KB
*   使用标准的 TensorFlow Lite [FlatBuffer](https://google.github.io/flatbuffers/)
    架构(schema)
*   为 Arduino、Keil 和 Mbed 等较为流行的嵌入式开发平台预生成的项目文件
*   针对多个嵌入式平台优化
*   演示口语热词检测的[示例代码](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/examples/micro_speech)

## 开发工作流程

这是将 TensorFlow 模型部署到微控制器的过程：

1. **创建或获取 TensorFlow 模型**

    该模型必须非常小，以便在转换后适合您的目标设备。它只能使用[支持的操作](build_convert.md#支持的操作)。如果要使用当前不被支持的操作，可以提供自己的实现。

2. **将模型转换为 TensorFlow Lite FlatBuffer**

    您将使用 [TensorFlow Lite 转换器](build_convert.md#转换模型)来将模型转换为标准 TensorFlow Lite 格式。您可能希望输出量化模型，因为它们的尺寸更小、执行效率更高。

3. **将 FlatBuffer 转换为 C byte 数组**

    模型保存在只读程序存储器中，并以简单的 C 文件的形式提供。标准工具可用于[将 FlatBuffer 转换为 C 数组](build_convert.md#转换为-C-数组)。

4. **集成 TensorFlow Lite for Microcontrollers 的 C++ 库**

    编写微控制器代码以使用 [C++ 库](library.md)执行推断。

5. **部署到您的设备**

    构建程序并将其部署到您的设备。

## 支持的平台

嵌入式软件开发的挑战之一是存在许多不同的体系结构、设备、操作系统和构建系统。我们的目标是尽可能多地支持流行的组合，并尽可能地让给其他设备添加支持变得简单。

如果您是产品开发人员，您可以下载我们提供的以下平台的构建说明或预生成的项目文件：

设备                                                                                          | Mbed                                                                     | Keil                                                                     | Make/GCC
------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | --------
[STM32F746G Discovery Board](https://www.st.com/en/evaluation-tools/32f746gdiscovery.html)  | [下载](https://drive.google.com/open?id=1OtgVkytQBrEYIpJPsE8F6GUKHPBS3Xeb) | -                                                                        | [下载](https://drive.google.com/open?id=1u46mTtAMZ7Y1aD-He1u3R8AE4ZyEpnOl)
["Blue Pill" STM32F103 兼容开发板](https://github.com/google/stm32_bare_lib)                     | -                                                                        | -                                                                        | [说明](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/README.md#building-for-the-blue-pill-stm32f103-using-make)
[Ambiq Micro Apollo3Blue EVB（使用 Make）](https://ambiqmicro.com/apollo-ultra-low-power-mcus/) | -                                                                        | -                                                                        | [说明](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/README.md#building-for-ambiq-micro-apollo3blue-evb-using-make)
[Generic Keil uVision Projects](http://www2.keil.com/mdk5/uvision/)                         | -                                                                        | [下载](https://drive.google.com/open?id=1Lw9rsdquNKObozClLPoE5CTJLuhfh5mV) | -
[Eta Compute ECM3531 EVB](https://etacompute.com/)                                          | -                                                                        | -                                                                        | [说明](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/README.md#Building-for-the-Eta-Compute-ECM3531-EVB-using-Make)

如果您的设备尚未被支持，添加支持也许并不困难。您可以在
[README.md](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/README.md#how-to-port-tensorflow-lite-micro-to-a-new-platform)
中了解该过程。

### 可移植参考代码

如果您还没有考虑具体的的微控制器平台，或者只想在开始移植之前试用代码，最简单的方法是[下载与平台无关的参考代码](https://drive.google.com/open?id=1cawEQAkqquK_SO4crReDYqf_v7yAwOY8)。

归档中有很多文件夹，每个文件夹只包含构建一个二进制文件所需的源文件。每个文件夹都有一个简单的 Makefile 文件，您应该能够将文件加载到几乎任何 IDE 中并构建它们。我们还提供了已经设置好的 [Visual Studio Code](https://code.visualstudio.com/) 项目文件，因此您可以轻松地在跨平台 IDE 中浏览代码。

## 目标

我们的设计目标是使框架可读、易于修改、经过良好测试、易于集成，并通过一致的文件架构、解释器、API 和内核接口与 TensorFlow Lite 完全兼容。

您可以阅读更多在[目标和权衡](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro#goals)方面有关设计的信息。

## 限制

TensorFlow Lite for Microcontrollers 专为微控制器开发中的特殊限制而设计。如果您正在使用更强大的设备（例如像 Raspberry Pi 这样的嵌入式 Linux 设备），标准的 TensorFlow Lite 框架可能更容易集成。

应考虑以下限制：

* 仅支持 TensorFlow 操作的[有限子集](build_convert.md#支持的操作)
* 仅支持有限的一些设备
* 低级 C++ API 需要手动内存管理
