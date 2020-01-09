page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.array_to_img


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/image/array_to_img">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/preprocessing/image.py#L47-L74">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a 3D Numpy array to a PIL Image instance.

### Aliases:

* <a href="/api_docs/python/tf/keras/preprocessing/image/array_to_img"><code>tf.compat.v1.keras.preprocessing.image.array_to_img</code></a>
* <a href="/api_docs/python/tf/keras/preprocessing/image/array_to_img"><code>tf.compat.v2.keras.preprocessing.image.array_to_img</code></a>


``` python
tf.keras.preprocessing.image.array_to_img(
    x,
    data_format=None,
    scale=True,
    dtype=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Input Numpy array.
* <b>`data_format`</b>: Image data format.
    either "channels_first" or "channels_last".
* <b>`scale`</b>: Whether to rescale image values
    to be within `[0, 255]`.
* <b>`dtype`</b>: Dtype to use.


#### Returns:

A PIL Image instance.



#### Raises:


* <b>`ImportError`</b>: if PIL is not available.
* <b>`ValueError`</b>: if invalid `x` or `data_format` is passed.
