page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.resize_images


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/resize_images">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2657-L2717">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Resizes the images contained in a 4D tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/resize_images"><code>tf.compat.v1.keras.backend.resize_images</code></a>
* <a href="/api_docs/python/tf/keras/backend/resize_images"><code>tf.compat.v2.keras.backend.resize_images</code></a>


``` python
tf.keras.backend.resize_images(
    x,
    height_factor,
    width_factor,
    data_format,
    interpolation='nearest'
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable to resize.
* <b>`height_factor`</b>: Positive integer.
* <b>`width_factor`</b>: Positive integer.
* <b>`data_format`</b>: One of `"channels_first"`, `"channels_last"`.
* <b>`interpolation`</b>: A string, one of `nearest` or `bilinear`.


#### Returns:

A tensor.



#### Raises:


* <b>`ValueError`</b>: in case of incorrect value for
  `data_format` or `interpolation`.
