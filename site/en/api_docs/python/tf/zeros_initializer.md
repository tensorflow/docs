page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.zeros_initializer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops_v2.py#L93-L98">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `zeros_initializer`

Initializer that generates tensors initialized to 0.

Inherits From: [`Initializer`](../tf/keras/initializers/Initializer)

### Aliases:

* Class `tf.compat.v2.initializers.Zeros`
* Class `tf.compat.v2.initializers.zeros`
* Class `tf.compat.v2.keras.initializers.Zeros`
* Class `tf.compat.v2.keras.initializers.zeros`
* Class `tf.compat.v2.zeros_initializer`
* Class `tf.initializers.Zeros`
* Class `tf.initializers.zeros`
* Class `tf.keras.initializers.Zeros`
* Class `tf.keras.initializers.zeros`


### Used in the guide:

* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)




## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops_v2.py#L96-L98">View source</a>

``` python
__call__(
    shape,
    dtype=tf.dtypes.float32
)
```

Returns a tensor object initialized as specified by the initializer.


#### Args:


* <b>`shape`</b>: Shape of the tensor.
* <b>`dtype`</b>: Optional dtype of the tensor. If not provided will return tensor
 of <a href="../tf#float32"><code>tf.float32</code></a>.

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops_v2.py#L61-L67">View source</a>

``` python
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.


#### Returns:

A JSON-serializable Python dict.
