page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.features.VBN

## Class `VBN`





Defined in [`tensorflow/contrib/gan/python/features/python/virtual_batchnorm_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/gan/python/features/python/virtual_batchnorm_impl.py).

A class to perform virtual batch normalization.

This technique was first introduced in `Improved Techniques for Training GANs`
(Salimans et al, https://arxiv.org/abs/1606.03498). Instead of using batch
normalization on a minibatch, it fixes a reference subset of the data to use
for calculating normalization statistics.

To do this, we calculate the reference batch mean and mean square, and modify
those statistics for each example. We use mean square instead of variance,
since it is linear.

Note that if `center` or `scale` variables are created, they are shared
between all calls to this object.

The `__init__` API is intended to mimic <a href="../../../../tf/layers/batch_normalization"><code>tf.layers.batch_normalization</code></a> as
closely as possible.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    reference_batch,
    axis=-1,
    epsilon=0.001,
    center=True,
    scale=True,
    beta_initializer=tf.zeros_initializer(),
    gamma_initializer=tf.ones_initializer(),
    beta_regularizer=None,
    gamma_regularizer=None,
    trainable=True,
    name=None,
    batch_axis=0
)
```

Initialize virtual batch normalization object.

We precompute the 'mean' and 'mean squared' of the reference batch, so that
`__call__` is efficient. This means that the axis must be supplied when the
object is created, not when it is called.

We precompute 'square mean' instead of 'variance', because the square mean
can be easily adjusted on a per-example basis.

#### Args:

* <b>`reference_batch`</b>: A minibatch tensors. This will form the reference data
    from which the normalization statistics are calculated. See
    https://arxiv.org/abs/1606.03498 for more details.
* <b>`axis`</b>: Integer, the axis that should be normalized (typically the features
    axis). For instance, after a `Convolution2D` layer with
    `data_format="channels_first"`, set `axis=1` in `BatchNormalization`.
* <b>`epsilon`</b>: Small float added to variance to avoid dividing by zero.
* <b>`center`</b>: If True, add offset of `beta` to normalized tensor. If False,
    `beta` is ignored.
* <b>`scale`</b>: If True, multiply by `gamma`. If False, `gamma` is
    not used. When the next layer is linear (also e.g. `nn.relu`), this can
    be disabled since the scaling can be done by the next layer.
* <b>`beta_initializer`</b>: Initializer for the beta weight.
* <b>`gamma_initializer`</b>: Initializer for the gamma weight.
* <b>`beta_regularizer`</b>: Optional regularizer for the beta weight.
* <b>`gamma_regularizer`</b>: Optional regularizer for the gamma weight.
* <b>`trainable`</b>: Boolean, if `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
* <b>`name`</b>: String, the name of the ops.
* <b>`batch_axis`</b>: The axis of the batch dimension. This dimension is treated
    differently in `virtual batch normalization` vs `batch normalization`.


#### Raises:

* <b>`ValueError`</b>: If `reference_batch` has unknown dimensions at graph
    construction.
* <b>`ValueError`</b>: If `batch_axis` is the same as `axis`.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(inputs)
```

Run virtual batch normalization on inputs.

#### Args:

* <b>`inputs`</b>: Tensor input.


#### Returns:

A virtual batch normalized version of `inputs`.


#### Raises:

* <b>`ValueError`</b>: If `inputs` shape isn't compatible with the reference batch.

<h3 id="reference_batch_normalization"><code>reference_batch_normalization</code></h3>

``` python
reference_batch_normalization()
```

Return the reference batch, but batch normalized.



