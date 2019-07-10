page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.layers.BatchNormalization

## Class `BatchNormalization`

Base class of Batch normalization layer (Ioffe and Szegedy, 2014).





Defined in [`python/keras/layers/normalization_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/normalization_v2.py).

<!-- Placeholder for "Used in" -->

Normalize the activations of the previous layer at each batch,
i.e. applies a transformation that maintains the mean activation
close to 0 and the activation standard deviation close to 1.

#### Arguments:


* <b>`axis`</b>: Integer, the axis that should be normalized
  (typically the features axis).
  For instance, after a `Conv2D` layer with
  `data_format="channels_first"`,
  set `axis=1` in `BatchNormalization`.
* <b>`momentum`</b>: Momentum for the moving average.
* <b>`epsilon`</b>: Small float added to variance to avoid dividing by zero.
* <b>`center`</b>: If True, add offset of `beta` to normalized tensor.
  If False, `beta` is ignored.
* <b>`scale`</b>: If True, multiply by `gamma`.
  If False, `gamma` is not used.
  When the next layer is linear (also e.g. `nn.relu`),
  this can be disabled since the scaling
  will be done by the next layer.
* <b>`beta_initializer`</b>: Initializer for the beta weight.
* <b>`gamma_initializer`</b>: Initializer for the gamma weight.
* <b>`moving_mean_initializer`</b>: Initializer for the moving mean.
* <b>`moving_variance_initializer`</b>: Initializer for the moving variance.
* <b>`beta_regularizer`</b>: Optional regularizer for the beta weight.
* <b>`gamma_regularizer`</b>: Optional regularizer for the gamma weight.
* <b>`beta_constraint`</b>: Optional constraint for the beta weight.
* <b>`gamma_constraint`</b>: Optional constraint for the gamma weight.
* <b>`renorm`</b>: Whether to use Batch Renormalization
  (https://arxiv.org/abs/1702.03275). This adds extra variables during
  training. The inference is the same for either value of this parameter.
* <b>`renorm_clipping`</b>: A dictionary that may map keys 'rmax', 'rmin', 'dmax' to
  scalar `Tensors` used to clip the renorm correction. The correction
  `(r, d)` is used as `corrected_value = normalized_value * r + d`, with
  `r` clipped to [rmin, rmax], and `d` to [-dmax, dmax]. Missing rmax, rmin,
  dmax are set to inf, 0, inf, respectively.
* <b>`renorm_momentum`</b>: Momentum used to update the moving means and standard
  deviations with renorm. Unlike `momentum`, this affects training
  and should be neither too small (which would add noise) nor too large
  (which would give stale estimates). Note that `momentum` is still applied
  to get the means and variances for inference.
* <b>`fused`</b>: if `True`, use a faster, fused implementation, or raise a ValueError
  if the fused implementation cannot be used. If `None`, use the faster
  implementation if possible. If False, do not used the fused
  implementation.
* <b>`trainable`</b>: Boolean, if `True` the variables will be marked as trainable.
* <b>`virtual_batch_size`</b>: An `int`. By default, `virtual_batch_size` is `None`,
  which means batch normalization is performed across the whole batch. When
  `virtual_batch_size` is not `None`, instead perform "Ghost Batch
  Normalization", which creates virtual sub-batches which are each
  normalized separately (with shared gamma, beta, and moving statistics).
  Must divide the actual batch size during execution.
* <b>`adjustment`</b>: A function taking the `Tensor` containing the (dynamic) shape of
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



#### References:

- [Batch Normalization: Accelerating Deep Network Training by Reducing
  Internal Covariate Shift](https://arxiv.org/abs/1502.03167)


{ {TRAINABLE_ATTRIBUTE_NOTE}}

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    axis=-1,
    momentum=0.99,
    epsilon=0.001,
    center=True,
    scale=True,
    beta_initializer='zeros',
    gamma_initializer='ones',
    moving_mean_initializer='zeros',
    moving_variance_initializer='ones',
    beta_regularizer=None,
    gamma_regularizer=None,
    beta_constraint=None,
    gamma_constraint=None,
    renorm=False,
    renorm_clipping=None,
    renorm_momentum=0.99,
    fused=None,
    trainable=True,
    virtual_batch_size=None,
    adjustment=None,
    name=None,
    **kwargs
)
```






