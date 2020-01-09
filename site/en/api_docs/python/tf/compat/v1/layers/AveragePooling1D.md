page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.layers.AveragePooling1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/layers/pooling.py#L29-L58">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `AveragePooling1D`

Average Pooling layer for 1D inputs.

Inherits From: [`AveragePooling1D`](../../../../tf/keras/layers/AveragePooling1D), [`Layer`](../../../../tf/compat/v1/layers/Layer)

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`pool_size`</b>: An integer or tuple/list of a single integer,
  representing the size of the pooling window.
* <b>`strides`</b>: An integer or tuple/list of a single integer, specifying the
  strides of the pooling operation.
* <b>`padding`</b>: A string. The padding method, either 'valid' or 'same'.
  Case-insensitive.
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, length, channels)` while `channels_first` corresponds to
  inputs with shape `(batch, channels, length)`.
* <b>`name`</b>: A string, the name of the layer.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/layers/pooling.py#L47-L58">View source</a>

``` python
__init__(
    pool_size,
    strides,
    padding='valid',
    data_format='channels_last',
    name=None,
    **kwargs
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="scope_name"><code>scope_name</code></h3>
