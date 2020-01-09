

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.applications.densenet.preprocess_input

``` python
tf.keras.applications.densenet.preprocess_input(
    x,
    data_format=None
)
```



Defined in [`tensorflow/python/keras/applications/densenet.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/applications/densenet.py).

Preprocesses a numpy array encoding a batch of images.

#### Arguments:

* <b>`x`</b>: a 3D or 4D numpy array consists of RGB values within [0, 255].
* <b>`data_format`</b>: data format of the image tensor.


#### Returns:

Preprocessed array.