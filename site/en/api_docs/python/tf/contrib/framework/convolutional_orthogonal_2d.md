page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.convolutional_orthogonal_2d

## Class `convolutional_orthogonal_2d`





Defined in [`tensorflow/python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/init_ops.py).

Initializer that generates a 2D orthogonal kernel for ConvNets.

The shape of the tensor must have length 4. The number of input
filters must not exceed the number of output filters.
The orthogonality(==isometry) is exact when the inputs are circular padded.
There are finite-width effects with non-circular padding (e.g. zero padding).
See algorithm 1 in (Xiao et al., 2018).

#### Args:

* <b>`gain`</b>: Multiplicative factor to apply to the orthogonal
    matrix. Default is 1. This has the effect of scaling the output 2-norm by
    a factor of `gain`.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    <a href="../../../tf/random/set_random_seed"><code>tf.set_random_seed</code></a> for behavior.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
    calling the initializer. Only floating point types are supported.

References:
    [Xiao et al., 2018](http://proceedings.mlr.press/v80/xiao18a.html)
    ([pdf](http://proceedings.mlr.press/v80/xiao18a/xiao18a.pdf))

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    gain=1.0,
    seed=None,
    dtype=tf.dtypes.float32
)
```

Initialize self.  See help(type(self)) for accurate signature.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

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

Returns the configuration of the initializer as a JSON-serializable dict.

#### Returns:

A JSON-serializable Python dict.



