#  TensorFlow Lite 在GPU环境下

[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)支持多种硬件加速器。本文档介绍如何在安卓系统（要求OpenGL ES 3.1或更高版本）和iOS（要求iOS 8 或更高版本）的GPU后端（backend）使用TensorFLow Lite delegate APIs。

## 使用GPU加速的优势

### 速度

GPUs 设计为具有高吞吐量、可大规模并行化的工作负载（workloads）。因此，它们非常适合于一个由大量运算符组成的深度神经网络，其中每一个GPU都可以处理一些输入张量（tensor）并且容易划分为较小的工作负载（workloads），然后并行执行。这样并行性通常能够有较低的延迟。在最好的情况下，在GPU上推断（inference）可以运行得足够快，以适应实时程序，这在以前是不可能的。

### 精度

GPU使用16位或32位浮点数进行运算，并且（与CPU不同）不需要量化（quantization）以获得最佳的性能。如果精度降低使得模型的量化（quantization）无法达到要求，那么在GPU上运行神经网络可能可以消除这种担忧。

### 能效

使用GPU进行推断（inference）的另一个好处在于它的能效。GPU能以非常有效和优化方法来进行运算，比在CPU上运行相同任务消耗更少的能源并产生更少的发热量。

### 支持的Ops

TensorFlow Lite 在GPU上支持16位和32位浮点精度中的以下操作：

* `ADD v1`
* `AVERAGE_POOL_2D v1`
* `CONCATENATION v1`
* `CONV_2D v1`
* `DEPTHWISE_CONV_2D v1-2`
* `FULLY_CONNECTED v1`
* `LOGISTIC v1`
* `MAX_POOL_2D v1`
* `MUL v1`
* `PAD v1`
* `PRELU v1`
* `RELU v1`
* `RELU6 v1`
* `RESHAPE v1`
* `RESIZE_BILINEAR v1`
* `SOFTMAX v1`
* `STRIDED_SLICE v1`
* `SUB v1`
* `TRANSPOSE_CONV v1`

## 基本用法

### Android (Java)

使用`TfLiteDelegate`在GPU上运行TensorFlow Lite，在Java中，您可以通过`Interpreter.Options`来指定GpuDelegate。

```java
// NEW: Prepare GPU delegate.
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);

// Set up interpreter.
Interpreter interpreter = new Interpreter(model, options);

// Run inference.
writeToInputTensor(inputTensor);
interpreter.run(inputTensor, outputTensor);
readFromOutputTensor(outputTensor);

// Clean up.
delegate.close();
```

### Android (C/C++)

在Android GPU上使用C/C++语言的TensorFlow Lite，可以使用`TfLiteGpuDelegateCreate()`创建，并使用`TfLiteGpuDelegateDelete()`销毁。

```c++
// Set up interpreter.
auto model = FlatBufferModel::BuildFromFile(model_path);
if (!model) return false;
ops::builtin::BuiltinOpResolver op_resolver;
std::unique_ptr<Interpreter> interpreter;
InterpreterBuilder(*model, op_resolver)(&interpreter);

// NEW: Prepare GPU delegate.
const TfLiteGpuDelegateOptions options = {
  .metadata = NULL,
  .compile_options = {
    .precision_loss_allowed = 1,  // FP16
    .preferred_gl_object_type = TFLITE_GL_OBJECT_TYPE_FASTEST,
    .dynamic_batch_enabled = 0,   // Not fully functional yet
  },
};
auto* delegate = TfLiteGpuDelegateCreate(&options);
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
WriteToInputTensor(interpreter->typed_input_tensor<float>(0));
if (interpreter->Invoke() != kTfLiteOk) return false;
ReadFromOutputTensor(interpreter->typed_output_tensor<float>(0));

// NEW: Clean up.
TfLiteGpuDelegateDelete(delegate);
```

