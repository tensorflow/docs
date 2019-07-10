page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.img_to_array

Converts a PIL Image instance to a Numpy array.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.img_to_array`
* `tf.compat.v2.keras.preprocessing.image.img_to_array`
* `tf.keras.preprocessing.image.img_to_array`

``` python
tf.keras.preprocessing.image.img_to_array(
    img,
    data_format=None,
    dtype=None
)
```



Defined in [`python/keras/preprocessing/image.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/preprocessing/image.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`img`</b>: PIL Image instance.
* <b>`data_format`</b>: Image data format,
    either "channels_first" or "channels_last".
* <b>`dtype`</b>: Dtype to use for the returned array.


#### Returns:

A 3D Numpy array.



#### Raises:


* <b>`ValueError`</b>: if invalid `img` or `data_format` is passed.