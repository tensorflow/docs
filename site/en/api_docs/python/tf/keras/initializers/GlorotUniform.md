page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.GlorotUniform


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops_v2.py#L557-L583">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GlorotUniform`

The Glorot uniform initializer, also called Xavier uniform initializer.

Inherits From: [`VarianceScaling`](../../../tf/keras/initializers/VarianceScaling)

### Aliases:

* Class `tf.compat.v2.initializers.GlorotUniform`
* Class `tf.compat.v2.initializers.glorot_uniform`
* Class `tf.compat.v2.keras.initializers.GlorotUniform`
* Class `tf.compat.v2.keras.initializers.glorot_uniform`
* Class `tf.initializers.GlorotUniform`
* Class `tf.initializers.glorot_uniform`
* Class `tf.keras.initializers.glorot_uniform`


<!-- Placeholder for "Used in" -->

It draws samples from a uniform distribution within [-limit, limit]
where `limit` is `sqrt(6 / (fan_in + fan_out))`
where `fan_in` is the number of input units in the weight tensor
and `fan_out` is the number of output units in the weight tensor.

#### Args:


* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.


#### References:

[Glorot et al., 2010](http://proceedings.mlr.press/v9/glorot10a.html)
([pdf](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf))


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops_v2.py#L575-L580">View source</a>

``` python
__init__(seed=None)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops_v2.py#L404-L437">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops_v2.py#L69-L89">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops_v2.py#L582-L583">View source</a>

``` python
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.


#### Returns:

A JSON-serializable Python dict.