适用于Android C / C ++的TFLite GPU使用[Bazel](https://bazel.io)构建系统。例如，可以使用以下命令构建委托（delegate）：

```sh
bazel build -c opt --config android_arm64 tensorflow/lite/delegates/gpu:gl_delegate                  # for static library
bazel build -c opt --config android_arm64 tensorflow/lite/delegates/gpu:libtensorflowlite_gpu_gl.so  # for dynamic library
```

### iOS(ObjC++)

要在GPU上运行TensorFlow Lite，需要通过`NewGpuDelegate()`对GPU委托（delegate），然后将其传递给`Interpreter::ModifyGraphWithDelegate()`（而不是调用`Interpreter::AllocateTensors()`）

```c++
// Set up interpreter.
auto model = FlatBufferModel::BuildFromFile(model_path);
if (!model) return false;
tflite::ops::builtin::BuiltinOpResolver op_resolver;
std::unique_ptr<Interpreter> interpreter;
InterpreterBuilder(*model, op_resolver)(&interpreter);

// NEW: Prepare GPU delegate.

const GpuDelegateOptions options = {
  .allow_precision_loss = false,
  .wait_type = kGpuDelegateOptions::WaitType::Passive,
};

auto* delegate = NewGpuDelegate(options);
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
WriteToInputTensor(interpreter->typed_input_tensor<float>(0));
if (interpreter->Invoke() != kTfLiteOk) return false;
ReadFromOutputTensor(interpreter->typed_output_tensor<float>(0));

// Clean up.
DeleteGpuDelegate(delegate);
```

注意：调用`Interpreter::ModifyGraphWithDelegate()`或`Interpreter::Invoke()`时，调用者必须在当前线程中有一个`EGLContext`，并且从同一个`EGLContext`中调用`Interpreter::Invoke()`。如果`EGLContext`不存在，委托（delegate）将在内部创建一个，但是开发人员必须确保始终从调用`Interpreter::Invoke()`的同一个线程调用`Interpreter::ModifyGraphWithDelegate()`。

## 高级用法

### 委托（Delegate）iOS 选项

`NewGpuDelegate()`接受一个 `struct` 选项。

```c++
struct GpuDelegateOptions {
  // Allows to quantify tensors, downcast values, process in float16 etc.
  bool allow_precision_loss;

  enum class WaitType {
    // waitUntilCompleted
    kPassive,
    // Minimize latency. It uses active spinning instead of mutex and consumes
    // additional CPU resources.
    kActive,
    // Useful when the output is used with GPU pipeline then or if external
    // command encoder is set
    kDoNotWait,
  };
  WaitType wait_type;
};
```

将`nullptr`传递给`NewGpuDelegate()`，并设置默认选项（即在上面的基本用法示例中阐述）。

```c++
// THIS:
const GpuDelegateOptions options = {
  .allow_precision_loss = false,
  .wait_type = kGpuDelegateOptions::WaitType::Passive,
};

auto* delegate = NewGpuDelegate(options);

// IS THE SAME AS THIS:
auto* delegate = NewGpuDelegate(nullptr);
```

虽然使用`nullptr`很方便，但我们建议您指定设置选项，以避免在以后更改默认值时出现任何异常情况。

### 输入/输出缓冲器

要想在GPU上进行计算，数据必须能够让GPU可见。这通常需要进行内存复制。如果可以的话，最好不要交叉CPU / GPU内存边界，因为这会占用大量时间。通常来说，这种交叉是不可避免的，但在某些特殊情况下，可以忽略其中一个。

如果网络的输入是已经加载到GPU内存中的图像（例如，包含相机传输的GPU纹理），那么可以直接保留在GPU内存中而无需进入到CPU内存。同样，如果网络的输出采用可渲染图像的格式（例如， [image style transfer](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)_)，那么它可以直接显示在屏幕上。

为了获得最佳性能，TensorFlow Lite让用户可以直接读取和写入TensorFlow硬件缓冲区并绕过可避免的内存副本。

#### Android

假设图像送入在GPU存储器中，则必须首先将其转换为OpenGL着色器存储缓冲区对象（SSBO）。您可以使用`Interpreter.bindGlBufferToTensor()`将TfLiteTensor与用户准备的SSBO相关联。注意：`Interpreter.bindGlBufferToTensor()`必须在`Interpreter.modifyGraphWithDelegate()`之前调用。

```java
// Ensure a valid EGL rendering context.
EGLContext eglContext = eglGetCurrentContext();
if (eglContext.equals(EGL_NO_CONTEXT)) return false;

// Create an SSBO.
int[] id = new int[1];
glGenBuffers(id.length, id, 0);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, id[0]);
glBufferData(GL_SHADER_STORAGE_BUFFER, inputSize, null, GL_STREAM_COPY);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);  // unbind
int inputSsboId = id[0];

// Create interpreter.
Interpreter interpreter = new Interpreter(tfliteModel);
Tensor inputTensor = interpreter.getInputTensor(0);
GpuDelegate gpuDelegate = new GpuDelegate();
// The buffer must be bound before the delegate is installed.
gpuDelegate.bindGlBufferToTensor(inputTensor, inputSsboId);
interpreter.modifyGraphWithDelegate(gpuDelegate);

// Run inference; the null input argument indicates use of the bound buffer for input.
fillSsboWithCameraImageTexture(inputSsboId);
float[] outputArray = new float[outputSize];
interpreter.runInference(null, outputArray);
```

