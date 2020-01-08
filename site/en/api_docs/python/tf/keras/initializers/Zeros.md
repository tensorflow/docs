page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.Zeros

## Class `Zeros`

Inherits From: [`Initializer`](../../../tf/keras/initializers/Initializer)

### Aliases:

* Class `tf.initializers.zeros`
* Class `tf.keras.initializers.Zeros`
* Class `tf.keras.initializers.zeros`
* Class `tf.zeros_initializer`



Defined in [`tensorflow/python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/init_ops.py).

See the guide: [Upgrade to TensorFlow 1.0 > Upgrading your code manually](../../../../../api_guides/python/upgrade#Upgrading_your_code_manually)

Initializer that generates tensors initialized to 0.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(dtype=tf.float32)
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

Example:

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





