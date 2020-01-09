page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.RandomNormal


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/initializers.py#L125-L143">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RandomNormal`

Initializer that generates tensors with a normal distribution.

Inherits From: [`random_normal_initializer`](../../../tf/random_normal_initializer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/initializers/RandomNormal"><code>tf.compat.v1.keras.initializers.RandomNormal</code></a>
* Class <a href="/api_docs/python/tf/keras/initializers/RandomNormal"><code>tf.compat.v1.keras.initializers.normal</code></a>
* Class <a href="/api_docs/python/tf/keras/initializers/RandomNormal"><code>tf.compat.v1.keras.initializers.random_normal</code></a>
* Class <a href="/api_docs/python/tf/keras/initializers/RandomNormal"><code>tf.keras.initializers.normal</code></a>
* Class <a href="/api_docs/python/tf/keras/initializers/RandomNormal"><code>tf.keras.initializers.random_normal</code></a>


<!-- Placeholder for "Used in" -->


#### Args:


* <b>`mean`</b>: a python scalar or a scalar tensor. Mean of the random values to
  generate. Defaults to 0.
* <b>`stddev`</b>: a python scalar or a scalar tensor. Standard deviation of the random
  values to generate. Defaults to 0.05.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: The data type. Only floating point types are supported.


#### Returns:

RandomNormal instance.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/initializers.py#L141-L143">View source</a>

``` python
__init__(
    mean=0.0,
    stddev=0.05,
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/init_ops.py#L319-L323">View source</a>

``` python
__call__(
    shape,
    dtype=None,
    partition_info=None
)
```

Returns a tensor object initialized as specified by the initializer.


#### Args:


* <b>`shape`</b>: Shape of the tensor.
* <b>`dtype`</b>: Optional dtype of the tensor. If not provided use the initializer
  dtype.
* <b>`partition_info`</b>: Optional information about the possible partitioning of a
  tensor.

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/init_ops.py#L78-L97">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/init_ops.py#L325-L331">View source</a>

``` python
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.


#### Returns:

A JSON-serializable Python dict.
