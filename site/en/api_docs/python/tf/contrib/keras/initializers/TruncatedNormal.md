

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.initializers.TruncatedNormal

### `class tf.contrib.keras.initializers.TruncatedNormal`



Defined in [`tensorflow/contrib/keras/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/initializers.py).

Initializer that generates a truncated normal distribution.

These values are similar to values from a `random_normal_initializer`
except that values more than two standard deviations from the mean
are discarded and re-drawn. This is the recommended initializer for
neural network weights and filters.

#### Arguments:

    mean: a python scalar or a scalar tensor. Mean of the random values
      to generate.
    stddev: a python scalar or a scalar tensor. Standard deviation of the
      random values to generate.
    seed: A Python integer. Used to seed the random generator.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    mean=0.0,
    stddev=0.05,
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





