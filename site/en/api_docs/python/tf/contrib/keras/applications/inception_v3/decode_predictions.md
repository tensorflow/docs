

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.applications.inception_v3.decode_predictions

### `tf.contrib.keras.applications.inception_v3.decode_predictions`
### `tf.contrib.keras.applications.resnet50.decode_predictions`
### `tf.contrib.keras.applications.vgg16.decode_predictions`
### `tf.contrib.keras.applications.vgg19.decode_predictions`
### `tf.contrib.keras.applications.xception.decode_predictions`

``` python
decode_predictions(
    preds,
    top=5
)
```



Defined in [`tensorflow/contrib/keras/python/keras/applications/imagenet_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/applications/imagenet_utils.py).

Decodes the prediction of an ImageNet model.

#### Arguments:

    preds: Numpy tensor encoding a batch of predictions.
    top: integer, how many top-guesses to return.


#### Returns:

    A list of lists of top class prediction tuples
    `(class_name, class_description, score)`.
    One list of tuples per sample in batch input.


#### Raises:

    ValueError: in case of invalid shape of the `pred` array
        (must be 2D).