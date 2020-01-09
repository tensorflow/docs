page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.GlobalAveragePooling1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/GlobalAveragePooling1D">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/pooling.py#L603-L651">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GlobalAveragePooling1D`

Global average pooling operation for temporal data.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/GlobalAveragePooling1D"><code>tf.compat.v1.keras.layers.GlobalAveragePooling1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/GlobalAveragePooling1D"><code>tf.compat.v1.keras.layers.GlobalAvgPool1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/GlobalAveragePooling1D"><code>tf.compat.v2.keras.layers.GlobalAveragePooling1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/GlobalAveragePooling1D"><code>tf.compat.v2.keras.layers.GlobalAvgPool1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/GlobalAveragePooling1D"><code>tf.keras.layers.GlobalAvgPool1D</code></a>


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`data_format`</b>: A string,
  one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, steps, features)` while `channels_first`
  corresponds to inputs with shape
  `(batch, features, steps)`.


#### Call arguments:


* <b>`inputs`</b>: A 3D tensor.
* <b>`mask`</b>: Binary tensor of shape `(batch_size, steps)` indicating whether
  a given step should be masked (excluded from the average).


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/pooling.py#L632-L635">View source</a>

``` python
__init__(
    data_format='channels_last',
    **kwargs
)
```
