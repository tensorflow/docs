page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.applications.NASNetLarge

### Aliases:

* `tf.keras.applications.NASNetLarge`
* `tf.keras.applications.nasnet.NASNetLarge`

``` python
tf.keras.applications.NASNetLarge(
    input_shape=None,
    include_top=True,
    weights='imagenet',
    input_tensor=None,
    pooling=None,
    classes=1000
)
```



Defined in [`tensorflow/python/keras/applications/nasnet.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/applications/nasnet.py).

Instantiates a NASNet model in ImageNet mode.

Note that only TensorFlow is supported for now,
therefore it only works with the data format
`image_data_format='channels_last'` in your Keras config
at `~/.keras/keras.json`.

#### Arguments:

* <b>`input_shape`</b>: Optional shape tuple, only to be specified
        if `include_top` is False (otherwise the input shape
        has to be `(331, 331, 3)` for NASNetLarge.
        It should have exactly 3 inputs channels,
        and width and height should be no smaller than 32.
        E.g. `(224, 224, 3)` would be one valid value.
* <b>`include_top`</b>: Whether to include the fully-connected
        layer at the top of the network.
* <b>`weights`</b>: `None` (random initialization) or
        `imagenet` (ImageNet weights)
* <b>`input_tensor`</b>: Optional Keras tensor (i.e. output of
        `layers.Input()`)
        to use as image input for the model.
* <b>`pooling`</b>: Optional pooling mode for feature extraction
        when `include_top` is `False`.
        - `None` means that the output of the model
            will be the 4D tensor output of the
            last convolutional layer.
        - `avg` means that global average pooling
            will be applied to the output of the
            last convolutional layer, and thus
            the output of the model will be a
            2D tensor.
        - `max` means that global max pooling will
            be applied.
* <b>`classes`</b>: Optional number of classes to classify images
        into, only to be specified if `include_top` is True, and
        if no `weights` argument is specified.


#### Returns:

A Keras model instance.


#### Raises:

* <b>`ValueError`</b>: in case of invalid argument for `weights`,
        or invalid input shape.
* <b>`RuntimeError`</b>: If attempting to run this model with a
        backend that does not support separable convolutions.