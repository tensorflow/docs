

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.saved_model.signature_def_utils.regression_signature_def

``` python
regression_signature_def(
    examples,
    predictions
)
```



Defined in [`tensorflow/python/saved_model/signature_def_utils_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/saved_model/signature_def_utils_impl.py).

Creates regression signature from given examples and predictions.

This function produces signatures intended for use with the TensorFlow Serving
Regress API (tensorflow_serving/apis/prediction_service.proto), and so
constrains the input and output types to those allowed by TensorFlow Serving.

#### Args:

* <b>`examples`</b>: A string `Tensor`, expected to accept serialized tf.Examples.
* <b>`predictions`</b>: A float `Tensor`.


#### Returns:

A regression-flavored signature_def.


#### Raises:

* <b>`ValueError`</b>: If examples is `None`.