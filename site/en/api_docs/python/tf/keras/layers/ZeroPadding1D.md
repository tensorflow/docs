page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ZeroPadding1D

## Class `ZeroPadding1D`

Zero-padding layer for 1D input (e.g. temporal sequence).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class `tf.compat.v1.keras.layers.ZeroPadding1D`
* Class `tf.compat.v2.keras.layers.ZeroPadding1D`
* Class `tf.keras.layers.ZeroPadding1D`



Defined in [`python/keras/layers/convolutional.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/convolutional.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`padding`</b>: Int, or tuple of int (length 2), or dictionary.
    - If int:
    How many zeros to add at the beginning and end of
    the padding dimension (axis 1).
    - If tuple of int (length 2):
    How many zeros to add at the beginning and at the end of
    the padding dimension (`(left_pad, right_pad)`).


#### Input shape:

3D tensor with shape `(batch, axis_to_pad, features)`



#### Output shape:

3D tensor with shape `(batch, padded_axis, features)`


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    padding=1,
    **kwargs
)
```






