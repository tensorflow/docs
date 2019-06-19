page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.convolutional_orthogonal_1d

## Class `convolutional_orthogonal_1d`





Defined in [`tensorflow/python/ops/init_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/init_ops.py).

Initializer that generates a 1D orthogonal kernel for ConvNets.

The shape of the tensor must have length 3. The number of input
filters must not exceed the number of output filters.
The orthogonality(==isometry) is exact when the inputs are circular padded.
There are finite-width effects with non-circular padding (e.g. zero padding).

#### Args:

* <b>`gain`</b>: Multiplicative factor to apply to the orthogonal matrix. Default is 1.
    The 2-norm of an input is multiplied by a factor of 'sqrt(gain)' after
    applying this convolution.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    <a href="../../../tf/set_random_seed"><code>tf.set_random_seed</code></a>
    for behavior.
* <b>`dtype`</b>: The data type.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    gain=1.0,
    seed=None,
    dtype=tf.float32
)
```



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





