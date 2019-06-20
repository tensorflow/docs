page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.compute_boundary_ts

``` python
tf.contrib.graph_editor.compute_boundary_ts(ops)
```



Defined in [`tensorflow/contrib/graph_editor/select.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/graph_editor/select.py).

See the guide: [Graph Editor (contrib) > Module: select](../../../../../api_guides/python/contrib.graph_editor#Module_select)

Compute the tensors at the boundary of a set of ops.

This function looks at all the tensors connected to the given ops (in/out)
and classify them into three categories:
1) input tensors: tensors whose generating operation is not in ops.
2) output tensors: tensors whose consumer operations are not in ops
3) inside tensors: tensors which are neither input nor output tensors.

Note that a tensor can be both an inside tensor and an output tensor if it is
consumed by operations both outside and inside of `ops`.

#### Args:

* <b>`ops`</b>: an object convertible to a list of tf.Operation.

#### Returns:

A tuple `(outside_input_ts, outside_output_ts, inside_ts)` where:
  `outside_input_ts` is a Python list of input tensors;
  `outside_output_ts` is a python list of output tensors;
  `inside_ts` is a python list of inside tensors.
Since a tensor can be both an inside tensor and an output tensor,
`outside_output_ts` and `inside_ts` might intersect.

#### Raises:

* <b>`TypeError`</b>: if ops cannot be converted to a list of tf.Operation.