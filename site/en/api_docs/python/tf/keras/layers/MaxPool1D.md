page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.MaxPool1D


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/layers/MaxPool1D">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/pooling.py#L112-L151">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MaxPool1D`

Max pooling operation for temporal data.



### Aliases:

* Class <a href="/api_docs/python/tf/keras/layers/MaxPool1D"><code>tf.compat.v1.keras.layers.MaxPool1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/MaxPool1D"><code>tf.compat.v1.keras.layers.MaxPooling1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/MaxPool1D"><code>tf.compat.v2.keras.layers.MaxPool1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/MaxPool1D"><code>tf.compat.v2.keras.layers.MaxPooling1D</code></a>
* Class <a href="/api_docs/python/tf/keras/layers/MaxPool1D"><code>tf.keras.layers.MaxPooling1D</code></a>


<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`pool_size`</b>: Integer, size of the max pooling windows.
* <b>`strides`</b>: Integer, or None. Factor by which to downscale.
  E.g. 2 will halve the input.
  If None, it will default to `pool_size`.
* <b>`padding`</b>: One of `"valid"` or `"same"` (case-insensitive).
* <b>`data_format`</b>: A string,
  one of `channels_last` (default) or `channels_first`.
  The ordering of the dimensions in the inputs.
  `channels_last` corresponds to inputs with shape
  `(batch, steps, features)` while `channels_first`
  corresponds to inputs with shape
  `(batch, features, steps)`.


#### Input shape:

- If `data_format='channels_last'`:
  3D tensor with shape `(batch_size, steps, features)`.
- If `data_format='channels_first'`:
  3D tensor with shape `(batch_size, features, steps)`.



#### Output shape:

- If `data_format='channels_last'`:
  3D tensor with shape `(batch_size, downsampled_steps, features)`.
- If `data_format='channels_first'`:
  3D tensor with shape `(batch_size, features, downsampled_steps)`.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/layers/pooling.py#L142-L151">View source</a>

``` python
__init__(
    pool_size=2,
    strides=None,
    padding='valid',
    data_format='channels_last',
    **kwargs
)
```
