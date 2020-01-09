page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.saved_model.classification_signature_def


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/saved_model/signature_def_utils_impl.py#L112-L168">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates classification signature from given examples and predictions.

### Aliases:

* `tf.compat.v1.saved_model.signature_def_utils.classification_signature_def`


``` python
tf.compat.v1.saved_model.classification_signature_def(
    examples,
    classes,
    scores
)
```



<!-- Placeholder for "Used in" -->

This function produces signatures intended for use with the TensorFlow Serving
Classify API (tensorflow_serving/apis/prediction_service.proto), and so
constrains the input and output types to those allowed by TensorFlow Serving.

#### Args:


* <b>`examples`</b>: A string `Tensor`, expected to accept serialized tf.Examples.
* <b>`classes`</b>: A string `Tensor`.  Note that the ClassificationResponse message
  requires that class labels are strings, not integers or anything else.
* <b>`scores`</b>: a float `Tensor`.


#### Returns:

A classification-flavored signature_def.



#### Raises:


* <b>`ValueError`</b>: If examples is `None`.
