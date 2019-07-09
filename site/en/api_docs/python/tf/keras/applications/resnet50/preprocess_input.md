page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.applications.resnet50.preprocess_input

### Aliases:

* `tf.keras.applications.resnet50.preprocess_input`
* `tf.keras.applications.vgg16.preprocess_input`
* `tf.keras.applications.vgg19.preprocess_input`

``` python
tf.keras.applications.resnet50.preprocess_input(
    x,
    data_format=None,
    mode='caffe'
)
```



Defined in [`tensorflow/python/keras/applications/imagenet_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/applications/imagenet_utils.py).

Preprocesses a tensor or Numpy array encoding a batch of images.

#### Arguments:

* <b>`x`</b>: Input Numpy or symbolic tensor, 3D or 4D.
* <b>`data_format`</b>: Data format of the image tensor/array.
* <b>`mode`</b>: One of "caffe", "tf".
        - caffe: will convert the images from RGB to BGR,
            then will zero-center each color channel with
            respect to the ImageNet dataset,
            without scaling.
        - tf: will scale pixels between -1 and 1,
            sample-wise.


#### Returns:

Preprocessed tensor or Numpy array.


#### Raises:

* <b>`ValueError`</b>: In case of unknown `data_format` argument.