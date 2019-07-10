page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random_uniform_initializer

## Class `random_uniform_initializer`

Initializer that generates tensors with a uniform distribution.

Inherits From: [`Initializer`](../tf/keras/initializers/Initializer)

### Aliases:

* Class `tf.compat.v1.initializers.random_uniform`
* Class `tf.compat.v1.random_uniform_initializer`
* Class `tf.initializers.random_uniform`
* Class `tf.random_uniform_initializer`



Defined in [`python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`minval`</b>: A python scalar or a scalar tensor. Lower bound of the range of
  random values to generate.
* <b>`maxval`</b>: A python scalar or a scalar tensor. Upper bound of the range of
  random values to generate.  Defaults to 1 for float types.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
  calling the initializer.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    minval=0,
    maxval=None,
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






