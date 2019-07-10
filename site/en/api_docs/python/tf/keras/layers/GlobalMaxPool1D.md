page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.GlobalMaxPool1D

## Class `GlobalMaxPool1D`

Global max pooling operation for temporal data.



### Aliases:

* Class `tf.compat.v1.keras.layers.GlobalMaxPool1D`
* Class `tf.compat.v1.keras.layers.GlobalMaxPooling1D`
* Class `tf.compat.v2.keras.layers.GlobalMaxPool1D`
* Class `tf.compat.v2.keras.layers.GlobalMaxPooling1D`
* Class `tf.keras.layers.GlobalMaxPool1D`
* Class `tf.keras.layers.GlobalMaxPooling1D`



Defined in [`python/keras/layers/pooling.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/pooling.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`data_format`</b>: A string,
  one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, steps, features)` while `channels_first`
  corresponds to inputs with shape
  `(batch, features, steps)`.


#### Input shape:

- If `data_format='channels_last'`:
  3D tensor with shape:
  `(batch_size, steps, features)`
- If `data_format='channels_first'`:
  3D tensor with shape:
  `(batch_size, features, steps)`



#### Output shape:

2D tensor with shape `(batch_size, features)`.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    data_format='channels_last',
    **kwargs
)
```






