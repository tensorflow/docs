# TensorFlow Lite 代理

_说明：Delegate API 仍处于试验阶段并将随时进行调整。_

## 什么是 TensorFlow Lite 代理？

TensorFlow Lite 代理是一种将部分或全部的图形运算委托予另一线程执行的方法。

## 你为什么应该使用代理？

由于移动设备的处理能力不足以及电量受限，在其之上进行高算力的机器学习模型的演算是不可行的。

为了避免加重 CPU（中央处理器）的负担，一些设备具有诸如 GPU（图形处理器）或 DSP（数字信号处理器）等的硬件加速器以求获取更佳的性能与更高的能效。

## 使用 GPU 代理

TensorFlow Lite 为具备 GPU 的设备提供了一个 GPU 代理用以模型计算的加速。

有关 GPU 代理的概述，请查看
[TensorFlow Lite 在 GPU 环境下](https://www.tensorflow.org/lite/performance/gpu_advanced) 。
有关在 Android 和 iOS 设备上使用 GPU 代理的步骤教程，请查看
[TensorFlow Lite GPU 代理](https://www.tensorflow.org/lite/performance/gpu) 。

## 代理是如何运作的？

假设我们将一个简化的图形样本进行如下图所示的操作：

![原生图形样本](../images/performance/tflite_delegate_graph_1.png "原生图形样本")

如果把一个代理用于进行具体操作，那么 TensorFlow Lite 会将图形分割为多个交由代理进行处理的子图块。

若使用一个拥有高效处理 Conv2D（卷积层）和计算 Mean（平均值）操作的能力且名为“MyDelegate”的代理，那么它将导致主图变更为进行如下图所示的操作。

![使用代理的图形样本](../images/performance/tflite_delegate_graph_2.png "使用代理的图形样本")

在返回值中，每个交由代理进行处理的子图将会被更替为评估该子图的节点。

根据不同的模型，末图可以一个节点终结，这意味着所有的图将被代理或以多个节点的子图进行处理。一般而言，当你每次从代理切换至主图而不希望采用由代理处理的混合子图时，将会造成由子图转换为主图的损耗。毕竟，内存交换并非总是安全的。

## 如何添置一个代理

_请注意以下所采用的 API 仍处于试验阶段并将随时进行调整。_

基于上节所述，添置一个代理需要完成以下步骤：

1.  定义一个用于负责评估代理子图的核心节点
2.  创建一个用于负责注册该核心节点以及说明代理可用节点的实例 [TensorFlow Lite 代理](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/c/c_api_internal.h#L545)

为了使用代码进行说明，让我们定义一个可快速执行 Conv2D 和计算 Mean 操作的代理并将其命名为“MyDelegate”。

```
// 这是执行操作或整个图形的开始。
// 该类具有一个空实现，仅作结构体的声明。
class MyDelegate {
 public:
  // 如果代理可以处理此类操作，则返回“true”。
  static bool SupportedOp(const TfLiteRegistration* registration) {
    switch (registration->builtin_code) {
      case kTfLiteBuiltinConv2d:
      case kTfLiteBuiltinMean:
        return true;
      default:
        return false;
    }
  }

  // 代码初始化
  bool Init() {}
  // 初始工作分配（例如：分配缓冲区）
  bool Prepare(TfLiteContext* context, TfLiteNode* node) {}
  // 代理子图开始运行。
  bool Invoke(TfLiteContext* context, TfLiteNode* node) {}
  // ... 添加其他所需的方法
};

// 为核心节点创建一个替代主 TfLite 图中的子图的 TfLiteRegistration。
TfLiteRegistration GetMyDelegateNodeRegistration() {
  // 这是为了获取被添加至 TFLite 图而非替换它的子图的代理节点的初始化
  // 它被视为一个操作节点。
  // 但在此，Init 函数将用于初始化代理，而 Invoke 函数将用于运行代理图。
  // 预缓冲。
  // 释放内存。
  TfLiteRegistration kernel_registration;
  kernel_registration.builtin_code = kTfLiteBuiltinDelegate;
  kernel_registration.custom_name = "MyDelegate";
  kernel_registration.free = [](TfLiteContext* context, void* buffer) -> void {
    delete reinterpret_cast<MyDelegate*>(buffer);
  };
  kernel_registration.init = [](TfLiteContext* context, const char* buffer,
                                   size_t) -> void* {
    // 在节点的初始化阶段中，初始化“MyDelegate”实例。
    const TfLiteDelegateParams* delegate_params =
        reinterpret_cast<const TfLiteDelegateParams*>(buffer);
    MyDelegate* my_delegate = new MyDelegate;
    if (!my_delegate->Init(context, params)) {
      return nullptr;
    }
    return my_delegate;
  };
  kernel_registration.invoke = [](TfLiteContext* context,
                                   TfLiteNode* node) -> TfLiteStatus {
    MyDelegate* kernel = reinterpret_cast<MyDelegate*>(node->user_data);
    return kernel->Invoke(context, node);
  };
  kernel_registration.prepare = [](TfLiteContext* context,
                                    TfLiteNode* node) -> TfLiteStatus {
    MyDelegate* kernel = reinterpret_cast<MyDelegate*>(node->user_data);
    return kernel->Prepare(context, node);
  };

  return kernel_registration;
}

// 实现 TfLiteDelegate 方法

TfLiteStatus DelegatePrepare(TfLiteContext* context, TfLiteDelegate* delegate) {
  // 说明所有可被代理评估的节点以及请求框架使用代理核心替换图。
  // 当我们需要获取头节点的大小时，保留一个节点。
  std::vector<int> supported_nodes(1);
  TfLiteIntArray* plan;
  TF_LITE_ENSURE_STATUS(context->GetExecutionPlan(context, &plan));
  TfLiteNode* node;
  TfLiteRegistration* registration;
  for (int node_index : TfLiteIntArrayView(plan)) {
    TF_LITE_ENSURE_STATUS(context->GetNodeAndRegistration(
        context, node_index, &node, &registration));
    if (MyDelegate::SupportedOp(registration)) {
      supported_nodes.push_back(node_index);
    }
  }
  // 设置替换所有节点的头节点。
  supported_nodes[0] = supported_nodes.size() - 1;
  TfLiteRegistration my_delegate_kernel_registration =
      GetMyDelegateNodeRegistration();

  // 该返回值将图分割为子图块，对于子图，它将被代理视为一个  
  // ‘my_delegate_kernel_registration’进行处理。
  return context->ReplaceNodeSubsetsWithDelegateKernels(
      context, my_delegate_kernel_registration,
      reinterpret_cast<TfLiteIntArray*>(supported_nodes.data()), delegate);
}

void FreeBufferHandle(TfLiteContext* context, TfLiteDelegate* delegate,
                      TfLiteBufferHandle* handle) {
  // 用于实现释放内存的方法。
}

TfLiteStatus CopyToBufferHandle(TfLiteContext* context,
                                TfLiteDelegate* delegate,
                                TfLiteBufferHandle buffer_handle,
                                TfLiteTensor* tensor) {
  // 若有所需，复制 tensor（张量）的数据至代理的缓冲区。
  return kTfLiteOk;
}

TfLiteStatus CopyFromBufferHandle(TfLiteContext* context,
                                  TfLiteDelegate* delegate,
                                  TfLiteBufferHandle buffer_handle,
                                  TfLiteTensor* tensor) {
  // 从代理的缓冲区存入数据至 tensor 的原始内存区域。
  return kTfLiteOk;
}

// 回调函数获取返回指针的所有权。
TfLiteDelegate* CreateMyDelegate() {
  TfLiteDelegate* delegate = new TfLiteDelegate;

  delegate->data_ = nullptr;
  delegate->flags = kTfLiteDelegateFlagsNone;
  delegate->Prepare = &DelegatePrepare;
  // 该项不可为空。
  delegate->CopyFromBufferHandle = &CopyFromBufferHandle;
  // 该项可为空。
  delegate->CopyToBufferHandle = &CopyToBufferHandle;
  // 该项可为空。
  delegate->FreeBufferHandle = &FreeBufferHandle;

  return delegate;
}

// 添加你所需调用的代理

auto* my_delegate = CreateMyDelegate();
if (interpreter->ModifyGraphWithDelegate(my_delegate) !=
        kTfLiteOk) {
  // 用于实现解决异常的方法
} else {
  interpreter->Invoke();
}
...
// 最后千万要记住注销代理。
delete my_delegate;
```
