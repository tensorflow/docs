page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.keras.initializers.VarianceScaling

## Class `VarianceScaling`

Initializer capable of adapting its scale to the shape of weights tensors.

Inherits From: [`Initializer`](../../../../../tf/compat/v2/keras/initializers/Initializer)

### Aliases:

* Class `tf.compat.v2.initializers.VarianceScaling`
* Class `tf.compat.v2.keras.initializers.VarianceScaling`



Defined in [`python/ops/init_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/init_ops_v2.py).

<!-- Placeholder for "Used in" -->

With `distribution="truncated_normal" or "untruncated_normal"`,
samples are drawn from a truncated/untruncated normal
distribution with a mean of zero and a standard deviation (after truncation,
if used) `stddev = sqrt(scale / n)`
where n is:
  - number of input units in the weight tensor, if mode = "fan_in"
  - number of output units, if mode = "fan_out"
  - average of the numbers of input and output units, if mode = "fan_avg"

With `distribution="uniform"`, samples are drawn from a uniform distribution
within [-limit, limit], with `limit = sqrt(3 * scale / n)`.

#### Args:


* <b>`scale`</b>: Scaling factor (positive float).
* <b>`mode`</b>: One of "fan_in", "fan_out", "fan_avg".
* <b>`distribution`</b>: Random distribution to use. One of "truncated_normal",
  "untruncated_normal" and  "uniform".
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../../../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.


#### Raises:


* <b>`ValueError`</b>: In case of an invalid value for the "scale", mode" or
  "distribution" arguments.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    scale=1.0,
    mode='fan_in',
    distribution='truncated_normal',
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






