description: Enable mixed precision via a graph rewrite.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.experimental.enable_mixed_precision_graph_rewrite" />
<meta itemprop="path" content="Stable" />
</div>

# tf.train.experimental.enable_mixed_precision_graph_rewrite

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/experimental/mixed_precision.py#L64-L206">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enable mixed precision via a graph rewrite.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.train.experimental.enable_mixed_precision_graph_rewrite(
    opt, loss_scale='dynamic'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Mixed precision is the use of both float32 and float16 data types when
training a model to improve performance. This is achieved via a graph rewrite
operation and a loss-scale optimizer.

Performing arithmetic operations in float16 takes advantage of specialized
processing units, such as NVIDIA Tensor Cores, for much higher arithmetic
throughput. However, due to the smaller representable range, performing the
entire training with float16 can result in gradient underflow, that is, small
gradient values becoming zeroes. Instead, performing only select arithmetic
operations in float16 results in higher throughput and decreased training
time when using compatible hardware accelerators while also reducing memory
usage, typically without sacrificing model accuracy.

Note: While the mixed precision rewrite changes the datatype of various
layers throughout the model, the same accuracy reached in float32 is
expected. If a `NaN` gradient occurs with dynamic loss scaling, the model
update for that batch is skipped. In this case, the global step count is not
incremented, and the `LossScaleOptimizer` attempts to decrease the loss
scaling value to avoid `NaN` values in subsequent iterations. This approach
has been shown to achieve the same accuracy as float32 and, in most cases,
better training throughput.

#### Example:



```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='softmax'),
])

opt = tf.keras.optimizers.SGD()
opt = tf.train.experimental.enable_mixed_precision_graph_rewrite(opt)
model.compile(loss="mse", optimizer=opt)

x_train = np.random.random((1024, 64))
y_train = np.random.random((1024, 64))
model.fit(x_train, y_train)
```

Calling `enable_mixed_precision_graph_rewrite(opt)` enables the graph rewrite
operation before computing gradients. The function additionally returns an
`Optimizer` (`opt`) wrapped with a `LossScaleOptimizer`. This prevents
underflow in the float16 tensors during the backward pass. An optimizer of
type <a href="../../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a> or <a href="../../../tf/compat/v1/train/Optimizer.md"><code>tf.compat.v1.train.Optimizer</code></a> must be
passed to this function, which will then be wrapped to use loss scaling.

The graph rewrite operation changes the dtype of certain operations in the
graph from float32 to float16. There are several categories of operations
that are either included or excluded by this rewrite operation. The following
categories of Ops are defined inside corresponding functions under the class
`AutoMixedPrecisionLists` in
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/
core/grappler/optimizers/auto_mixed_precision_lists.h">
auto_mixed_precision_lists.h</a>:

* `ClearList`: Ops that do not have numerically significant adverse effects.
E.g. `ArgMax` and `Floor`.
* `WhiteList`: Ops that are considered numerically safe for execution in
float16, and thus are always converted. E.g. `Conv2D`.
* `BlackList`: Ops that are numerically unsafe to execute in float16 and
can negatively affect downstream nodes. E.g. `Softmax`.
* `GrayList`: Ops that are considered numerically safe for execution in
float16 unless downstream from a BlackList Op. E.g. `Add` and `AvgPool`.

When this function is used, gradients should be computed and applied with the
returned optimizer, either by calling `opt.minimize()` or
`opt.compute_gradients()` followed by `opt.apply_gradients()`. If gradients
are instead computed with <a href="../../../tf/gradients.md"><code>tf.gradients</code></a> or <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>, loss scaling
will not be applied, which will likely cause your model not to converge due to
float16 underflow problems. To apply lossing scaling with <a href="../../../tf/gradients.md"><code>tf.gradients</code></a> or
<a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>, <a href="../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#get_scaled_loss"><code>LossScaleOptimizer.get_scaled_loss</code></a> and
<a href="../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md#get_unscaled_gradients"><code>LossScaleOptimizer.get_unscaled_gradients</code></a>. See
<a href="../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md"><code>keras.mixed_precision.experimental.LossScaleOptimizer</code></a> for details how to do
this.

