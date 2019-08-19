# 性能的最佳实践

由于移动和嵌入式设备的运算能力有限，所以保持应用的资源被高效利用是非常重要的。我们已经编写了一份最佳实践和策略的清单，你能用它来优化你的 TensorFlow Lite 模型和应用。

## 为任务选择最佳的模型

根据任务的不同，你会需要在模型复杂度和大小之间做取舍。如果你的任务需要高准确率，那么你可能需要一个大而复杂的模型。对于精确度不高的任务，就最好使用小一点的模型，因为小的模型不仅占用更少的磁盘和内存，也一般更快更高效。比如，下图展示了常见的图像分类模型中准确率和延迟对模型大小的影响。

![模型大小和准确度的关系图](../images/performance/model_size_vs_accuracy.png "模型大小和准确度")

![准确度和延迟时间的关系图](../images/performance/accuracy_vs_latency.png "准确度和延迟时间")

一个针对移动设备优化的示例模型就是 [MobileNets](https://arxiv.org/abs/1704.04861)，该模型是为了移动端视觉应用而优化的。我们的 [模型列表](../models/hosted.md) 列出了另外几种专为移动和嵌入式设备优化的模型。

你可以用你自己的数据通过迁移学习再训练这些模型。查看我们的迁移学习教程：[图像分类](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0) 和 [物体检测](https://medium.com/tensorflow/training-and-serving-a-realtime-mobile-object-detector-in-30-minutes-with-cloud-tpus-b78971cf1193)。

## 测试你的模型

在选择了一个适合你的任务的模型之后，测试该模型和设立基准很好的行为。TensorFlow Lite [测试工具](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark) 有内置的测试器，可展示每一个运算符的测试数据。这能帮助理解性能瓶颈和哪些运算符主导了运算时间。

## 测试和优化图（graph）中的运算符

如果某个特定的运算符频繁出现在模型中，并且基于测试你发现这个运算符消耗了大部分时间，那么你可以研究如何优化这个运算符。这种情况应该非常少见，因为 TensorFlow Lite 中的大部分运算符都是优化过的版本。然而，如果你了解该运算符的运行限制，你或许可以写一个自定义的更快的版本。查看我们的 [自定义运算符文档](../custom_operators.md)。

## 优化你的模型

模型压缩旨在创建更小的模型，并且通常更快、更高效节能。因此它们能被部署到移动设备上。

### 量化

如果你的模型使用浮点权重或者激励函数，那么模型大小或许可以通过量化减少75%，该方法有效地将浮点权重从32字节转化为8字节。量化分为：[训练后量化](post_training_quantization.md) 和 [量化训练](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/quantize/README.md){:.external}。前者不需要再训练模型，但是在极少情况下会有精度损失。当精度损失超过了可接受范围，则应该使用量化训练。

我们强烈推荐设立基准以确保模型压缩期间准确率没有被影响。查看详细信息：[模型优化文档](model_optimization.md)。

## 调整线程数

TensorFlow Lite 支持针对多运算符使用多线程内核。你可以增加线程数以提高运算符运行速度。然而，增加线程数会使你的模型使用更多的资源和能源。

对有些应用来说，延迟或许比能源效率更重要。你可以通过设定 [解释器](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/interpreter.h#L346) 的数量来增加线程数。然而，根据同时运行的其他操作不同，多线程运行会增加性能的可变性。比如，隔离测试可能显示多线程的速度是单线程的两倍，但如果同时有另一个应用在运行的话，性能测试结果可能比单线程更差。

## 清除冗余副本

如果你的应用没有被很好地设计，在输入模型和读取模型输出时可能会有冗余副本。应确保清除冗余副本。如果你在使用高层 API，如 Java，请确保仔细阅读性能注意事项。比如，如果使用 ByteBuffers 作为[输入](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/java/src/main/java/org/tensorflow/lite/Interpreter.java#L175)，Java API 会快得多。

## 用平台特定工具测试你的应用

平台特定工具，如 [Android profiler](https://developer.android.com/studio/profile/android-profiler) 和 [Instruments](https://help.apple.com/instruments/mac/current/)，提供了丰富的可被用于调试应用的测试信息。有时性能问题可能不出自于模型，而是与模型交互的应用代码。确保熟悉平台特定测试工具和对该平台最好的测试方法。

## 评估你的模型是否受益于使用设备上可用的硬件加速器

TensorFlow Lite 增加了新的方法来配合更快的硬件加速模型，比如 GPU、DSP 和神经加速器。一般来说，这些加速器通过 [代理](delegates.md) 子模块暴露，这些子模块接管部分解释器执行。TensorFlow Lite 能通过以下方法使用代理：

*   使用 Android 的 [神经网络 API](https://developer.android.com/ndk/guides/neuralnetworks/)。你可以利用这些硬件加速器后台来提升模型速度和效率。要启用神经网络 API，在解释器实例内调用 [UseNNAPI](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/interpreter.h#L343)。
*   我们已经发布了一个仅限二进制的 GPU 代理，Android 和 iOS 分别使用 OpenGL 和 Metal。要试用它们，查看 [GPU 代理教程](gpu.md) 和 [文档](gpu_advanced.md)。
*   如果你能访问非标准硬件，也可以创建你自己的代理。更多信息，查看 [TensorFlow Lite 代理](delegates.md)。

请注意，有的加速器在某些模型效果更好。为每个代理设立基准以测试出最优的选择是很重要的。比如，如果你有一个非常小的模型，那可能没必要将模型委托给 NN API 或 GPU。相反，对于具有高算术强度的大模型来说，加速器就是一个很好的选择。

## 需要更多帮助？

TensorFlow 团队非常乐意帮助你诊断和定位具体的性能问题。请在 [GitHub](https://github.com/tensorflow/tensorflow/issues) 提出问题并描述细节。
