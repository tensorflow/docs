


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.saved_model.signature_def_utils.classification_signature_def

### `tf.saved_model.signature_def_utils.classification_signature_def`

```
tf.saved_model.signature_def_utils.classification_signature_def(examples, classes, scores)
```


Creates classification signature from given examples and predictions.

#### Args:

* <b>`examples`</b>: `Tensor`.
* <b>`classes`</b>: `Tensor`.
* <b>`scores`</b>: `Tensor`.


#### Returns:

  A classification-flavored signature_def.


#### Raises:

* <b>`ValueError`</b>: If examples is `None`.

Defined in [`tensorflow/python/saved_model/signature_def_utils_impl.py`](https://www.tensorflow.org/code/tensorflow/python/saved_model/signature_def_utils_impl.py).

