page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.spatial_3d_padding


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/spatial_3d_padding">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L3031-L3072">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Pads 5D tensor with zeros along the depth, height, width dimensions.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/spatial_3d_padding"><code>tf.compat.v1.keras.backend.spatial_3d_padding</code></a>
* <a href="/api_docs/python/tf/keras/backend/spatial_3d_padding"><code>tf.compat.v2.keras.backend.spatial_3d_padding</code></a>


``` python
tf.keras.backend.spatial_3d_padding(
    x,
    padding=((1, 1), (1, 1), (1, 1)),
    data_format=None
)
```



<!-- Placeholder for "Used in" -->

Pads these dimensions with respectively
"padding[0]", "padding[1]" and "padding[2]" zeros left and right.

For 'channels_last' data_format,
the 2nd, 3rd and 4th dimension will be padded.
For 'channels_first' data_format,
the 3rd, 4th and 5th dimension will be padded.

#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`padding`</b>: Tuple of 3 tuples, padding pattern.
* <b>`data_format`</b>: One of `channels_last` or `channels_first`.


#### Returns:

A padded 5D tensor.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is neither
    `channels_last` or `channels_first`.
