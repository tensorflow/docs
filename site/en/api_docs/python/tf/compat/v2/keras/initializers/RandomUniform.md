page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.initializers.RandomUniform

## Class `RandomUniform`

Initializer that generates tensors with a uniform distribution.

Inherits From: [`Initializer`](../../../../../tf/compat/v2/keras/initializers/Initializer)

### Aliases:

* Class `tf.compat.v2.initializers.RandomUniform`
* Class `tf.compat.v2.keras.initializers.RandomUniform`
* Class `tf.compat.v2.random_uniform_initializer`



Defined in [`python/ops/init_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops_v2.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`minval`</b>: A python scalar or a scalar tensor. Lower bound of the range
  of random values to generate.
* <b>`maxval`</b>: A python scalar or a scalar tensor. Upper bound of the range
  of random values to generate.  Defaults to 1 for float types.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../../../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    minval=-0.05,
    maxval=0.05,
    seed=None
)
```






## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    shape,
    dtype=tf.dtypes.float32
)
```

Returns a tensor object initialized as specified by the initializer.


#### Args:


* <b>`shape`</b>: Shape of the tensor.
* <b>`dtype`</b>: Optional dtype of the tensor. Only floating point and integer
types are supported.


#### Raises:


* <b>`ValueError`</b>: If the dtype is not numeric.

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


* <b>`config`</b>: A Python dictionary.
  It will typically be the output of `get_config`.


#### Returns:

An Initializer instance.


<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```






