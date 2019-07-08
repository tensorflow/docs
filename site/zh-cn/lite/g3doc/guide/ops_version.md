TensorFlow Lite 操作(operator)的版本

本文档描述了TensorFlow Lite的操作(operator)版本架构。 操作(operator)的版本使开发人员能够将新功能和参数添加到现有操作中。 此外，它保证以下内容：

* 向后兼容性：新版本的 TensorFlow Lite 实现方式可以处理旧的模型文件。
* 向前兼容性：只要没有使用新功能，旧版本的 TensorFlow Lite 实现方式可以处理由新版 TOCO 生成的新版本的模型文件。 
* 前向兼容性检测：如果旧的 TensorFlow Lite 实现读取包含不支持的新版本的模型，则应报告错误。

##示例：将膨胀(Dilation)添加到卷积操作中
本文档的其余部分通过展示如何在卷积操作中添加膨胀系数来解释 TFLite 中操作(operator)的版本。

了解本文档内容并不需要了解卷积核膨胀的知识。需要注意的是：

* 将添加2个新的整数参数：'dilation_width_factor' 和 'dilation_height_factor'。  
* 不支持膨胀的旧卷积核相当于将扩张因子膨胀系数设置为1。

### 更改 FlatBuffer 架构(Schema)

要将新参数添加到操作(operator)中，请更改`lite/schema/schema.fbs`中的选项表 。

例如，卷积的选项表如下所示：

```
table Conv2DOptions {
  padding:Padding;
  stride_w:int;
  stride_h:int;
  fused_activation_function:ActivationFunctionType;
}
```

在添加新参数时：

* 添加注释，指明哪个版本支持哪些参数。
* 当新的实现获取新添加的参数的默认值时，它应该与旧实现完全相同。

添加新参数后，参数表如下所示：

```
table Conv2DOptions {
  // 版本1支持的参数：
  padding:Padding;
  stride_w:int;
  stride_h:int;
  fused_activation_function:ActivationFunctionType;

  // Parameters supported by version 2:
  dilation_width_factor:int = 1;
  dilation_height_factor:int = 1;
}
```

### 更改C中的结构体和内核实现

在 TensorFlow Lite 中，内核实现与 FlatBuffer 定义分离。内核从 lite/builtin_op_data.h 中定义的 C 结构文件中读取参数 。
原始卷积参数如下：
```
typedef struct {
  TfLitePadding padding;
  int stride_width;
  int stride_height;
  TfLiteFusedActivation activation;
} TfLiteConvParams;
```
与 FlatBuffer 架构一样，添加注释，指明从哪个版本开始支持这些参数。结果如下：
```
typedef struct {
  // 版本1支持的参数：
  TfLitePadding padding;
  int stride_width;
  int stride_height;
  TfLiteFusedActivation activation;

  // Parameters supported by version 2:
  int dilation_width_factor;
  int dilation_height_factor;
} TfLiteConvParams;
```
请同时更改内核实现以从 C 结构中读取新添加的参数。具体细节省略。
### 更改 FlatBuffer 代码以获取新参数

读取 FlatBuffer 和生成 C 结构的逻辑是 lite/model.cc。
更新该文件以处理新参数，如下所示：
```
case BuiltinOperator_CONV_2D: {
  TfLiteConvParams* params = MallocPOD<TfLiteConvParams>();
  if (auto* conv_params = op->builtin_options_as_Conv2DOptions()) {
    params->padding = parse_padding(conv_params->padding());
    params->stride_width = conv_params->stride_w();
    params->stride_height = conv_params->stride_h();
    params->activation =
        parse_activation(conv_params->fused_activation_function());
    params->dilation_width_factor = conv_params->dilation_width_factor();
    params->dilation_height_factor = conv_params->dilation_height_factor();
  }
  *builtin_data = reinterpret_cast<void*>(params);
  break;
}
```
这里不需要检查操作版本。当新版本的阅读代码读取缺少膨胀系数的旧模型文件时，它将使用 1 作为默认值，并且新内核将与旧内核一致地工作。
## 改变内核注册
MutableOpResolver（定义于 lite/op_resolver.h）提供了一些注册 op 内核的函数。默认情况下，最小和最大版本号为1：
```
void AddBuiltin(tflite::BuiltinOperator op, TfLiteRegistration* registration,
                int min_version = 1, int max_version = 1);
void AddCustom(const char* name, TfLiteRegistration* registration,
               int min_version = 1, int max_version = 1);
```
内置操作已注册于 lite/kernels/register.cc 。在这个例子中，我们要实现一个新的 op 内核，可以处理 Conv2D 的版本 1 和 2，所以我们需要改变这一行：
```
AddBuiltin(BuiltinOperator_CONV_2D, Register_CONV_2D());
```
至：
```
AddBuiltin(BuiltinOperator_CONV_2D, Register_CONV_2D(), 1, 2);
```

### 改变 TOCO TFLite 的导出

最后一步是让 TOCO 填充执行操作所需的最低版本。在这个例子中，它意味着：
> 当膨胀系数均为1时，填充版本 = 1。                                                                       
> 否则填充版本 = 2。
为此，您需要在`lite/toco/tflite/operator.cc`中重写定义操作(operator)的类(class)中的`GetVersion`函数。

lite/toco/tflite/operator.cc。
对于只有一个版本的操作，该 GetVersion 函数定义为：
```
int GetVersion(const Operator& op) const override { return 1; }
```

当支持多个版本时，请检查参数并确定op的版本，如以下示例所示：

```
int GetVersion(const Operator& op) const override {
  const auto& conv_op = static_cast<const ConvOperator&>(op);
  if (conv_op.dilation_width_factor != 1 ||
      conv_op.dilation_height_factor != 1) {
    return 2;
  }
  return 1;
}
```

### 委托实现

TensorFlow Lite 提供了一个委托 API，可以将操作委派给硬件后端。在 Delegate 的 Prepare 函数中，检查该版本是否支持委派代码中的每个节点。
```
const int kMinVersion = 1;
TfLiteNode* node;
TfLiteRegistration;
context->GetNodeAndRegistration(context, node_index, &node, &registration);

if (registration->version > kMinVersion) {
  // 如果不支持该版本，则拒绝该节点。
}
```
即使委派仅支持版本1的操作，这也是必需的，这使委派可以在获得更高版本操作时检测到不兼容性。
