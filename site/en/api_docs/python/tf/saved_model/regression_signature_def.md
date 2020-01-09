page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.regression_signature_def


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/saved_model/signature_def_utils_impl.py#L64-L109">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates regression signature from given examples and predictions.

### Aliases:

* <a href="/api_docs/python/tf/saved_model/regression_signature_def"><code>tf.compat.v1.saved_model.regression_signature_def</code></a>
* <a href="/api_docs/python/tf/saved_model/regression_signature_def"><code>tf.compat.v1.saved_model.signature_def_utils.regression_signature_def</code></a>
* <a href="/api_docs/python/tf/saved_model/regression_signature_def"><code>tf.saved_model.signature_def_utils.regression_signature_def</code></a>


``` python
tf.saved_model.regression_signature_def(
    examples,
    predictions
)
```



<!-- Placeholder for "Used in" -->

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
