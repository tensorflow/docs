

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.applications.Xception

### `tf.contrib.keras.applications.Xception`
### `tf.contrib.keras.applications.xception.Xception`

``` python
Xception(
    include_top=True,
    weights='imagenet',
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000
)
```



Defined in [`tensorflow/contrib/keras/python/keras/applications/xception.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/applications/xception.py).

Instantiates the Xception architecture.

Optionally loads weights pre-trained
on ImageNet. This model is available for TensorFlow only,
and can only be used with inputs following the TensorFlow
data format `(width, height, channels)`.
You should set `image_data_format="channels_last"` in your Keras config
located at ~/.keras/keras.json.

Note that the default input image size for this model is 299x299.

#### Arguments:

    include_top: whether to include the fully-connected
        layer at the top of the network.
    weights: one of `None` (random initialization)
        or "imagenet" (pre-training on ImageNet).
    input_tensor: optional Keras tensor (i.e. output of `layers.Input()`)
        to use as image input for the model.
    input_shape: optional shape tuple, only to be specified
        if `include_top` is False (otherwise the input shape
        has to be `(299, 299, 3)`.
        It should have exactly 3 inputs channels,
        and width and height should be no smaller than 71.
        E.g. `(150, 150, 3)` would be one valid value.
    pooling: Optional pooling mode for feature extraction
        when `include_top` is `False`.
        - `None` means that the output of the model will be
            the 4D tensor output of the
            last convolutional layer.
        - `avg` means that global average pooling
            will be applied to the output of the
            last convolutional layer, and thus
            the output of the model will be a 2D tensor.
        - `max` means that global max pooling will
            be applied.
    classes: optional number of classes to classify images
        into, only to be specified if `include_top` is True, and
        if no `weights` argument is specified.


#### Returns:

    A Keras model instance.


#### Raises:

    ValueError: in case of invalid argument for `weights`,
        or invalid input shape.
    RuntimeError: If attempting to run this model with a
        backend that does not support separable convolutions.