page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.MaxPooling1D

## Class `MaxPooling1D`

Max Pooling layer for 1D inputs.

Inherits From: [`MaxPool1D`](../../tf/keras/layers/MaxPool1D), [`Layer`](../../tf/layers/Layer)

### Aliases:

* Class `tf.compat.v1.layers.MaxPooling1D`
* Class `tf.layers.MaxPooling1D`



Defined in [`python/layers/pooling.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/layers/pooling.py).

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






