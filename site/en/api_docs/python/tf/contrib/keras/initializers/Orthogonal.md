

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.initializers.Orthogonal

### `class tf.contrib.keras.initializers.Orthogonal`



Defined in [`tensorflow/contrib/keras/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/initializers.py).

Initializer that generates a random orthogonal matrix.

#### Arguments:

    gain: Multiplicative factor to apply to the orthogonal matrix.
    seed: A Python integer. Used to seed the random generator.

References:
    Saxe et al., http://arxiv.org/abs/1312.6120

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    gain=1.0,
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





