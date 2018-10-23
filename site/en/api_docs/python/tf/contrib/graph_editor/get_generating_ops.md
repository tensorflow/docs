

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.graph_editor.get_generating_ops

``` python
tf.contrib.graph_editor.get_generating_ops(ts)
```



Defined in [`tensorflow/contrib/graph_editor/util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/graph_editor/util.py).

See the guide: [Graph Editor (contrib) > Module: util](../../../../../api_guides/python/contrib.graph_editor#Module_util)

Return all the generating ops of the tensors in `ts`.

#### Args:

* <b>`ts`</b>: a list of `tf.Tensor`

#### Returns:

A list of all the generating `tf.Operation` of the tensors in `ts`.

#### Raises:

* <b>`TypeError`</b>: if `ts` cannot be converted to a list of `tf.Tensor`.