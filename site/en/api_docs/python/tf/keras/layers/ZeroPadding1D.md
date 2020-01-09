page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.ZeroPadding1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/ZeroPadding1D">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/convolutional.py#L2073-L2110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ZeroPadding1D`

Zero-padding layer for 1D input (e.g. temporal sequence).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/ZeroPadding1D"><code>tf.compat.v1.keras.layers.ZeroPadding1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/ZeroPadding1D"><code>tf.compat.v2.keras.layers.ZeroPadding1D</code></a>


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/convolutional.py#L2092-L2095">View source</a>

``` python
__init__(
    padding=1,
    **kwargs
)
```
