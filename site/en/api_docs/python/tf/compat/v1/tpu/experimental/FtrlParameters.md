description: Optimization parameters for Ftrl with TPU embeddings.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.experimental.FtrlParameters" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.compat.v1.tpu.experimental.FtrlParameters

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_embedding.py#L551-L630">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimization parameters for Ftrl with TPU embeddings.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.experimental.FtrlParameters(
    learning_rate, learning_rate_power=-0.5, initial_accumulator_value=0.1,
    l1_regularization_strength=0.0, l2_regularization_strength=0.0,
    use_gradient_accumulation=(True), clip_weight_min=None, clip_weight_max=None,
    weight_decay_factor=None, multiply_weight_decay_factor_by_learning_rate=None
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
        optimization_parameters=tf.tpu.experimental.FtrlParameters(0.1),
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
`learning_rate_power`
</td>
<td>
A float value, must be less or equal to zero.
Controls how the learning rate decreases during training. Use zero for
a fixed learning rate. See section 3.1 in the
[paper](https://www.eecs.tufts.edu/~dsculley/papers/ad-click-prediction.pdf).
</td>
</tr><tr>
<td>
`initial_accumulator_value`
</td>
<td>
The starting value for accumulators.
Only zero or positive values are allowed.
</td>
</tr><tr>
<td>
`l1_regularization_strength`
</td>
<td>
A float value, must be greater than or
equal to zero.
</td>
</tr><tr>
<td>
`l2_regularization_strength`
</td>
<td>
A float value, must be greater than or
equal to zero.
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
</tr>
</table>



