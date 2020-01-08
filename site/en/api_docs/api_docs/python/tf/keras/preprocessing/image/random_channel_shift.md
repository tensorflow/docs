

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.random_channel_shift

``` python
tf.keras.preprocessing.image.random_channel_shift(
    x,
    intensity,
    channel_axis=0
)
```



Defined in [`tensorflow/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/preprocessing/image.py).

Perform a random channel shift.

#### Arguments:

* <b>`x`</b>: Input tensor. Must be 3D.
* <b>`intensity`</b>: Transformation intensity.
* <b>`channel_axis`</b>: Index of axis for channels in the input tensor.


#### Returns:

Numpy image tensor.