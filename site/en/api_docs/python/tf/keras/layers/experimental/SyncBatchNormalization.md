description: Normalize and scale inputs or activations synchronously across replicas.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.SyncBatchNormalization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.experimental.SyncBatchNormalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/normalization_v2.py#L32-L204">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Normalize and scale inputs or activations synchronously across replicas.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.SyncBatchNormalization(
    axis=-1, momentum=0.99, epsilon=0.001, center=(True), scale=(True),
    beta_initializer='zeros', gamma_initializer='ones',
    moving_mean_initializer='zeros', moving_variance_initializer='ones',
    beta_regularizer=None, gamma_regularizer=None, beta_constraint=None,
    gamma_constraint=None, renorm=(False), renorm_clipping=None,
    renorm_momentum=0.99, trainable=(True), adjustment=None, name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Applies batch normalization to activations of the previous layer at each batch
by synchronizing the global batch statistics across all devices that are
training the model. For specific details about batch normalization please
refer to the <a href="../../../../tf/keras/layers/BatchNormalization.md"><code>tf.keras.layers.BatchNormalization</code></a> layer docs.

If this layer is used when using tf.distribute strategy to train models
across devices/workers, there will be an allreduce call to aggregate batch
statistics across all replicas at every training step. Without tf.distribute
strategy, this layer behaves as a regular <a href="../../../../tf/keras/layers/BatchNormalization.md"><code>tf.keras.layers.BatchNormalization</code></a>
layer.

#### Example usage:


```
strategy = tf.distribute.MirroredStrategy()

with strategy.scope():
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(16))
  model.add(tf.keras.layers.experimental.SyncBatchNormalization())
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`axis`
</td>
<td>
Integer, the axis that should be normalized
(typically the features axis).
For instance, after a `Conv2D` layer with
`data_format="channels_first"`,
set `axis=1` in `BatchNormalization`.
</td>
</tr><tr>
<td>
`momentum`
</td>
<td>
Momentum for the moving average.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
Small float added to variance to avoid dividing by zero.
</td>
</tr><tr>
<td>
`center`
</td>
<td>
If True, add offset of `beta` to normalized tensor.
If False, `beta` is ignored.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
If True, multiply by `gamma`.
If False, `gamma` is not used.
When the next layer is linear (also e.g. <a href="../../../../tf/nn/relu.md"><code>nn.relu</code></a>),
this can be disabled since the scaling
will be done by the next layer.
</td>
</tr><tr>
<td>
`beta_initializer`
</td>
<td>
Initializer for the beta weight.
</td>
</tr><tr>
<td>
`gamma_initializer`
</td>
<td>
Initializer for the gamma weight.
</td>
</tr><tr>
<td>
`moving_mean_initializer`
</td>
<td>
Initializer for the moving mean.
</td>
</tr><tr>
<td>
`moving_variance_initializer`
</td>
<td>
Initializer for the moving variance.
</td>
</tr><tr>
<td>
`beta_regularizer`
</td>
<td>
Optional regularizer for the beta weight.
</td>
</tr><tr>
<td>
`gamma_regularizer`
</td>
<td>
Optional regularizer for the gamma weight.
</td>
</tr><tr>
<td>
`beta_constraint`
</td>
<td>
Optional constraint for the beta weight.
</td>
</tr><tr>
<td>
`gamma_constraint`
</td>
<td>
Optional constraint for the gamma weight.
</td>
</tr><tr>
<td>
`renorm`
</td>
<td>
Whether to use Batch Renormalization
(https://arxiv.org/abs/1702.03275). This adds extra variables during
training. The inference is the same for either value of this parameter.
</td>
</tr><tr>
<td>
`renorm_clipping`
</td>
<td>
A dictionary that may map keys 'rmax', 'rmin', 'dmax' to
scalar `Tensors` used to clip the renorm correction. The correction
`(r, d)` is used as `corrected_value = normalized_value * r + d`, with
`r` clipped to [rmin, rmax], and `d` to [-dmax, dmax]. Missing rmax, rmin,
dmax are set to inf, 0, inf, respectively.
</td>
</tr><tr>
<td>
`renorm_momentum`
</td>
<td>
Momentum used to update the moving means and standard
deviations with renorm. Unlike `momentum`, this affects training
and should be neither too small (which would add noise) nor too large
(which would give stale estimates). Note that `momentum` is still applied
to get the means and variances for inference.
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, if `True` the variables will be marked as trainable.
</td>
</tr>
</table>



#### Call arguments:


* <b>`inputs`</b>: Input tensor (of any rank).
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode.
  - `training=True`: The layer will normalize its inputs using the
    mean and variance of the current batch of inputs.
  - `training=False`: The layer will normalize its inputs using the
    mean and variance of its moving statistics, learned during training.


#### Input shape:

Arbitrary. Use the keyword argument `input_shape`
(tuple of integers, does not include the samples axis)
when using this layer as the first layer in a model.



#### Output shape:

Same shape as input.


