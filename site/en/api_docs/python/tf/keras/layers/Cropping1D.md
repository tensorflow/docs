page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.Cropping1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/Cropping1D">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/convolutional.py#L2334-L2374">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Cropping1D`

Cropping layer for 1D input (e.g. temporal sequence).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/Cropping1D"><code>tf.compat.v1.keras.layers.Cropping1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/Cropping1D"><code>tf.compat.v2.keras.layers.Cropping1D</code></a>


<!-- Placeholder for "Used in" -->

It crops along the time dimension (axis 1).

#### Arguments:


* <b>`cropping`</b>: Int or tuple of int (length 2)
  How many units should be trimmed off at the beginning and end of
  the cropping dimension (axis 1).
  If a single int is provided, the same value will be used for both.


#### Input shape:

3D tensor with shape `(batch, axis_to_crop, features)`



#### Output shape:

3D tensor with shape `(batch, cropped_axis, features)`


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/convolutional.py#L2352-L2355">View source</a>

``` python
__init__(
    cropping=(1, 1),
    **kwargs
)
```
