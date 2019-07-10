page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.glorot_uniform_initializer

## Class `glorot_uniform_initializer`

The Glorot uniform initializer, also called Xavier uniform initializer.

Inherits From: [`variance_scaling`](../tf/initializers/variance_scaling)

### Aliases:

* Class `tf.compat.v1.glorot_uniform_initializer`
* Class `tf.compat.v1.initializers.glorot_uniform`
* Class `tf.compat.v1.keras.initializers.glorot_uniform`
* Class `tf.glorot_uniform_initializer`
* Class `tf.initializers.glorot_uniform`
* Class `tf.keras.initializers.glorot_uniform`



Defined in [`python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops.py).

<!-- Placeholder for "Used in" -->

It draws samples from a uniform distribution within [-limit, limit]
where `limit` is `sqrt(6 / (fan_in + fan_out))`
where `fan_in` is the number of input units in the weight tensor
and `fan_out` is the number of output units in the weight tensor.

#### Args:


* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
  calling the initializer. Only floating point types are supported.

#### References:

[Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
([pdf](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf))


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    seed=None,
    dtype=tf.dtypes.float32
)
```

DEPRECATED FUNCTION ARGUMENTS

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dtype)`. They will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor



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






