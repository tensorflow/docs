

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.applications.densenet.preprocess_input

``` python
tf.keras.applications.densenet.preprocess_input(
    x,
    data_format=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/applications/densenet.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/applications/densenet.py).

Preprocesses a numpy array encoding a batch of images.

#### Arguments:

* <b>`x`</b>: a 3D or 4D numpy array consists of RGB values within [0, 255].
* <b>`data_format`</b>: data format of the image tensor.


#### Returns:

Preprocessed array.