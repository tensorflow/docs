page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.Orthogonal

## Class `Orthogonal`

Inherits From: [`Initializer`](../../../tf/keras/initializers/Initializer)

### Aliases:

* Class `tf.initializers.orthogonal`
* Class `tf.keras.initializers.Orthogonal`
* Class `tf.keras.initializers.orthogonal`
* Class `tf.orthogonal_initializer`



Defined in [`tensorflow/python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/init_ops.py).

Initializer that generates an orthogonal matrix.

If the shape of the tensor to initialize is two-dimensional, it is initialized
with an orthogonal matrix obtained from the QR decomposition of a matrix of
random numbers drawn from a normal distribution.
If the matrix has fewer rows than columns then the output will have orthogonal
rows. Otherwise, the output will have orthogonal columns.

If the shape of the tensor to initialize is more than two-dimensional,
a matrix of shape `(shape[0] * ... * shape[n - 2], shape[n - 1])`
is initialized, where `n` is the length of the shape vector.
The matrix is subsequently reshaped to give a tensor of the desired shape.

#### Args:

* <b>`gain`</b>: multiplicative factor to apply to the orthogonal matrix
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    <a href="../../../tf/random/set_random_seed"><code>tf.set_random_seed</code></a>
    for behavior.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
    calling the initializer. Only floating point types are supported.

References:
    [Saxe et al., 2014](https://openreview.net/forum?id=_wzZwKpTDF_9C)
    ([pdf](https://arxiv.org/pdf/1312.6120.pdf))

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