类似的方法可以应用于输出张量(tensor)。在这种情况下，`Interpreter.Options.setAllowBufferHandleOutput(true)`应该被用来传递，来禁用从GPU内存到CPU内存的网络输出复制的默认操作。

```java
// Ensure a valid EGL rendering context.
EGLContext eglContext = eglGetCurrentContext();
if (eglContext.equals(EGL_NO_CONTEXT)) return false;

// Create a SSBO.
int[] id = new int[1];
glGenBuffers(id.length, id, 0);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, id[0]);
glBufferData(GL_SHADER_STORAGE_BUFFER, outputSize, null, GL_STREAM_COPY);
glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);  // unbind
int outputSsboId = id[0];

// Create interpreter.
Interpreter.Options options = (new Interpreter.Options()).setAllowBufferHandleOutput(true);
Interpreter interpreter = new Interpreter(tfliteModel, options);
Tensor outputTensor = interpreter.getOutputTensor(0);
GpuDelegate gpuDelegate = new GpuDelegate();
// The buffer must be bound before the delegate is installed.
gpuDelegate.bindGlBufferToTensor(outputTensor, outputSsboId);
interpreter.modifyGraphWithDelegate(gpuDelegate);

// Run inference; the null output argument indicates use of the bound buffer for output.
ByteBuffer input = getCameraImageByteBuffer();
interpreter.runInference(input, null);
renderOutputSsbo(outputSsboId);
```

#### iOS

假设图像送入在GPU存储器中，则必须首先将其转换为Metal的`MTLBuffer`对象。您可以将TfLiteTensor与用户准备的`MTLBuffer`和`BindMetalBufferToTensor()`相关联。注意：必须在`Interpreter::ModifyGraphWithDelegate()`之前调用`BindMetalBufferToTensor()`。此外，默认情况下，推断（inference）结果的输出，会从GPU内存复制到CPU内存。在初始化期间调用`Interpreter::SetAllowBufferHandleOutput(true)`可以关闭该操作。

```c++
// Prepare GPU delegate.
auto* delegate = NewGpuDelegate(nullptr);
interpreter->SetAllowBufferHandleOutput(true);  // disable default gpu->cpu copy
if (!BindMetalBufferToTensor(delegate, interpreter->inputs()[0], user_provided_input_buffer)) return false;
if (!BindMetalBufferToTensor(delegate, interpreter->outputs()[0], user_provided_output_buffer)) return false;
if (interpreter->ModifyGraphWithDelegate(delegate) != kTfLiteOk) return false;

// Run inference.
if (interpreter->Invoke() != kTfLiteOk) return false;
```

注意：一旦关闭从GPU内存复制到CPU内存的操作后，将推断（inference）结果输出从GPU内存复制到CPU内存需要为每个输出张量显式调用`Interpreter::EnsureTensorDataIsReadable()`。

## 提示与技巧

* 在CPU上执行一些微不足道的操作可能需要非常高的代价，譬如各种形式的reshape操作（包括`BATCH_TO_SPACE`，`SPACE_TO_BATCH`，`SPACE_TO_DEPTH`和其他类似的操作）。如果不需要这些操作（比如使用这些操作是为了帮助理解网络架构和了解整个系统但不会影响输出），那么值得删除它们以提高性能。
* 在GPU上，张量（tensor）数据被划分为4个通道（channel）。因此对形状为`[B, H, W, 5]` 的张量（tensor）的计算量大致与`[B, H, W, 8]`相同，但明显比`[B, H, W, 4]`要大。
  * 比如：如果相机的硬件支持RGBA，那么传输4通道（channel）数据的速度要快得多，因为可以避免内存复制（从3通道RGB到4通道RGBX）。
* 为了获得最佳性能，请不要犹豫使用移动优化过（mobile-optimized）的网络架构重新训练您的分类器。 这是设备推断（inference）优化的重要部分。

