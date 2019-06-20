page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.orthogonal_initializer

## Class `orthogonal_initializer`

Inherits From: [`Initializer`](../tf/keras/initializers/Initializer)

### Aliases:

* Class `tf.initializers.orthogonal`
* Class `tf.keras.initializers.Orthogonal`
* Class `tf.keras.initializers.orthogonal`
* Class `tf.orthogonal_initializer`



Defined in [`tensorflow/python/ops/init_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/init_ops.py).

See the guide: [Variables > Sharing Variables](../../../api_guides/python/state_ops#Sharing_Variables)

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
    <a href="../tf/set_random_seed"><code>tf.set_random_seed</code></a>
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





