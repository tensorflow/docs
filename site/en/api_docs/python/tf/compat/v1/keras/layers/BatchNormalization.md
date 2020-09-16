description: Normalize and scale inputs or activations. (Ioffe and Szegedy, 2014).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.layers.BatchNormalization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.compat.v1.keras.layers.BatchNormalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/normalization.py#L940-L953">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Normalize and scale inputs or activations. (Ioffe and Szegedy, 2014).

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.layers.BatchNormalization(
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

Normalize the activations of the previous layer at each batch,
i.e. applies a transformation that maintains the mean activation
close to 0 and the activation standard deviation close to 1.

Batch normalization differs from other layers in several key aspects:

1) Adding BatchNormalization with `training=True` to a model causes the
result of one example to depend on the contents of all other examples in a
minibatch. Be careful when padding batches or masking examples, as these can
change the minibatch statistics and affect other examples.

2) Updates to the weights (moving statistics) are based on the forward pass
of a model rather than the result of gradient computations.

3) When performing inference using a model containing batch normalization, it
is generally (though not always) desirable to use accumulated statistics
rather than mini-batch statistics. This is accomplished by passing
`training=False` when calling the model, or using `model.predict`.

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
When the next layer is linear (also e.g. `nn.relu`),
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
tf.random.uniform(shape[-1:], -0.1, 0.1))`
will scale the normalized value by up to 7% up or down, then shift the
result by up to 0.1 (with independent scaling and bias for each feature
but shared across all examples), and finally apply gamma and/or beta. If
`None`, no adjustment is applied. Cannot be specified if
virtual_batch_size is specified.
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




Normalization equations:
  Consider the intermediate activations \(x\) of a mini-batch of size
  \\(m\\):

  We can compute the mean and variance of the batch

  \\({\mu_B} = \frac{1}{m} \sum_{i=1}^{m} {x_i}\\)

  \\({\sigma_B^2} = \frac{1}{m} \sum_{i=1}^{m} ({x_i} - {\mu_B})^2\\)

  and then compute a normalized \\(x\\), including a small factor
  \\({\epsilon}\\) for numerical stability.

  \\(\hat{x_i} = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}\\)

  And finally \\(\hat{x}\) is linearly transformed by \({\gamma}\\)
  and \\({\beta}\\), which are learned parameters:

  \\({y_i} = {\gamma * \hat{x_i} + \beta}\\)

#### References:


- [Batch Normalization: Accelerating Deep Network Training by Reducing
  Internal Covariate Shift](https://arxiv.org/abs/1502.03167)

