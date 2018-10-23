

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.applications.resnet50.preprocess_input

### `tf.contrib.keras.applications.resnet50.preprocess_input`
### `tf.contrib.keras.applications.vgg16.preprocess_input`
### `tf.contrib.keras.applications.vgg19.preprocess_input`

``` python
preprocess_input(
    x,
    data_format=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/applications/imagenet_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/applications/imagenet_utils.py).

Preprocesses a tensor encoding a batch of images.

#### Arguments:

    x: input Numpy tensor, 4D.
    data_format: data format of the image tensor.


#### Returns:

    Preprocessed tensor.