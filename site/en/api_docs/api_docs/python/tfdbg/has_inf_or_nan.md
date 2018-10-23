

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tfdbg.has_inf_or_nan

``` python
has_inf_or_nan(
    datum,
    tensor
)
```



Defined in [`tensorflow/python/debug/lib/debug_data.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/debug/lib/debug_data.py).

See the guide: [TensorFlow Debugger > Tensor-value predicates](../../../api_guides/python/tfdbg#Tensor_value_predicates)

A predicate for whether a tensor consists of any bad numerical values.

This predicate is common enough to merit definition in this module.
Bad numerical values include `nan`s and `inf`s.
The signature of this function follows the requirement of the method
`DebugDumpDir.find()`.

#### Args:

* <b>`datum`</b>: (`DebugTensorDatum`) Datum metadata.
* <b>`tensor`</b>: (`numpy.ndarray` or None) Value of the tensor. None represents
    an uninitialized tensor.


#### Returns:

  (`bool`) True if and only if tensor consists of any nan or inf values.