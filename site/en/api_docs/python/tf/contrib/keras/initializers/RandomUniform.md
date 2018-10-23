

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.initializers.RandomUniform

### `class tf.contrib.keras.initializers.RandomUniform`



Defined in [`tensorflow/contrib/keras/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/initializers.py).

Initializer that generates tensors with a uniform distribution.

#### Arguments:

    minval: A python scalar or a scalar tensor. Lower bound of the range
      of random values to generate.
    maxval: A python scalar or a scalar tensor. Upper bound of the range
      of random values to generate.  Defaults to 1 for float types.
    seed: A Python integer. Used to seed the random generator.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    minval=-0.05,
    maxval=0.05,
    seed=None
)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    shape,
    dtype=None
)
```



<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```



<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```





