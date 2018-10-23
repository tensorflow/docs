

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.initializers.Initializer

## Class `Initializer`





Defined in [`tensorflow/python/ops/init_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/init_ops.py).

Initializer base class: all initializers inherit from this class.
  

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

```
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

#### Arguments:

* <b>`config`</b>: A Python dictionary.
    It will typically be the output of `get_config`.


#### Returns:

  An Initializer instance.

<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.

#### Returns:

  A JSON-serializable Python dict.



