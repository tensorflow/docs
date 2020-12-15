description: Optimization parameters for Adam with TPU embeddings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.experimental.AdamParameters" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.compat.v1.tpu.experimental.AdamParameters

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/tpu_embedding.py#L524-L610">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimization parameters for Adam with TPU embeddings.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.experimental.AdamParameters(
    learning_rate: float,
    beta1: float = 0.9,
    beta2: float = 0.999,
    epsilon: float = 1e-08,
    lazy_adam: bool = (True),
    sum_inside_sqrt: bool = (True),
    use_gradient_accumulation: bool = (True),
    clip_weight_min: Optional[float] = None,
    clip_weight_max: Optional[float] = None,
    weight_decay_factor: Optional[float] = None,
    multiply_weight_decay_factor_by_learning_rate: Optional[bool] = None,
    clip_gradient_min: Optional[float] = None,
    clip_gradient_max: Optional[float] = None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Pass this to `tf.estimator.tpu.experimental.EmbeddingConfigSpec` via the
`optimization_parameters` argument to set the optimizer and its parameters.
See the documentation for `tf.estimator.tpu.experimental.EmbeddingConfigSpec`
for more details.

```
estimator = tf.estimator.tpu.TPUEstimator(
    ...
    embedding_config_spec=tf.estimator.tpu.experimental.EmbeddingConfigSpec(
        ...
        optimization_parameters=tf.tpu.experimental.AdamParameters(0.1),
        ...))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`
</td>
<td>
a floating point value. The learning rate.
</td>
</tr><tr>
<td>
`beta1`
</td>
<td>
A float value.
The exponential decay rate for the 1st moment estimates.
</td>
</tr><tr>
<td>
`beta2`
</td>
<td>
A float value.
The exponential decay rate for the 2nd moment estimates.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A small constant for numerical stability.
</td>
</tr><tr>
<td>
`lazy_adam`
</td>
<td>
Use lazy Adam instead of Adam. Lazy Adam trains faster.
Please see `optimization_parameters.proto` for details.
</td>
</tr><tr>
<td>
`sum_inside_sqrt`
</td>
<td>
This improves training speed. Please see
`optimization_parameters.proto` for details.
</td>
</tr><tr>
<td>
`use_gradient_accumulation`
</td>
<td>
setting this to `False` makes embedding
gradients calculation less accurate but faster. Please see
`optimization_parameters.proto` for details.
for details.
</td>
</tr><tr>
<td>
`clip_weight_min`
</td>
<td>
the minimum value to clip by; None means -infinity.
</td>
</tr><tr>
<td>
`clip_weight_max`
</td>
<td>
the maximum value to clip by; None means +infinity.
</td>
</tr><tr>
<td>
`weight_decay_factor`
</td>
<td>
amount of weight decay to apply; None means that the
weights are not decayed.
</td>
</tr><tr>
<td>
`multiply_weight_decay_factor_by_learning_rate`
</td>
<td>
if true,
`weight_decay_factor` is multiplied by the current learning rate.
</td>
</tr><tr>
<td>
`clip_gradient_min`
</td>
<td>
the minimum value to clip by; None means -infinity.
</td>
</tr><tr>
<td>
`clip_gradient_max`
</td>
<td>
the maximum value to clip by; None means +infinity.
</td>
</tr>
</table>