When eager execution is enabled, the mixed precision graph rewrite is only
enabled within <a href="../../../tf/function.md"><code>tf.function</code></a>s, as outside <a href="../../../tf/function.md"><code>tf.function</code></a>s, there is no graph.

For NVIDIA GPUs with Tensor cores, as a general performance guide, dimensions
(such as batch size, input size, output size, and channel counts)
should be powers of two if under 256, or  otherwise divisible by 8 if above
256. For more information, check out the
[NVIDIA Deep Learning Performance Guide](
https://docs.nvidia.com/deeplearning/sdk/dl-performance-guide/index.html).

Currently, mixed precision is only enabled on NVIDIA Tensor Core GPUs with
Compute Capability 7.0 and above (Volta, Turing, or newer architectures). The
parts of the graph on CPUs and TPUs are untouched by the graph rewrite.

## Comparison with the Keras mixed precision  API
Both this function and the [Keras mixed precision
API](https://www.tensorflow.org/guide/keras/mixed_precision) enable the use of
mixed precision in a model. Therefore, only one of the two APIs can be used.
We recommend using the Keras mixed precision API, as it is more customizable
and supports Eager execution. However, it only supports models which use Keras
layers, while the graph rewrite works in any model that uses <a href="../../../tf/function.md"><code>tf.function</code></a>s.

The core difference between the two APIs is that this function is a graph
rewrite, and so it changes the graph to use mixed precision under the hood.
You still build your graph in float32, and the graph rewrite will change
certain ops to float16. The Keras mixed precision API directly builds the
Keras Model using a mix of float16 and float32.

One core advantage of the Keras API is it supports mixed precision with Eager
execution, i.e. mixed precision outside <a href="../../../tf/function.md"><code>tf.function</code></a>s. The graph rewrite will
only affect ops within <a href="../../../tf/function.md"><code>tf.function</code></a>s, making it harder to debug if issues
occur with mixed precision. The Keras API is also more customizable, as you
can override any layer to run in float32 by passing `dtype="float32"` to the
layer constructor. Additionally, you can query the dtype of tensors in the
model by checking `tensor.dtype`. With the graph rewrite, all tensors appear
to be float32 since the dtype is only changed under the hood.

The main advantage of the graph rewrite (this function) is that it works even
if you do not use Keras layers or any other part of Keras. The Keras mixed
precision API requires models which use Keras layers, as it only inserts casts
inside Keras layers and models. Another advantage is that the graph rewrite
never results in a TypeError, which the Keras API may introduce if you do
certain operations outside Keras. For example, the following will result in a
TypeError if the Keras mixed precision API is enabled, as a float16 and
float32 tensor will be added:
`tf.keras.layers.Dense(2)(x) + tf.keras.layers.Dense(2, dtype="float32")(x)`

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
`ValueError`, if the <a href="../../../tf/keras/mixed_precision.md"><code>tf.keras.mixed_precision</code></a> API is also used by calling
<a href="../../../tf/keras/mixed_precision/experimental/set_policy.md"><code>tf.keras.mixed_precision.experimental.set_policy</code></a>. Only one mixed precision
API can be used.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`opt`
</td>
<td>
An instance of a <a href="../../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a>.
</td>
</tr><tr>
<td>
`loss_scale`
</td>
<td>
Either an int/float, the string `"dynamic"`, or an instance of a
<a href="../../../tf/mixed_precision/experimental/LossScale.md"><code>tf.mixed_precision.experimental.LossScale</code></a>. The loss scale to use. It is
recommended to keep this as its default value of `"dynamic"`, which will
adjust the scaling automatically to prevent `Inf` or `NaN` values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A version of `opt` that will use loss scaling to prevent underflow.
</td>
</tr>

</table>

