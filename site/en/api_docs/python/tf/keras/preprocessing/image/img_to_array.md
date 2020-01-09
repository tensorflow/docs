page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.img_to_array


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/preprocessing/image.py#L77-L101">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a PIL Image instance to a Numpy array.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.img_to_array`
* `tf.compat.v2.keras.preprocessing.image.img_to_array`


``` python
tf.keras.preprocessing.image.img_to_array(
    img,
    data_format=None,
    dtype=None
)
```



### Used in the guide:

* [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)

### Used in the tutorials:

* [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)




#### Arguments:


* <b>`img`</b>: PIL Image instance.
* <b>`data_format`</b>: Image data format,
    either "channels_first" or "channels_last".
* <b>`dtype`</b>: Dtype to use for the returned array.


#### Returns:

A 3D Numpy array.



#### Raises:


* <b>`ValueError`</b>: if invalid `img` or `data_format` is passed.
