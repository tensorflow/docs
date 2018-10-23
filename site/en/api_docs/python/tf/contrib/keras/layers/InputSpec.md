

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.layers.InputSpec

### `class tf.contrib.keras.layers.InputSpec`



Defined in [`tensorflow/contrib/keras/python/keras/engine/topology.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/engine/topology.py).

Specifies the ndim, dtype and shape of every input to a layer.

Every layer should expose (if appropriate) an `input_spec` attribute:
a list of instances of InputSpec (one per input tensor).

A None entry in a shape is compatible with any dimension,
a None shape is compatible with any shape.

#### Arguments:

    dtype: Expected datatype of the input.
    shape: Shape tuple, expected shape of the input
        (may include None for unchecked axes).
    ndim: Integer, expected rank of the input.
    max_ndim: Integer, maximum rank of the input.
    min_ndim: Integer, minimum rank of the input.
    axes: Dictionary mapping integer axes to
        a specific dimension value.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    dtype=None,
    shape=None,
    ndim=None,
    max_ndim=None,
    min_ndim=None,
    axes=None
)
```





