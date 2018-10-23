

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.lite.convert_op_hints_to_stubs

``` python
tf.contrib.lite.convert_op_hints_to_stubs(session)
```



Defined in [`tensorflow/contrib/lite/python/op_hint.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/lite/python/op_hint.py).

Converts a graphdef with LiteOp hints into stub operations.

This is used to prepare for toco conversion of complex intrinsic usages.

#### Args:

* <b>`session`</b>: A TensorFlow session that contains the graph to convert.

#### Returns:

A new graphdef with all ops contained in OpHints being replaced by
a single op call with the right parameters.