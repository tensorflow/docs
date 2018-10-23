

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.saved_model.get_signature_def_by_key

``` python
tf.contrib.saved_model.get_signature_def_by_key(
    meta_graph_def,
    signature_def_key
)
```



Defined in [`tensorflow/contrib/saved_model/python/saved_model/signature_def_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/saved_model/python/saved_model/signature_def_utils.py).

Utility function to get a SignatureDef protocol buffer by its key.

#### Args:

* <b>`meta_graph_def`</b>: MetaGraphDef protocol buffer with the SignatureDefMap to
    look up.
* <b>`signature_def_key`</b>: Key of the SignatureDef protocol buffer to find in the
    SignatureDefMap.


#### Returns:

A SignatureDef protocol buffer corresponding to the supplied key, if it
exists.


#### Raises:

* <b>`ValueError`</b>: If no entry corresponding to the supplied key is found in the
  SignatureDefMap of the MetaGraphDef.