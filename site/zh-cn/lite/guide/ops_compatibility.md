# TensorFlow Lite 和 TensorFlow 操作符（operator）兼容性

TensorFlow Lite 支持许多常见推理模型中 TensorFlow 的运算操作（operations）。这些支持的运算操作在被映射至 TensorFlow Lite 对应操作符之前，会经过 TensorFlow Lite 的优化转换，可能会有省略或融合。

因为 TensorFlow Lite 的操作集比 TensorFlow 的要小，不是每个模型都可以被转换。考虑到性能的因素，甚至对于支持的操作，有时也需要用专门的使用模式。我们希望在未来的版本中扩充支持的操作集。以增加 binary size 为代价，可以引入更多的操作符，通过[使用选择的 TensorFlow 操作符](ops_select.md)。

想要理解如何搭建适用于 TensorFlow Lite 的 TensorFlow 模型的最好方法，就是仔细考虑操作运算是如何转换和优化的，以及在过程中引入的种种限制。

## 支持的类型

大部分 TensorFlow Lite 运算支持浮点数（float32）和量化（uint8, int8）推断。不过需到操作还不支持其他类型比如 tf.float16 和 strings。

浮点与量化模型除了使用不同版本的运算操作，转换方式也有不同。量化转换需要张量的动态范围信息。这需要在模型训练中使用“假量化”（fake-quantization），通过校准数据集获得范围信息，或者进行 ”on-the-fly“ 范围估计，详见[量化](../performance/model_optimization.md)。

## 数据格式与广播

目前 TensorFlow Lite 仅支持 TensorFlow 的“NHWC”格式，仅有有限的操作符（tf.add, tf.mul, tf.sub, and tf.div）支持广播。

## 兼容操作运算

下列 TensorFlow 操作运算通常映射至对应的 TensorFlow Lite 运算：

