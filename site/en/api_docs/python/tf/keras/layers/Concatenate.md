page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Concatenate

## Class `Concatenate`

Layer that concatenates a list of inputs.



### Aliases:

* Class `tf.compat.v1.keras.layers.Concatenate`
* Class `tf.compat.v2.keras.layers.Concatenate`
* Class `tf.keras.layers.Concatenate`



Defined in [`python/keras/layers/merge.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/merge.py).

<!-- Placeholder for "Used in" -->

It takes as input a list of tensors,
all of the same shape except for the concatenation axis,
and returns a single tensor, the concatenation of all inputs.

#### Arguments:


* <b>`axis`</b>: Axis along which to concatenate.
* <b>`**kwargs`</b>: standard layer keyword arguments.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    axis=-1,
    **kwargs
)
```






