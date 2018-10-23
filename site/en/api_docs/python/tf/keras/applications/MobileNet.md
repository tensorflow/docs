

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.applications.MobileNet

### Aliases:

* `tf.keras.applications.MobileNet`
* `tf.keras.applications.mobilenet.MobileNet`

``` python
MobileNet(
    input_shape=None,
    alpha=1.0,
    depth_multiplier=1,
    dropout=0.001,
    include_top=True,
    weights='imagenet',
    input_tensor=None,
    pooling=None,
    classes=1000
)
```



Defined in [`tensorflow/python/keras/_impl/keras/applications/mobilenet.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/applications/mobilenet.py).

Instantiates the MobileNet architecture.

Note that only TensorFlow is supported for now,
therefore it only works with the data format
`image_data_format='channels_last'` in your Keras config
at `~/.keras/keras.json`.

To load a MobileNet model via `load_model`, import the custom
objects `relu6` and `DepthwiseConv2D` and pass them to the
`custom_objects` parameter.
E.g.
model = load_model('mobilenet.h5', custom_objects={
                   'relu6': mobilenet.relu6,
                   'DepthwiseConv2D': mobilenet.DepthwiseConv2D})

#### Arguments:

* <b>`input_shape`</b>: optional shape tuple, only to be specified
        if `include_top` is False (otherwise the input shape
        has to be `(224, 224, 3)` (with `channels_last` data format)
        or (3, 224, 224) (with `channels_first` data format).
        It should have exactly 3 input channels,
        and width and height should be no smaller than 32.
        E.g. `(200, 200, 3)` would be one valid value.
* <b>`alpha`</b>: controls the width of the network.
        - If `alpha` < 1.0, proportionally decreases the number
            of filters in each layer.
        - If `alpha` > 1.0, proportionally increases the number
            of filters in each layer.
        - If `alpha` = 1, default number of filters from the paper
             are used at each layer.
* <b>`depth_multiplier`</b>: depth multiplier for depthwise convolution
        (also called the resolution multiplier)
* <b>`dropout`</b>: dropout rate
* <b>`include_top`</b>: whether to include the fully-connected
        layer at the top of the network.
* <b>`weights`</b>: one of `None` (random initialization),
        'imagenet' (pre-training on ImageNet),
        or the path to the weights file to be loaded.
* <b>`input_tensor`</b>: optional Keras tensor (i.e. output of
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
* <b>`classes`</b>: optional number of classes to classify images
        into, only to be specified if `include_top` is True, and
        if no `weights` argument is specified.


#### Returns:

A Keras model instance.


#### Raises:

* <b>`ValueError`</b>: in case of invalid argument for `weights`,
        or invalid input shape.
* <b>`RuntimeError`</b>: If attempting to run this model with a
        backend that does not support separable convolutions.