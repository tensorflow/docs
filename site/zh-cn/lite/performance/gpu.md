# TensorFlow Lite GPU 代理

[TensorFlow Lite](https://www.tensorflow.org/lite) 支持多种硬件加速器。本文档描述了如何在 Android 和 iOS 设备上使用 TensorFlow Lite 的代理 APIs 来预览实验性的 GPU 后端功能。

GPU 是设计用来完成高吞吐量的大规模并行工作的。因此，它们非常适合用在包含大量运算符的神经网络上，一些输入张量可以容易的被划分为更小的工作负载且可以同时执行，通常这会导致更低的延迟。在最佳情况下，用 GPU 在实时应用程序上做推理运算已经可以运行的足够快，而这在以前是不可能的。

不同于 CPU 的是，GPU 可以计算 16 位浮点数或者 32 位浮点数并且 GPU 不需要量化来获得最佳的系统性能。

使用 GPU 做推理运算还有一个好处就是它的能源效率。GPU 可以以非常高效和优化的方式下进行计算，所以 GPU 在完成和 CPU 一样的任务时可以消耗更少的电力和产生更少的热量。

## 演示应用程序教程

最简单的尝试实验 GPU 代理的方法就是跟着下面的教程，教程将贯串我们整个使用 GPU 构建的分类演示应用程序。GPU 代码现在只有二进制的形式，但是很快就会开源。一旦你理解了如何把我们的演示程序运行起来，你就可以在你自己的模型上尝试。

### Android（使用 Android Studio）

如果需要一个分步教程, 请观看
[适用于 Android 的实验性 GPU 代理](https://youtu.be/Xkhgre8r5G0) 的视频。

注意：这需要 OpenGL ES 3.1或者更高版本

#### 第一步 克隆 TensorFlow 的源代码并在 Android Studio 中打开

```
git clone https://github.com/tensorflow/tensorflow
```

#### 第二步 编辑 `app/build.gradle` 文件来使用 nightly 版本的 GPU AAR

在现有的 `dependencies` 模块已有的 `tensorflow-lite` 包的位置下添加 `tensorflow-lite-gpu` 包。

```
dependencies {
    ...
    implementation 'org.tensorflow:tensorflow-lite:0.0.0-nightly'
    implementation 'org.tensorflow:tensorflow-lite-gpu:0.0.0-nightly'
}
```

#### 第三步. 编译和运行

点击 Run 按钮来运行应用程序。当你运行应用程序的时候你会看到一个启用 GPU 的按钮。将应用程序从量化模式改为浮点模式后点击 GPU 按钮后，程序将在 GPU 上运行。

![运行 Android gpu 演示应用程序和切换到 GPU](images/android_gpu_demo.gif)

### iOS (使用 XCode)

如果需要一个分步教程, 请观看
[适用于 iOS 的实验性 GPU 代理](https://youtu.be/Xkhgre8r5G0) 的视频。

注意：这需要 XCode 10.1 或者更高版本

#### 第一步. 获取演示应用程序的源码并确保它已被编译

遵照我们的 iOS 演示应用程序[教程](https://www.tensorflow.org/lite/demo_ios)。这会告诉你没有修改的iOS相机应用程序是如何在我们的手机上运行的。

#### 第二部. 修改 Podfile 文件来使用 TensorFlow Lite GPU CocoaPod

我们构建了一个包含 GPU 代理的二进制 CocoaPod 文件。如果需要切换到工程并使用它，修改
`tensorflow/tensorflow/lite/examples/ios/camera/Podfile` 文件来使用  `TensorFlowLiteGpuExperimental` 的 pod 替代 `TensorFlowLite`。

```
target 'YourProjectName'
  # pod 'TensorFlowLite', '1.12.0'
  pod 'TensorFlowLiteGpuExperimental'
```

#### 第三步. 启用 GPU 代理

为了确保代码会使用 GPU 代理，你需要将 `CameraExampleViewController.h` 的
`TFLITE_USE_GPU_DELEGATE` 从 0 修改为 1 。

```c
#define TFLITE_USE_GPU_DELEGATE 1
```

#### 第四步. 编译和运行演示应用程序

如果你完成了上面的步骤，你应该已经可以运行这个应用程序了。

#### 第五步. 发布模式

你在第四步是在调试模式下运行的应用程序，为了获得更好的性能表现，你应该使用适当的最佳 Metal 设置将应用程序改为发布版本。特别需要注意的是，需要修改这些设置 `Product > Scheme > Edit
Scheme...`，选择 ` Run `，在 ` Info ` 一栏，修改 ` Build Configuration `，从 `Debug ` 改为 ` Release `，取消选择 ` Debug executable`。

![设置发布](images/iosdebug.png)

然后点击 `Options` 栏然后将 `GPU Frame Capture` 修改成 `Disabled`，并将 `Metal API Validation` 修改成 `Disabled`。

![设置 metal 选项](images/iosmetal.png)

最后需要确保发布版本只能在 64 位系统上构建。在 `Project
navigator -> tflite_camera_example -> PROJECT -> tflite_camera_example -> Build
Settings` 上将 `Build Active Architecture Only > Release`选择为 Yes。

![设置发布选项](images/iosrelease.png)

## 在你自己的模型上使用GPU代理

### Android

查看演示应用程序来了解如何添加代理。在你的应用程序中，像上面一样添加 AAR ，导入`org.tensorflow.lite.gpu.GpuDelegate` 模块，并使用 `addDelegate` 功能将GPU代理注册到解释器中。

```java
import org.tensorflow.lite.Interpreter;
import org.tensorflow.lite.gpu.GpuDelegate;

// 初始化使用 GPU 代理的解释器
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);
Interpreter interpreter = new Interpreter(model, options);

// 进行推理
while (true) {
  writeToInput(input);
  interpreter.run(input, output);
  readFromOutput(output);
}

// 清理
delegate.close();
```

### iOS
 
在你的应用程序代码中，引入 GPU 代理头文件来让`Interpreter::ModifyGraphWithDelegate` 功能将 GPU 代理注册到解释器中。

```cpp
#import "tensorflow/lite/delegates/gpu/metal_delegate.h"

// 初始化使用 GPU 代理的解释器
std::unique_ptr<Interpreter> interpreter;
InterpreterBuilder(*model, resolver)(&interpreter);
auto* delegate = NewGpuDelegate(nullptr);  // default config
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// 进行推理 
while (true) {
  WriteToInputTensor(interpreter->typed_input_tensor<float>(0));
  if (interpreter->Invoke() != kTfLiteOk) return false;
  ReadFromOutputTensor(interpreter->typed_output_tensor<float>(0));
}

// 清理
interpreter = nullptr;
DeleteGpuDelegate(delegate);
```

## 支持的模型和 Ops

在 GPU 代理发布后，我们提供了少数可以在后端运行的模型：

* [MobileNet v1 (224x224)图像分类](https://ai.googleblog.com/2017/06/mobilenets-open-source-models-for.html) [[下载]](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/mobilenet_v1_1.0_224.tflite)
<br /><i>(为移动和嵌入式视觉应用设计的图像分类模型)</i>
* [DeepLab 分割 (257x257)](https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html) [[下载]](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/deeplabv3_257_mv_gpu.tflite)
<br /><i>(将输入图像的每个像素指定语义标签（例如，狗，猫。汽车的图像分割模型)</i>
* [MobileNet SSD 物体检测](https://ai.googleblog.com/2018/07/accelerated-training-and-inference-with.html) [[下载]](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/mobile_ssd_v2_float_coco.tflite)
<br /><i>(用于检测多个带有边框的对象的图像分类模型)</i>
* [PoseNet用于姿势估计](https://github.com/tensorflow/tfjs-models/tree/master/posenet) [[下载]](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/multi_person_mobilenet_v1_075_float.tflite)
<br /><i>(用于估计图像或视频中人物的姿势的视觉模型)</i>

如果需要完整的支持的 Ops 的列表，请看[进阶文档](gpu_advanced.md)。

## 不支持的模型和 ops

如果一些 ops 并不支持 GPU 代理，框架只会在 GPU 上运行图形的一部分，剩下的部分会在 CPU 上运行。因为这会导致 CPU/GPU 同时出现很高的使用率，像这样的分开执行模式会导致运行起来比整个网络在 CPU 上运行要慢。在这种情况下，用户会收到一个像这样的警告：

```
WARNING: op code #42 cannot be handled by this delegate.
```

```
警告：此代理无法处理#42操作码
```

我们没有为这种失败提供回调，因为这不是真的运行错误，但是这个错误是开发者可以注意到的，他们可以尝试将整个网络在代理上运行。

## 优化建议

一些在 CPU 上的琐碎的的操作可能在 GPU 上会有很高的占用。其中的一种操作就是很多形式的 reshape 操作，像 `BATCH_TO_SPACE`, `SPACE_TO_BATCH`, `SPACE_TO_DEPTH` 等等。如果这些 ops 只是为了方便网络构架师的逻辑思考而放置在网络中，为了更好的性能将他们在网络中移除是值得的。

在 GPU 上，张量数据被分成4个通道。因此，计算一个 `[B,H,W,5]` 的张量和计算 `[B,H,W,8]`的效果是一样的，但是它们都比运行 `[B,H,W,4]` 的性能要差的多。

从这个意义上讲，如果相机硬件支持 RGBA 形式图像帧，4 通道输入明显更快因为可以避免内存复制(从 3 通道 RGB 转变到 4 通道 RGBX）。

为了获得最佳性能，请不要犹豫，使用移动优化的网络架构来重新训练您的分类器。这是优化设备推断性能的重要部分。
