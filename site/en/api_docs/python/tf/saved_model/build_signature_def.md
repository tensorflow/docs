page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.saved_model.build_signature_def

Utility function to build a SignatureDef protocol buffer.

### Aliases:

* `tf.compat.v1.saved_model.build_signature_def`
* `tf.compat.v1.saved_model.signature_def_utils.build_signature_def`
* `tf.saved_model.build_signature_def`
* `tf.saved_model.signature_def_utils.build_signature_def`

``` python
tf.saved_model.build_signature_def(
    inputs=None,
    outputs=None,
    method_name=None
)
```



Defined in [`python/saved_model/signature_def_utils_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/saved_model/signature_def_utils_impl.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`inputs`</b>: Inputs of the SignatureDef defined as a proto map of string to
    tensor info.
* <b>`outputs`</b>: Outputs of the SignatureDef defined as a proto map of string to
    tensor info.
* <b>`method_name`</b>: Method name of the SignatureDef as a string.


#### Returns:

A SignatureDef protocol buffer constructed based on the supplied arguments.
