page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.save_img


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/preprocessing/image.py#L104-L131">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Saves an image stored as a Numpy array to a path or file object.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.save_img`
* `tf.compat.v2.keras.preprocessing.image.save_img`


``` python
tf.keras.preprocessing.image.save_img(
    path,
    x,
    data_format=None,
    file_format=None,
    scale=True,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`path`</b>: Path or file object.
* <b>`x`</b>: Numpy array.
* <b>`data_format`</b>: Image data format,
    either "channels_first" or "channels_last".
* <b>`file_format`</b>: Optional file format override. If omitted, the
    format to use is determined from the filename extension.
    If a file object was used instead of a filename, this
    parameter should always be used.
* <b>`scale`</b>: Whether to rescale image values to be within `[0, 255]`.
* <b>`**kwargs`</b>: Additional keyword arguments passed to `PIL.Image.save()`.
