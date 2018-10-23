

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.applications.resnet50.preprocess_input

### Aliases:

* `tf.keras.applications.resnet50.preprocess_input`
* `tf.keras.applications.vgg16.preprocess_input`
* `tf.keras.applications.vgg19.preprocess_input`

``` python
preprocess_input(
    x,
    data_format=None,
    mode='caffe'
)
```



Defined in [`tensorflow/python/keras/_impl/keras/applications/imagenet_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/applications/imagenet_utils.py).

Preprocesses a tensor encoding a batch of images.

#### Arguments:

* <b>`x`</b>: input Numpy or symoblic tensor, 3D or 4D.
* <b>`data_format`</b>: data format of the image tensor.
* <b>`mode`</b>: One of "caffe", "tf".
        - caffe: will convert the images from RGB to BGR,
            then will zero-center each color channel with
            respect to the ImageNet dataset,
            without scaling.
        - tf: will scale pixels between -1 and 1,
            sample-wise.


#### Returns:

Preprocessed tensor.


#### Raises:

* <b>`ValueError`</b>: in case of incorrect data_format.