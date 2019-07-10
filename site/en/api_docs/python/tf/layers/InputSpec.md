page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.InputSpec

## Class `InputSpec`

Specifies the ndim, dtype and shape of every input to a layer.



### Aliases:

* Class `tf.compat.v1.keras.layers.InputSpec`
* Class `tf.compat.v1.layers.InputSpec`
* Class `tf.compat.v2.keras.layers.InputSpec`
* Class `tf.keras.layers.InputSpec`
* Class `tf.layers.InputSpec`



Defined in [`python/keras/engine/input_spec.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/engine/input_spec.py).

<!-- Placeholder for "Used in" -->

Every layer should expose (if appropriate) an `input_spec` attribute:
a list of instances of InputSpec (one per input tensor).

A None entry in a shape is compatible with any dimension,
a None shape is compatible with any shape.

#### Arguments:


* <b>`dtype`</b>: Expected DataType of the input.
* <b>`shape`</b>: Shape tuple, expected shape of the input
    (may include None for unchecked axes).
* <b>`ndim`</b>: Integer, expected rank of the input.
* <b>`max_ndim`</b>: Integer, maximum rank of the input.
* <b>`min_ndim`</b>: Integer, minimum rank of the input.
* <b>`axes`</b>: Dictionary mapping integer axes to
    a specific dimension value.

<h2 id="__init__"><code>__init__</code></h2>

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






