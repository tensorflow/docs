page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.Flatten

## Class `Flatten`

Flattens an input tensor while preserving the batch axis (axis 0).

Inherits From: [`Flatten`](../../tf/keras/layers/Flatten), [`Layer`](../../tf/layers/Layer)

### Aliases:

* Class `tf.compat.v1.layers.Flatten`
* Class `tf.layers.Flatten`



Defined in [`python/layers/core.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/layers/core.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, ..., channels)` while `channels_first` corresponds to
  inputs with shape `(batch, channels, ...)`.


#### Examples:



```
  x = tf.compat.v1.placeholder(shape=(None, 4, 4), dtype='float32')
  y = Flatten()(x)
  # now `y` has shape `(None, 16)`

  x = tf.compat.v1.placeholder(shape=(None, 3, None), dtype='float32')
  y = Flatten()(x)
  # now `y` has shape `(None, None)`
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    data_format=None,
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






