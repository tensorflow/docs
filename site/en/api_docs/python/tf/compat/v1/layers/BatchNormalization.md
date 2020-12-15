description: Batch Normalization layer from (Ioffe et al., 2015).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.layers.BatchNormalization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.compat.v1.layers.BatchNormalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/legacy_tf_layers/normalization.py#L31-L172">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Batch Normalization layer from (Ioffe et al., 2015).

Inherits From: [`BatchNormalization`](../../../../tf/compat/v1/keras/layers/BatchNormalization.md), [`Layer`](../../../../tf/compat/v1/layers/Layer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.layers.BatchNormalization(
    axis=-1, momentum=0.99, epsilon=0.001, center=(True), scale=(True),
    beta_initializer=tf.zeros_initializer(),
    gamma_initializer=tf.ones_initializer(),
    moving_mean_initializer=tf.zeros_initializer(),
    moving_variance_initializer=tf.ones_initializer(), beta_regularizer=None,
    gamma_regularizer=None, beta_constraint=None, gamma_constraint=None,
    renorm=(False), renorm_clipping=None, renorm_momentum=0.99, fused=None,
    trainable=(True), virtual_batch_size=None, adjustment=None, name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Keras APIs handle BatchNormalization updates to the moving_mean and
moving_variance as part of their `fit()` and `evaluate()` loops. However, if a
custom training loop is used with an instance of `Model`, these updates need
to be explicitly included.  Here's a simple example of how it can be done:

```python
  # model is an instance of Model that contains BatchNormalization layer.
  update_ops = model.get_updates_for(None) + model.get_updates_for(features)
  train_op = optimizer.minimize(loss)
  train_op = tf.group([train_op, update_ops])
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
An `int` or list of `int`, the axis or axes that should be normalized,
typically the features axis/axes. For instance, after a `Conv2D` layer
with `data_format="channels_first"`, set `axis=1`. If a list of axes is
provided, each axis in `axis` will be normalized
simultaneously. Default is `-1` which uses the last axis. Note: when
using multi-axis batch norm, the `beta`, `gamma`, `moving_mean`, and
`moving_variance` variables are the same rank as the input Tensor,
with dimension size 1 in all reduced (non-axis) dimensions).
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
next layer is linear (also e.g. `nn.relu`), this can be disabled since the
scaling can be done by the next layer.
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
An optional projection function to be applied to the `beta`
weight after being updated by an `Optimizer` (e.g. used to implement norm
constraints or value constraints for layer weights). The function must
take as input the unprojected variable and must return the projected
variable (which must have the same shape). Constraints are not safe to use
when doing asynchronous distributed training.
</td>
</tr><tr>
<td>
`gamma_constraint`
</td>
<td>
An optional projection function to be applied to the
`gamma` weight after being updated by an `Optimizer`.
</td>
</tr><tr>
<td>
`renorm`
</td>
<td>
Whether to use Batch Renormalization (Ioffe, 2017). This adds extra
variables during training. The inference is the same for either value of
this parameter.
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
if `None` or `True`, use a faster, fused implementation if possible.
If `False`, use the system recommended implementation.
</td>
</tr><tr>
<td>
`trainable`
</td>
<td>
Boolean, if `True` also add variables to the graph collection
`GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
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
</tr><tr>
<td>
`name`
</td>
<td>
A string, the name of the layer.
</td>
</tr>
</table>



#### References:

Batch Normalization - Accelerating Deep Network Training by Reducing
  Internal Covariate Shift:
  [Ioffe et al., 2015](http://proceedings.mlr.press/v37/ioffe15.html)
  ([pdf](http://proceedings.mlr.press/v37/ioffe15.pdf))
Batch Renormalization - Towards Reducing Minibatch Dependence in
  Batch-Normalized Models:
  [Ioffe,
    2017](http://papers.nips.cc/paper/6790-batch-renormalization-towards-reducing-minibatch-dependence-in-batch-normalized-models)
  ([pdf](http://papers.nips.cc/paper/6790-batch-renormalization-towards-reducing-minibatch-dependence-in-batch-normalized-models.pdf))




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.
</td>
</tr><tr>
<td>
`scope_name`
</td>
<td>

</td>
</tr>
</table>



