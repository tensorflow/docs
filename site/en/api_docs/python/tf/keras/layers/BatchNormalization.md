description: Layer that normalizes its inputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.BatchNormalization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.BatchNormalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/normalization_v2.py#L215-L254">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer that normalizes its inputs.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.BatchNormalization(
    axis=-1, momentum=0.99, epsilon=0.001, center=(True), scale=(True),
    beta_initializer='zeros', gamma_initializer='ones',
    moving_mean_initializer='zeros', moving_variance_initializer='ones',
    beta_regularizer=None, gamma_regularizer=None, beta_constraint=None,
    gamma_constraint=None, renorm=(False), renorm_clipping=None,
    renorm_momentum=0.99, fused=None, trainable=(True), virtual_batch_size=None,
    adjustment=None, name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Batch normalization applies a transformation that maintains the mean output
close to 0 and the output standard deviation close to 1.

Importantly, batch normalization works differently during training and
during inference.

**During training** (i.e. when using `fit()` or when calling the layer/model
with the argument `training=True`), the layer normalizes its output using
the mean and standard deviation of the current batch of inputs. That is to
say, for each channel being normalized, the layer returns
`(batch - mean(batch)) / (var(batch) + epsilon) * gamma + beta`, where:

- `epsilon` is small constant (configurable as part of the constructor
arguments)
- `gamma` is a learned scaling factor (initialized as 1), which
can be disabled by passing `scale=False` to the constructor.
- `beta` is a learned offset factor (initialized as 0), which
can be disabled by passing `center=False` to the constructor.

**During inference** (i.e. when using `evaluate()` or `predict()` or when
calling the layer/model with the argument `training=False` (which is the
default), the layer normalizes its output using a moving average of the
mean and standard deviation of the batches it has seen during training. That
is to say, it returns
`(batch - self.moving_mean) / (self.moving_var + epsilon) * gamma + beta`.

`self.moving_mean` and `self.moving_var` are non-trainable variables that
are updated each time the layer in called in training mode, as such:

- `moving_mean = moving_mean * momentum + mean(batch) * (1 - momentum)`
- `moving_var = moving_var * momentum + var(batch) * (1 - momentum)`

As such, the layer will only normalize its inputs during inference
*after having been trained on data that has similar statistics as the
inference data*.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`axis`
</td>
<td>
Integer or a list of integers, the axis that should be normalized
(typically the features axis). For instance, after a `Conv2D` layer with
`data_format="channels_first"`, set `axis=1` in `BatchNormalization`.
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
If True, add offset of `beta` to normalized tensor. If False, `beta`
is ignored.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
If True, multiply by `gamma`. If False, `gamma` is not used. When the
next layer is linear (also e.g. <a href="../../../tf/nn/relu.md"><code>nn.relu</code></a>), this can be disabled since the
scaling will be done by the next layer.
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
Whether to use [Batch Renormalization](
https://arxiv.org/abs/1702.03275). This adds extra variables during
training. The inference is the same for either value of this parameter.
</td>
</tr><tr>
<td>
`renorm_clipping`
</td>
<td>
A dictionary that may map keys 'rmax', 'rmin', 'dmax' to
scalar `Tensors` used to clip the renorm correction. The correction `(r,
d)` is used as `corrected_value = normalized_value * r + d`, with `r`
clipped to [rmin, rmax], and `d` to [-dmax, dmax]. Missing rmax, rmin,
dmax are set to inf, 0, inf, respectively.
</td>
</tr><tr>
<td>
`renorm_momentum`
</td>
<td>
Momentum used to update the moving means and standard
deviations with renorm. Unlike `momentum`, this affects training and
should be neither too small (which would add noise) nor too large (which
would give stale estimates). Note that `momentum` is still applied to get
the means and variances for inference.
</td>
</tr><tr>
<td>
`fused`
</td>
<td>
if `True`, use a faster, fused implementation, or raise a ValueError
if the fused implementation cannot be used. If `None`, use the faster
implementation if possible. If False, do not used the fused
implementation.
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, if `True` the variables will be marked as trainable.
</td>
</tr><tr>
<td>
`virtual_batch_size`
</td>
<td>
An `int`. By default, `virtual_batch_size` is `None`,
which means batch normalization is performed across the whole batch. When
`virtual_batch_size` is not `None`, instead perform "Ghost Batch
Normalization", which creates virtual sub-batches which are each
normalized separately (with shared gamma, beta, and moving statistics).
Must divide the actual batch size during execution.
</td>
</tr><tr>
<td>
`adjustment`
</td>
<td>
A function taking the `Tensor` containing the (dynamic) shape of
the input tensor and returning a pair (scale, bias) to apply to the
normalized values (before gamma and beta), only during training. For
example, if axis==-1,
`adjustment = lambda shape: (
tf.random.uniform(shape[-1:], 0.93, 1.07),
tf.random.uniform(shape[-1:], -0.1, 0.1))` will scale the normalized
value by up to 7% up or down, then shift the result by up to 0.1
(with independent scaling and bias for each feature but shared
across all examples), and finally apply gamma and/or beta. If
`None`, no adjustment is applied. Cannot be specified if
virtual_batch_size is specified.
</td>
</tr>
</table>



#### Call arguments:


* <b>`inputs`</b>: Input tensor (of any rank).
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode.
  - `training=True`: The layer will normalize its inputs using the mean and
    variance of the current batch of inputs.
  - `training=False`: The layer will normalize its inputs using the mean and
    variance of its moving statistics, learned during training.

Input shape: Arbitrary. Use the keyword argument `input_shape` (tuple of
  integers, does not include the samples axis) when using this layer as the
  first layer in a model.

Output shape: Same shape as input.  
**About setting `layer.trainable = False` on a `BatchNormalization` layer:**

The meaning of setting `layer.trainable = False` is to freeze the layer,
i.e. its internal state will not change during training:
its trainable weights will not be updated
during `fit()` or `train_on_batch()`, and its state updates will not be run.

Usually, this does not necessarily mean that the layer is run in inference
mode (which is normally controlled by the `training` argument that can
be passed when calling a layer). "Frozen state" and "inference mode"
are two separate concepts.

However, in the case of the `BatchNormalization` layer, **setting
`trainable = False` on the layer means that the layer will be
subsequently run in inference mode** (meaning that it will use
the moving mean and the moving variance to normalize the current batch,
rather than using the mean and variance of the current batch).

This behavior has been introduced in TensorFlow 2.0, in order
to enable `layer.trainable = False` to produce the most commonly
expected behavior in the convnet fine-tuning use case.

#### Note that:

- This behavior only occurs as of TensorFlow 2.0. In 1.*,
  setting `layer.trainable = False` would freeze the layer but would
  not switch it to inference mode.
- Setting `trainable` on an model containing other layers will
  recursively set the `trainable` value of all inner layers.
- If the value of the `trainable`
  attribute is changed after calling `compile()` on a model,
  the new value doesn't take effect for this model
  until `compile()` is called again.




#### Reference:

- [Ioffe and Szegedy, 2015](https://arxiv.org/abs/1502.03167).


