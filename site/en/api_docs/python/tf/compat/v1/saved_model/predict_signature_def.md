page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.saved_model.predict_signature_def


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/signature_def_utils_impl.py#L171-L209">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates prediction signature from given inputs and outputs.

### Aliases:

* `tf.compat.v1.saved_model.signature_def_utils.predict_signature_def`


``` python
tf.compat.v1.saved_model.predict_signature_def(
    inputs,
    outputs
)
```



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
