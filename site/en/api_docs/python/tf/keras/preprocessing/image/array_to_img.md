page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.array_to_img

Converts a 3D Numpy array to a PIL Image instance.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.array_to_img`
* `tf.compat.v2.keras.preprocessing.image.array_to_img`
* `tf.keras.preprocessing.image.array_to_img`

``` python
tf.keras.preprocessing.image.array_to_img(
    x,
    data_format=None,
    scale=True,
    dtype=None
)
```



Defined in [`python/keras/preprocessing/image.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/preprocessing/image.py).

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