

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.signature_def_utils.predict_signature_def

``` python
tf.saved_model.signature_def_utils.predict_signature_def(
    inputs,
    outputs
)
```



Defined in [`tensorflow/python/saved_model/signature_def_utils_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/saved_model/signature_def_utils_impl.py).

Creates prediction signature from given inputs and outputs.

This function produces signatures intended for use with the TensorFlow Serving
Predict API (tensorflow_serving/apis/prediction_service.proto). This API
imposes no constraints on the input and output types.

#### Args:

* <b>`inputs`</b>: dict of string to `Tensor`.
* <b>`outputs`</b>: dict of string to `Tensor`.


#### Returns:

A prediction-flavored signature_def.


#### Raises:

* <b>`ValueError`</b>: If inputs or outputs is `None`.