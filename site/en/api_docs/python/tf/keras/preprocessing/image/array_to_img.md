page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.array_to_img


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/preprocessing/image.py#L47-L74">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a 3D Numpy array to a PIL Image instance.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.array_to_img`
* `tf.compat.v2.keras.preprocessing.image.array_to_img`


``` python
tf.keras.preprocessing.image.array_to_img(
    x,
    data_format=None,
    scale=True,
    dtype=None
)
```



### Used in the tutorials:

* [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)




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
