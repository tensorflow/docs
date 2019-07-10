page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.initializers.RandomNormal

## Class `RandomNormal`

Initializer that generates tensors with a normal distribution.

Inherits From: [`Initializer`](../../../../../tf/compat/v2/keras/initializers/Initializer)

### Aliases:

* Class `tf.compat.v2.initializers.RandomNormal`
* Class `tf.compat.v2.keras.initializers.RandomNormal`
* Class `tf.compat.v2.random_normal_initializer`



Defined in [`python/ops/init_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops_v2.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`mean`</b>: a python scalar or a scalar tensor. Mean of the random values
  to generate.
* <b>`stddev`</b>: a python scalar or a scalar tensor. Standard deviation of the
  random values to generate.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../../../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    mean=0.0,
    stddev=0.05,
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
* <b>`dtype`</b>: Optional dtype of the tensor. Only floating point types are
 supported.


#### Raises:


* <b>`ValueError`</b>: If the dtype is not floating point

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






