page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.experimental.enable_mixed_precision_graph_rewrite


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/experimental/mixed_precision.py#L122-L162">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Enable mixed precision via a graph rewrite.

``` python
tf.compat.v1.train.experimental.enable_mixed_precision_graph_rewrite(
    opt,
    loss_scale='dynamic'
)
```



<!-- Placeholder for "Used in" -->

Mixed precision is the use of both float16 and float32 when training a model,
and is used to make the model run faster. This function will use mixed
precision to speed up the execution time of your model when run on a GPU. It
does this by changing the dtype of certain operations in the graph from
float32 to float16.

This function additionally wraps an Optimizer with a LossScaleOptimizer, which
is required to prevent underflow in the float16 tensors during the backwards
pass. An optimizer must be passed to this function, which will then be wrapped
to use loss scaling.

When this function is used, gradients should only be computed and applied with
the returned optimizer, either by calling `opt.minimize()` or
`opt.compute_gradients()` followed by `opt.apply_gradients()`. Gradients
should not be computed with <a href="../../../../../tf/gradients"><code>tf.gradients</code></a> or <a href="../../../../../tf/GradientTape"><code>tf.GradientTape</code></a>. This is
because the returned optimizer will apply loss scaling, and
<a href="../../../../../tf/gradients"><code>tf.gradients</code></a>/<a href="../../../../../tf/GradientTape"><code>tf.GradientTape</code></a> will not. If you do directly use
<a href="../../../../../tf/gradients"><code>tf.gradients</code></a> or <a href="../../../../../tf/GradientTape"><code>tf.GradientTape</code></a>, your model may train to a worse quality.

Currently, mixed precision is only enabled on Volta GPUs and above. TPU
support is coming soon. CPUs are not supported, as CPUs do not run float16
operations faster than float32 operations.

#### Args:


* <b>`opt`</b>: An instance of a <a href="../../../../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a> or a
  `tf.train.Optimizer`.
* <b>`loss_scale`</b>: Either an int/float, the string "dynamic", or an instance of a
  <a href="../../../../../tf/train/experimental/LossScale"><code>tf.train.experimental.LossScale</code></a>. The loss scale to use. It is
  recommended to keep this as its default value of "dynamic".


#### Returns:

A version of `opt` that will use loss scaling to prevent underflow.
