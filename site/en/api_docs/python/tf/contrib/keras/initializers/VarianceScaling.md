

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.initializers.VarianceScaling

### `class tf.contrib.keras.initializers.VarianceScaling`



Defined in [`tensorflow/contrib/keras/python/keras/initializers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/initializers.py).

Initializer capable of adapting its scale to the shape of weights.

With `distribution="normal"`, samples are drawn from a truncated normal
distribution centered on zero, with `stddev = sqrt(scale / n)` where n is:
    - number of input units in the weight tensor, if mode = "fan_in"
    - number of output units, if mode = "fan_out"
    - average of the numbers of input and output units, if mode = "fan_avg"

With `distribution="uniform"`,
samples are drawn from a uniform distribution
within [-limit, limit], with `limit = sqrt(3 * scale / n)`.

#### Arguments:

    scale: Scaling factor (positive float).
    mode: One of "fan_in", "fan_out", "fan_avg".
    distribution: Random distribution to use. One of "normal", "uniform".
    seed: A Python integer. Used to seed the random generator.


#### Raises:

    ValueError: In case of an invalid value for the "scale", mode" or
      "distribution" arguments.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    scale=1.0,
    mode='fan_in',
    distribution='normal',
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





