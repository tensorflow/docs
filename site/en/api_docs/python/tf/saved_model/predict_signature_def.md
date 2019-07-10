page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.predict_signature_def

Creates prediction signature from given inputs and outputs.

### Aliases:

* `tf.compat.v1.saved_model.predict_signature_def`
* `tf.compat.v1.saved_model.signature_def_utils.predict_signature_def`
* `tf.saved_model.predict_signature_def`
* `tf.saved_model.signature_def_utils.predict_signature_def`

``` python
tf.saved_model.predict_signature_def(
    inputs,
    outputs
)
```



Defined in [`python/saved_model/signature_def_utils_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/saved_model/signature_def_utils_impl.py).

<!-- Placeholder for "Used in" -->

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