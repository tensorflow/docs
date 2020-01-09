page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.inf_nan_callback


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/execution_callbacks.py#L125-L204">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



An execution callback that checks for `inf`s and `nan`s in output tensors.

``` python
tf.contrib.eager.inf_nan_callback(
    op_type,
    inputs,
    attrs,
    outputs,
    op_name,
    check_inf=True,
    check_nan=True,
    action=tf.contrib.eager.ExecutionCallback.RAISE
)
```



<!-- Placeholder for "Used in" -->

This callback can be used with `tfe.add_execute_callback` to check for invalid
numeric values. E.g.,

```python
tfe.add_execute_callback(tfe.inf_nan_callback)
```

#### Args:


* <b>`op_type`</b>: Name of the TFE operation type (e.g., `MatMul`).
* <b>`inputs`</b>: The `list` of input tensors to the operation, currently unused by
  this callback.
* <b>`attrs`</b>: Attributes of the TFE operation, as a tuple of alternating attribute
  names and attribute values.
* <b>`outputs`</b>: The `list` of output tensors from the operation, checked by this
  callback for `inf` and `nan` values.
* <b>`op_name`</b>: Name of the TFE operation. This name is set by client and can be
  `None` if it unset.
* <b>`check_inf`</b>: (`bool`) Whether this callback should check for `inf` values in
  the output tensor values.
* <b>`check_nan`</b>: (`bool`) Whether this callback should check for `nan` values in
  the output tensor values.
* <b>`action`</b>: (`ExecutionCallback`) Action to be taken by the callback when
  `inf` or `nan` values are detected.


#### Raises:


* <b>`InfOrNanError`</b>: iff `inf` or `nan` values are seen in any of `outputs` and
  `action` is `"raise"`.
* <b>`ValueError`</b>: iff the value of `action` is invalid.
