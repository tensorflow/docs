page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.TruncatedNormal

## Class `TruncatedNormal`

Initializer that generates a truncated normal distribution.

Inherits From: [`truncated_normal`](../../../tf/initializers/truncated_normal)

### Aliases:

* Class `tf.compat.v1.keras.initializers.TruncatedNormal`
* Class `tf.compat.v1.keras.initializers.truncated_normal`
* Class `tf.keras.initializers.TruncatedNormal`
* Class `tf.keras.initializers.truncated_normal`



Defined in [`python/keras/initializers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/initializers.py).

<!-- Placeholder for "Used in" -->

These values are similar to values from a `random_normal_initializer`
except that values more than two standard deviations from the mean
are discarded and re-drawn. This is the recommended initializer for
neural network weights and filters.

#### Args:


* <b>`mean`</b>: a python scalar or a scalar tensor. Mean of the random values to
  generate. Defaults to 0.
* <b>`stddev`</b>: a python scalar or a scalar tensor. Standard deviation of the random
  values to generate. Defaults to 0.05.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: The data type. Only floating point types are supported.


#### Returns:

A TruncatedNormal instance.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    mean=0.0,
    stddev=0.05,
    seed=None,
    dtype=tf.dtypes.float32
)
```






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






