

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.applications.densenet.decode_predictions

### Aliases:

* `tf.keras.applications.densenet.decode_predictions`
* `tf.keras.applications.inception_resnet_v2.decode_predictions`
* `tf.keras.applications.inception_v3.decode_predictions`
* `tf.keras.applications.mobilenet.decode_predictions`
* `tf.keras.applications.nasnet.decode_predictions`
* `tf.keras.applications.resnet50.decode_predictions`
* `tf.keras.applications.vgg16.decode_predictions`
* `tf.keras.applications.vgg19.decode_predictions`
* `tf.keras.applications.xception.decode_predictions`

``` python
tf.keras.applications.densenet.decode_predictions(
    preds,
    top=5
)
```



Defined in [`tensorflow/python/keras/applications/imagenet_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/applications/imagenet_utils.py).

Decodes the prediction of an ImageNet model.

#### Arguments:

* <b>`preds`</b>: Numpy tensor encoding a batch of predictions.
* <b>`top`</b>: Integer, how many top-guesses to return.


#### Returns:

A list of lists of top class prediction tuples
`(class_name, class_description, score)`.
One list of tuples per sample in batch input.


#### Raises:

* <b>`ValueError`</b>: In case of invalid shape of the `pred` array
        (must be 2D).