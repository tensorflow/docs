page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.GlobalMaxPool1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/pooling.py#L655-L681">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GlobalMaxPool1D`

Global max pooling operation for temporal data.



### Aliases:

* Class `tf.compat.v1.keras.layers.GlobalMaxPool1D`
* Class `tf.compat.v1.keras.layers.GlobalMaxPooling1D`
* Class `tf.compat.v2.keras.layers.GlobalMaxPool1D`
* Class `tf.compat.v2.keras.layers.GlobalMaxPooling1D`
* Class `tf.keras.layers.GlobalMaxPooling1D`


### Used in the guide:

* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)




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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/pooling.py#L580-L583">View source</a>

``` python
__init__(
    data_format='channels_last',
    **kwargs
)
```
