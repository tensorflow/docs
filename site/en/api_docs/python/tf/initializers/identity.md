page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.initializers.identity

## Class `identity`

Initializer that generates the identity matrix.

Inherits From: [`Initializer`](../../tf/keras/initializers/Initializer)

### Aliases:

* Class `tf.compat.v1.initializers.identity`
* Class `tf.compat.v1.keras.initializers.Identity`
* Class `tf.compat.v1.keras.initializers.identity`
* Class `tf.initializers.identity`
* Class `tf.keras.initializers.Identity`
* Class `tf.keras.initializers.identity`



Defined in [`python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops.py).

<!-- Placeholder for "Used in" -->

Only use for 2D matrices.

#### Args:


* <b>`gain`</b>: Multiplicative factor to apply to the identity matrix.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
  calling the initializer. Only floating point types are supported.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    gain=1.0,
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






