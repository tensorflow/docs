

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.convolutional_delta_orthogonal

## Class `convolutional_delta_orthogonal`

Inherits From: [`Initializer`](../../../tf/keras/initializers/Initializer)



Defined in [`tensorflow/python/ops/init_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/init_ops.py).

Initializer that generates a delta orthogonal kernel for ConvNets.

The shape of the tensor must have length 3, 4 or 5. The number of input
filters must not exceed the number of output filters. The center pixels of the
tensor form an orthogonal matrix. Other pixels are set to be zero. See
algorithm 2 in [Xiao et al., 2018]: https://arxiv.org/abs/1806.05393


#### Args:

* <b>`gain`</b>: Multiplicative factor to apply to the orthogonal matrix. Default is 1.
    The 2-norm of an input is multiplied by a factor of 'sqrt(gain)' after
    applying this convolution.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    <a href="../../../tf/set_random_seed"><code>tf.set_random_seed</code></a> for behavior.
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





