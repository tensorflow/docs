page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.uniform_unit_scaling

## Class `uniform_unit_scaling`

Initializer that generates tensors without scaling variance.

Inherits From: [`Initializer`](../../tf/keras/initializers/Initializer)

### Aliases:

* Class `tf.compat.v1.initializers.uniform_unit_scaling`
* Class `tf.compat.v1.uniform_unit_scaling_initializer`
* Class `tf.initializers.uniform_unit_scaling`
* Class `tf.uniform_unit_scaling_initializer`



Defined in [`python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops.py).

<!-- Placeholder for "Used in" -->

When initializing a deep network, it is in principle advantageous to keep
the scale of the input variance constant, so it does not explode or diminish
by reaching the final layer. If the input is `x` and the operation `x * W`,
and we want to initialize `W` uniformly at random, we need to pick `W` from

    [-sqrt(3) / sqrt(dim), sqrt(3) / sqrt(dim)]

to keep the scale intact, where `dim = W.shape[0]` (the size of the input).
A similar calculation for convolutional networks gives an analogous result
with `dim` equal to the product of the first 3 dimensions.  When
nonlinearities are present, we need to multiply this by a constant `factor`.
See (Sussillo et al., 2014) for deeper motivation, experiments
and the calculation of constants. In section 2.3 there, the constants were
numerically computed: for a linear layer it's 1.0, relu: ~1.43, tanh: ~1.15.

#### Args:


* <b>`factor`</b>: Float.  A multiplicative factor by which the values will be scaled.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
  calling the initializer. Only floating point types are supported.

#### References:

[Sussillo et al., 2014](https://arxiv.org/abs/1412.6558)
([pdf](http://arxiv.org/pdf/1412.6558.pdf))


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    factor=1.0,
    seed=None,
    dtype=tf.dtypes.float32
)
```

DEPRECATED FUNCTION (deprecated arguments)

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dtype)`. They will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use tf.initializers.variance_scaling instead with distribution=uniform to get equivalent behavior.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    shape,
    dtype=None,
    partition_info=None
)
```




<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```

Instantiates an initializer from a configuration dictionary.


#### Example:



```python
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

#### Args:


* <b>`config`</b>: A Python dictionary. It will typically be the output of
  `get_config`.


#### Returns:

An Initializer instance.


<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```






