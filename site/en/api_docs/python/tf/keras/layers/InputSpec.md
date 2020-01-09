page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.InputSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/input_spec.py#L34-L103">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `InputSpec`

Specifies the ndim, dtype and shape of every input to a layer.



### Aliases:

* Class `tf.compat.v1.keras.layers.InputSpec`
* Class `tf.compat.v1.layers.InputSpec`
* Class `tf.compat.v2.keras.layers.InputSpec`


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/input_spec.py#L54-L81">View source</a>

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

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/input_spec.py#L101-L103">View source</a>

``` python
@classmethod
from_config(
    cls,
    config
)
```




<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/engine/input_spec.py#L92-L99">View source</a>

``` python
get_config()
```
