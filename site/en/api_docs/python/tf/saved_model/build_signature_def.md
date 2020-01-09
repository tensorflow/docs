page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.build_signature_def


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/saved_model/signature_def_utils_impl.py#L32-L61">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Utility function to build a SignatureDef protocol buffer.

### Aliases:

* <a href="/api_docs/python/tf/saved_model/build_signature_def"><code>tf.compat.v1.saved_model.build_signature_def</code></a>
* <a href="/api_docs/python/tf/saved_model/build_signature_def"><code>tf.compat.v1.saved_model.signature_def_utils.build_signature_def</code></a>
* <a href="/api_docs/python/tf/saved_model/build_signature_def"><code>tf.saved_model.signature_def_utils.build_signature_def</code></a>


``` python
tf.saved_model.build_signature_def(
    inputs=None,
    outputs=None,
    method_name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`inputs`</b>: Inputs of the SignatureDef defined as a proto map of string to
    tensor info.
* <b>`outputs`</b>: Outputs of the SignatureDef defined as a proto map of string to
    tensor info.
* <b>`method_name`</b>: Method name of the SignatureDef as a string.


#### Returns:

A SignatureDef protocol buffer constructed based on the supplied arguments.
