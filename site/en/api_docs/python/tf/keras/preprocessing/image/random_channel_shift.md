

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.random_channel_shift

``` python
tf.keras.preprocessing.image.random_channel_shift(
    x,
    intensity,
    channel_axis=0
)
```



Defined in [`tensorflow/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/preprocessing/image.py).

Perform a random channel shift.

#### Arguments:

* <b>`x`</b>: Input tensor. Must be 3D.
* <b>`intensity`</b>: Transformation intensity.
* <b>`channel_axis`</b>: Index of axis for channels in the input tensor.


#### Returns:

Numpy image tensor.