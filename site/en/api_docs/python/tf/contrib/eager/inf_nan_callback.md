

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.inf_nan_callback

``` python
tf.contrib.eager.inf_nan_callback(
    op_type,
    op_name,
    attrs,
    inputs,
    outputs,
    check_inf=True,
    check_nan=True,
    action=_DEFAULT_CALLBACK_ACTION
)
```



Defined in [`tensorflow/python/eager/execution_callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/eager/execution_callbacks.py).

An execution callback that checks for `inf`s and `nan`s in output tensors.

This callback can be used with `tfe.add_execute_callback` to check for invalid
numeric values. E.g.,

```python
tfe.add_execute_callback(tfe.inf_nan_callback)
```

#### Args:

* <b>`op_type`</b>: Name of the TFE operation type (e.g., `MatMul`).
* <b>`op_name`</b>: Name of the TFE operation. This name is set by client and can be
    `None` if it unset.
* <b>`attrs`</b>: Attributes of the TFE operation, as a tuple of alternating attribute
    names and attribute values.
* <b>`inputs`</b>: The `list` of input tensors to the operation, currently unused by
    this callback.
* <b>`outputs`</b>: The `list` of output tensors from the operation, checked by this
    callback for `inf` and `nan` values.
* <b>`check_inf`</b>: (`bool`) Whether this callback should check for `inf` values in
    the output tensor values.
* <b>`check_nan`</b>: (`bool`) Whether this callback should check for `nan` values in
    the output tensor values.
* <b>`action`</b>: (`str`) Action to be taken by the callback when `inf` or `nan`
    values are detected. Possible values {"raise", "warn", "print"}
    `"raise"`: Raise a `InfOrNanError`.
    `"warn"`: Log a warning using `tf.logging.warn`.
    `"print"`: Print a message to `sys.stdout`.


#### Raises:

* <b>`InfOrNanError`</b>: iff `inf` or `nan` values are seen in any of `outputs` and
    `action` is `"raise"`.
* <b>`ValueError`</b>: iff the value of `action` is invalid.