*   [tf.batch_to_space_nd](https://www.tensorflow.google.cn/api_docs/python/tf/batch_to_space_nd) -
    *当输入张量是 4D(1 batch + 2 spatial + 1 other) 并且未使用裁剪时*
*   [tf.exp](https://www.tensorflow.google.cn/api_docs/python/tf/exp)
*   [tf.fake_quant*](https://www.tensorflow.google.cn/api_docs/python/tf/fake_quant_with_min_max_args)
*   [tf.matmul](https://www.tensorflow.google.cn/api_docs/python/tf/matmul) - *当第二个参数是常量并且未使用转置时*
*   [tf.nn.avg_pool](https://www.tensorflow.google.cn/api_docs/python/tf/nn/avg_pool)
*   [tf.nn.conv2d](https://www.tensorflow.google.cn/api_docs/python/tf/nn/conv2d) -
    *当 filter 是常量时*
*   [tf.nn.depthwise_conv2d](https://www.tensorflow.google.cn/api_docs/python/tf/nn/depthwise_conv2d) -
    *当 filter 是常量并且 rate 是[1,1]时*
*   [tf.nn.l2_normalize](https://www.tensorflow.google.cn/api_docs/python/tf/nn/l2_normalize) -
    *当对最后一个维度进行正则化时*
*   [tf.nn.local_response_normalization](https://www.tensorflow.google.cn/api_docs/python/tf/nn/local_response_normalization)
*   [tf.nn.log_softmax](https://www.tensorflow.google.cn/api_docs/python/tf/nn/log_softmax) -
    *当 axis 未被提供时*
*   [tf.nn.max_pool](https://www.tensorflow.google.cn/api_docs/python/tf/nn/max_pool)
*   [tf.nn.softmax](https://www.tensorflow.google.cn/api_docs/python/tf/nn/softmax) -
    *当张量是二维并且 axis 是最后一个维度时*
*   [tf.nn.top_k](https://www.tensorflow.google.cn/api_docs/python/tf/nn/top_k)
*   [tf.one_hot](https://www.tensorflow.google.cn/api_docs/python/tf/one_hot)
*   [tf.pad](https://www.tensorflow.google.cn/api_docs/python/tf/pad) - *当未使用mode以及constant_values时*
*   [tf.reduce_mean](https://www.tensorflow.google.cn/api_docs/python/tf/reduce_mean) -
    *当未使用 reduction_indices 属性时*
*   [tf.reshape](https://www.tensorflow.google.cn/api_docs/python/tf/reshape)
*   [tf.sigmoid](https://www.tensorflow.google.cn/api_docs/python/tf/sigmoid)
*   [tf.space_to_batch_nd](https://www.tensorflow.google.cn/api_docs/python/tf/space_to_batch_nd) -
    *当输入张量是 4D(1 batch + 2 spatial + 1 other) 时*
*   [tf.space_to_depth](https://www.tensorflow.google.cn/api_docs/python/tf/space_to_depth)
*   [tf.split](https://www.tensorflow.google.cn/api_docs/python/tf/split) - *当未提供 num 并且 num_or_size_split 包含作为 0 维张量分离的数量时*
*   [tf.squeeze](https://www.tensorflow.google.cn/api_docs/python/tf/squeeze) - *当未提供 axis 时*
*   [tf.squared_difference](https://www.tensorflow.google.cn/versions/master/api_docs/python/tf/squared_difference)
*   [tf.strided_slice](https://www.tensorflow.google.cn/api_docs/python/tf/strided_slice) -
    *当未使用 ellipsis_mask 以及 new_axis_mask 时*
*   [tf.transpose](https://www.tensorflow.google.cn/versions/master/api_docs/python/tf/transpose) -
    *当未使用共轭时*
	
## 直接转换，常量合并与融合

许多 TensorFlow 操作可以经 TensorFlow Lite 处理，尽管它们没有直接的等价操作。这种情况出现在，运算操作可以直接从 graph 中去除（tf.identity），被张量替换（tf.placeholder），或融入更复杂的运算操作（tf.nn.bias_add）时。一些 TensorFlow Lite 支持的操作，在这一过程中也可能被去除。

下列是通常从graph中去除的TensorFlow运算操作列表：

*   [tf.add](https://www.tensorflow.google.cn/api_docs/python/tf/add)
*   [tf.check_numerics](https://www.tensorflow.google.cn/api_docs/python/tf/check_numerics)
*   [tf.constant](https://www.tensorflow.google.cn/api_docs/python/tf/constant)
*   [tf.div](https://www.tensorflow.google.cn/api_docs/python/tf/div)
*   [tf.divide](https://www.tensorflow.google.cn/api_docs/python/tf/divide)
*   [tf.fake_quant_with_min_max_args](https://www.tensorflow.google.cn/api_docs/python/tf/fake_quant_with_min_max_args)
*   [tf.fake_quant_with_min_max_vars](https://www.tensorflow.google.cn/api_docs/python/tf/fake_quant_with_min_max_vars)
*   [tf.identity](https://www.tensorflow.google.cn/api_docs/python/tf/identity)
*   [tf.maximum](https://www.tensorflow.google.cn/api_docs/python/tf/maximum)
*   [tf.minimum](https://www.tensorflow.google.cn/api_docs/python/tf/minimum)
*   [tf.multiply](https://www.tensorflow.google.cn/api_docs/python/tf/multiply)
*   [tf.no_op](https://www.tensorflow.google.cn/api_docs/python/tf/no_op)
*   [tf.placeholder](https://www.tensorflow.google.cn/api_docs/python/tf/placeholder)
*   [tf.placeholder_with_default](https://www.tensorflow.google.cn/api_docs/python/tf/placeholder_with_default)
*   [tf.realdiv](https://www.tensorflow.google.cn/api_docs/python/tf/realdiv)
*   [tf.reduce_max](https://www.tensorflow.google.cn/api_docs/python/tf/reduce_max)
*   [tf.reduce_min](https://www.tensorflow.google.cn/api_docs/python/tf/reduce_min)
*   [tf.reduce_sum](https://www.tensorflow.google.cn/api_docs/python/tf/reduce_sum)
*   [tf.rsqrt](https://www.tensorflow.google.cn/api_docs/python/tf/rsqrt)
*   [tf.shape](https://www.tensorflow.google.cn/api_docs/python/tf/shape)
*   [tf.sqrt](https://www.tensorflow.google.cn/api_docs/python/tf/sqrt)
*   [tf.square](https://www.tensorflow.google.cn/api_docs/python/tf/square)
*   [tf.subtract](https://www.tensorflow.google.cn/api_docs/python/tf/subtract)
*   [tf.tile](https://www.tensorflow.google.cn/api_docs/python/tf/tile)
*   [tf.nn.batch_norm_with_global_normalization](https://www.tensorflow.google.cn/api_docs/python/tf/nn/batch_norm_with_global_normalization)
*   [tf.nn.bias_add](https://www.tensorflow.google.cn/api_docs/python/tf/nn/bias_add)
*   [tf.nn.fused_batch_norm](https://www.tensorflow.google.cn/api_docs/python/tf/nn/fused_batch_norm)
*   [tf.nn.relu](https://www.tensorflow.google.cn/api_docs/python/tf/nn/relu)
*   [tf.nn.relu6](https://www.tensorflow.google.cn/api_docs/python/tf/nn/relu6)

请注意，这之中很多运算操作，在 TensorFlow Lite 中没有等价操作，如果它们不能被去除或融合，相应的模型将无法被转换。

## 不支持的运算操作

之前未被列出的 TensorFlow 运算操作大概率是不支持的。需要注意的是，下列的常见操作符目前是不被支持的：
*   [tf.depth_to_space](https://www.tensorflow.google.cn/api_docs/python/tf/depth_to_space)

## TensorFlow Lite 运算操作

下列 TensorFlow Lite 是完全支持的，用来替换之前列出的 TensorFlow 运算操作：
**ABS**

```
Inputs {
  0: 一个 tensor（张量）
}
Outputs {
  0: 输入张量逐元素取绝对值（elementwise abs of the input）
}
```

**ADD**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: 输入张量逐元素求和（elementwise sum of the input tensors）
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
}
```

**ADD_N**

```
Inputs {
  0-N: 任意数量的张量，需要同样的 size 与 shape
}
Outputs {
  0: 输入张量逐元素求和（elementwise sum of the input tensors）
}
```

**ARG_MAX**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: 包含最大值索引的张量（a tensor of indices of maximum values）
}
```

**ARG_MIN**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: 包含最小值索引的张量（a tensor of indices of minimum values）
}
```

**AVERAGE_POOL_2D**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 每个值是对应输入窗中值的张量
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
  padding: SAME|VALID
  stride_w,stride_h: 滑动窗的步长（stride）
  filter_width,filter_height: 滑动窗的尺寸（size）
}
```

**BATCH_TO_SPACE_ND**

```
Inputs {
  0: 4D 张量
  1: 1D 张量
  2: 2D 张量
}
Outputs {
  0: 使用 block_shape 重排后的张量，具体细节参考 tf.batch_to_space_nd
}
```

**CONCATENATION**

```
Inputs {
  0-N: 任意数量张量
}
Outputs {
  0: 输入张量沿指定 axis 的连接
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
  axis: 指定连接的 axis
}
```

**CONV_2D**

```
Inputs {
  0: 4D 张量
  1: filter
  2: bias （可选）
}
Outputs {
  0: 输入张量的二维卷积
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
  padding: SAME|VALID
  stride_w,stride_h: filter 窗的步长
}
```

**TRANSPOSE_CONV**

```
Inputs {
  0: 输出 shape
  1: filter
  2: 4D 张量
}
Outputs {
  0: conv2d 的转置（gradient）
}
Options {
  padding: SAME|VALID
  stride_w,stride_h: filter 窗的步长
}
```

**DEPTHWISE_CONV_2D**

```
Inputs {
  0: 4D 张量
  1: filter
  2: bias （可选）
}
Outputs {
  0: 输入张量的 depthwise-2D 卷积
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
  padding: SAME|VALID
  stride_w,stride_h: filter 窗的步长
  depth_multiplier: 输入与输出张量最后一个维度的关系
}
```

**ELU**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 张量等于 exp(features) - 1 若 < 0, 否则等于 features.
}
```

**EQUAL**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: bool型张量，当第一个张量中任意元素等于第二个张量中对应的元素时，为真
}
```

**EXP**

```
Inputs {
  0: 张量
}
Outputs {
  0: 输入张量逐元素计算指数的结果
}
```

**FILL**

```
Inputs {
  0: 一个 1D 张量
  1: 一个 0D (scalar) 张量
}
Outputs {
  0: 使用张量 1 的值填充 shape 等于张量 0 的张量
}
```

**FLOOR**

```
inputs {
  0: tensor
}
outputs: {
  0: 逐元素计算输入张量的floor
}
```

**FLOOR_DIV**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: 逐元素计算`tensor 0`除以`tensor 1`的 floor 的结果
}
```

**FLOOR_MOD**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: 逐元素计算`tensor 0`对`tensor 1`取余的 floor 的结果
}
```

**CEIL**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 逐元素计算输入张量 cell 的结果
}
```

**FULLY_CONNECTED**

```
Inputs {
  0: 4D 张量
  1: filter
  2: bias （可选）
}
Outputs {
  0: 全连接层的输出
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
}
```

**GATHER**

```
Inputs {
  0: params 张量
  1: indices 张量
  2: axis 张量（可选）
}
Outputs {
  0: 与 params 张量有相同尺寸的张量
}
```

**GATHER_ND**

```
Inputs {
  0: params 张量
  1: indices 张量
}
Outputs {
  0: 与 params 张量有相同尺寸的张量
}
```

**GREATER**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: bool 型张量，当第一个张量中任意元素大于第二个张量中对应的元素，为真
}
```

**GREATER_EQUAL**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: bool 型张量，当第一个张量中任意元素大于等于第二个张量中对应的元素，为真
}
```

**L2_NORMALIZATION**

```
Inputs {
  0: 输入张量
}
Outputs {
  0: 正则化（normalized）张量（沿最后的维度）
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
}
```

**L2_POOL_2D**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 tf.sqrt(tf.nn.ave_pool(tf.square(input))
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
  padding: SAME|VALID
  stride_w,stride_h: 滑动窗的 stride
  filter_width,filter_height: 滑动窗的 size
}
```

**LEAKY_RELU**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 max(input, input * alpha)
}
Options {
  alpha: 当 x < 0时，激活的坡度（提供的alpha <= 1）
}
```

**LESS**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: bool 型张量，当第一个张量中任意元素小于第二个张量中对应的元素，为真
}
```

**LESS_EQUAL**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: bool 型张量，当第一个张量中任意元素小于等于第二个张量中对应的元素，为真
}
```

**LOCAL_RESPONSE_NORMALIZATION**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 tf.nn.local_response_normalization
}
Options {
  radius
  bias
  alpha
  beta
}
```

**LOGICAL_OR**

```
Inputs {
  0: 张量的list
  1: 张量的list
}
Outputs {
  0: 输入张量的 logical_or
}
```

**LOGISTIC**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 1 / (1 + exp(-input))
}
```

**LOG**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 log(input)
}
```

**LOG_SOFTMAX**

```
Inputs {
  0: 张量
}
Outputs {
  0: 张量，等效于 logits - log(reduce_sum(exp(logits), -1))
}
```

**MAX_POOL_2D**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 每个值是对应输入窗最大值的张量
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
  padding: SAME|VALID
  stride_w,stride_h: 滑动窗的 stride
  filter_width,filter_height: 滑动窗的 size
}
```

**MUL**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: 输入张量逐元素相乘
}
Options {
  fused_activation_function:  NONE|RELU|RELU6
}
```

**NEG**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 输入张量逐元素取负
}
```

**PACK**

```
Inputs {
  0: 张量的list
  1: 一个整型数
}
Outputs {
  0: 包含堆栈张量的张量
}
```

**PAD**

```
Inputs {
  0: 张量
  1: 张量
}
Outputs {
  0: padding 后的张量
}
```

**MEAN (tf.reduce_mean)**

```
Inputs {
  0: 张量
  1: 张量
}
Outputs {
  0: 包含张量中值的张量
}
Options {
  keep_dims: 是否保留减小的维度
}
```

**NOT_EQUAL**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: bool 型张量，当第一个张量中任意元素不等于第二个张量中对应的元素时，为真
}
```

**POW**

```
Inputs {
  0: 一个张量
  1: 一个张量
}
Outputs {
  0: 逐元素取幂指数
}
```

**RANGE**

```
Inputs {
  0: 一个 0D (scalar) 张量
  1: 一个 0D (scalar) 张量
  2: 一个 0D (scalar) 张量
}
Outputs {
  0: 一个 1D 张量，类型为`dtype`，`张量 0` 是其开始，`张量 1`是其界限，`张量 2`是delta
}
Options {
  dtype
}
```

**RANK**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 一个 0D，int32 类型的张量，表示输入张量的秩
}
```

**RELU**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 max(0, input)
}
```

**RELU_N1_TO_1**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 max(-1, min(input, 1)
}
```

**RELU6**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 max(0, min(input, 6)
}
```

**RESHAPE**

```
Inputs {
  0: 一个张量
  1: 忽略
}
Outputs {
  0: 与输入张量值相等，但是 shape 改变的张量
}
Options {
  new_shape
}
```

**RESIZE_BILINEAR**

```
Inputs {
  0: 一个 4D 张量
  1: 一个 1D 张量，包含两个元素
}
Outputs {
  0: 通过双线性插值，将`张量 0`根据`张量 1`的 height/width 值进行 resize
}
Options {
  align_corners
}
```

**RESIZE_NEAREST_NEIGHBOR**

```
Inputs {
  0: 一个 4D 张量
  1: 一个 1D 张量，包含两个元素
}
Outputs {
  0: 通过最近邻插值，将`张量 0`根据`张量 1`的 height/width 值进行 resize
}
Options {
  align_corners
}
```

**RSQRT**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 逐元素计算反平方根倒数
}
```

**REVERSE_SEQUENCE**

```
Inputs {
  0: 一个张量
  1: 一个 1-D 张量 指定了各 sequence 的长度
  dim
}
Outputs {
  0: 与输入张量有相同 shape 的张量
}
Options {
  seq_dim: 一个 0-D int 张量（scalar），维度部分保留
  batch_dim: 一个 0-D int 张量（scalar），默认为0，取逆时所沿维度
}
```

**SHAPE**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 一个 1D 张量，代表了输入张量的 shape
}
Options {
  out_type: 操作符的输出类型（int32 or int64），默认是 int32.
}
```

**ROUND**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 逐元素 round
}
```

**SLICE**

```
Inputs {
  0: 张量
  1: 1D 张量
  2: 1D 张量
}
Outputs {
  0: 根据给定 size 对输入张量切片
}
```

**SOFTMAX**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 等效于 exp(input) / tf.reduce_sum(exp(input * beta), dim)，其中 dim 是最后一个维度大小
}
Options {
  beta
}
```

**SPACE_TO_DEPTH**

```
Inputs {
  0: 一个 4D 张量
}
Outputs {
  0:使用 block_size 重排的张量，详见 tf.space_to_depth
}
Options {
  block_size
}
```

**SPACE_TO_BATCH_ND**

```
Inputs {
  0: 4D 张量
  1: 1D 张量
  2: 2D 张量
}
Outputs {
  0: 使用 block_shape 重排的张量，详见 tf.space_to_batch_nd
}
```

**SPARSE_TO_DENSE**

```
Inputs {
  0: 0D 或 1D 或 2D 张量
  1: 1D 张量
  2: 0D 或 1D 张量
  3: 0D 张量
  4: 一个布尔值
}
Outputs {
  0: Dense 张量，shape 等于 output_shape，与 sparse_values 有相同类型
}
```

**SPLIT**

```
Inputs {
  0: 0D 张量 (axis)
  1: 张量 (input)
}
Outputs {
  0-N: 根据输入张量构造的子张量
}
Options {
  num_splits: 指定输出的数量
}
```

**SPLIT_V**

```
Inputs {
  0: 张量 (input)
  1: 1-D 张量 (size_splits)
  2: 0-D 张量 (axis)
}
Outputs {
  0-N: 根据输入张量构造的子张量
}
Options {
  num_splits: 指定输出的数量
}
```

**SQRT**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 逐元素计算平方根
}
```

**SQUEEZE**

```
Inputs {
  0: 张量
}
Outputs {
  0: 没有 size 等于 1 的维度的张量
}
Options {
  squeeze_dims
}
```

**STRIDED_SLICE**

```
Inputs {
  0: 张量
  1: 1D 张量
  2: 1D 张量
  3: 1D 张量
}
Outputs {
  0: 输入张量的切片
}
Options {
  begin_mask: 起始索引的mask
  end_mask: 最终索引的mask
  shrink_axis_mask: 指明去除维度的mask
}
```

**TANH**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 逐元素计算 tanh
}
```

**TOP_K**

```
Inputs {
  0: 张量
  1: OD 张量
}
Outputs {
  0: k 个沿最大维度切片的最大值
  1: 输入张量最大维度中值的索引
}
```

**TRANSPOSE**

```
Inputs {
  0: 张量
  1: 张量
}
Outputs {
  0: 转置张量
}
```

**SELECT**

```
Inputs {
  0: 张量
  1: 张量
  2: 张量
}
Outputs {
  0: 张量，若'张量 1'中对应元素为 true，其对应值为'张量 0'中对应元素，若为 false，其对应值为'张量 2'中对应元素
}
```

**UNPACK**

```
Inputs {
  0: 一个张量.
  1: 一个 integer.
  2: 一个 integer.
}
Outputs {
  0-N: 包含 unpacked 张量的张量
}
```

**WHERE**

```
Inputs {
  0: bool 型张量
  1: 与条件有相同 shape 的张量，如果条件秩为 1，x 的秩可以更大，不过其第一个维度必须与条件的 size 一致
  2: 与 x 有相同 shape 与类型的张量
}
Outputs {
  0: 若 x, y 不为 None, 张量与 x，y 有相同 shape 与类型，否则其 shape等于(num_true, dim_size(condition))。
}
```

**ZEROS_LIKE**

```
Inputs {
  0: 一个张量
}
Outputs {
  0: 与 x 类型与 type 一致，使用 0 填充
}
```

**FILL**

```
Inputs {
  0: 一个张量。必须是下列类型: int32, int64. 1-D. 代表了输出张量的 shape。
  1: 一个张量。0-D (scalar). 用于填充返回张量的值
}
Outputs {
  0: 张量类型与（input1）值类型一样.
}
```
这些 TensorFlow Lite 运算操作还未能在自定义模型中使用：

*   CALL
*   CONCAT_EMBEDDINGS
*   CUSTOM
*   EMBEDDING_LOOKUP
*   EMBEDDING_LOOKUP_SPARSE
*   HASHTABLE_LOOKUP
*   LSH_PROJECTION
*   LSTM
*   RNN
*   SKIP_GRAM
*   SVDF
