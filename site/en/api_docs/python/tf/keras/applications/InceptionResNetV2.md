

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.applications.InceptionResNetV2

### Aliases:

* `tf.keras.applications.InceptionResNetV2`
* `tf.keras.applications.inception_resnet_v2.InceptionResNetV2`

``` python
InceptionResNetV2(
    include_top=True,
    weights='imagenet',
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000
)
```



Defined in [`tensorflow/python/keras/_impl/keras/applications/inception_resnet_v2.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/applications/inception_resnet_v2.py).

Instantiates the Inception-ResNet v2 architecture.

Optionally loads weights pre-trained on ImageNet.
Note that when using TensorFlow, for best performance you should
set `"image_data_format": "channels_last"` in your Keras config
at `~/.keras/keras.json`.

The model and the weights are compatible with TensorFlow, Theano and
CNTK backends. The data format convention used by the model is
the one specified in your Keras config file.

Note that the default input image size for this model is 299x299, instead
of 224x224 as in the VGG16 and ResNet models. Also, the input preprocessing
function is different (i.e., do not use `imagenet_utils.preprocess_input()`
with this model. Use `preprocess_input()` defined in this module instead).

#### Arguments:

* <b>`include_top`</b>: whether to include the fully-connected
        layer at the top of the network.
* <b>`weights`</b>: one of `None` (random initialization),
        'imagenet' (pre-training on ImageNet),
        or the path to the weights file to be loaded.
* <b>`input_tensor`</b>: optional Keras tensor (i.e. output of `layers.Input()`)
        to use as image input for the model.
* <b>`input_shape`</b>: optional shape tuple, only to be specified
        if `include_top` is `False` (otherwise the input shape
        has to be `(299, 299, 3)` (with `'channels_last'` data format)
        or `(3, 299, 299)` (with `'channels_first'` data format).
        It should have exactly 3 inputs channels,
        and width and height should be no smaller than 139.
        E.g. `(150, 150, 3)` would be one valid value.
* <b>`pooling`</b>: Optional pooling mode for feature extraction
        when `include_top` is `False`.
        - `None` means that the output of the model will be
            the 4D tensor output of the last convolutional layer.
        - `'avg'` means that global average pooling
            will be applied to the output of the
            last convolutional layer, and thus
            the output of the model will be a 2D tensor.
        - `'max'` means that global max pooling will be applied.
* <b>`classes`</b>: optional number of classes to classify images
        into, only to be specified if `include_top` is `True`, and
        if no `weights` argument is specified.


#### Returns:

A Keras `Model` instance.


#### Raises:

* <b>`ValueError`</b>: in case of invalid argument for `weights`,
        or invalid input shape.