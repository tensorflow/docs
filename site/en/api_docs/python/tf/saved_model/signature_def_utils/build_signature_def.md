


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.saved_model.signature_def_utils.build_signature_def

### `tf.saved_model.signature_def_utils.build_signature_def`

```
tf.saved_model.signature_def_utils.build_signature_def(inputs=None, outputs=None, method_name=None)
```


Utility function to build a SignatureDef protocol buffer.

#### Args:

* <b>`inputs`</b>: Inputs of the SignatureDef defined as a proto map of string to
      tensor info.
* <b>`outputs`</b>: Outputs of the SignatureDef defined as a proto map of string to
      tensor info.
* <b>`method_name`</b>: Method name of the SignatureDef as a string.


#### Returns:

  A SignatureDef protocol buffer constructed based on the supplied arguments.

Defined in [`tensorflow/python/saved_model/signature_def_utils_impl.py`](https://www.tensorflow.org/code/tensorflow/python/saved_model/signature_def_utils_impl.py).

