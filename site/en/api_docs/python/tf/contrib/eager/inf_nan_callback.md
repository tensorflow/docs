page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.inf_nan_callback

``` python
tf.contrib.eager.inf_nan_callback(
    op_type,
    inputs,
    attrs,
    outputs,
    op_name,
    check_inf=True,
    check_nan=True,
    action=_DEFAULT_CALLBACK_ACTION
)
```



Defined in [`tensorflow/python/eager/execution_callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/eager/execution_callbacks.py).

An execution callback that checks for `inf`s and `nan`s in output tensors.

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
* <b>`action`</b>: (`str`) Action to be taken by the callback when `inf` or `nan`
    values are detected. Possible values {"raise", "warn", "print"}
    `"raise"`: Raise a `InfOrNanError`.
    `"warn"`: Log a warning using <a href="../../../tf/logging/warn"><code>tf.logging.warn</code></a>.
    `"print"`: Print a message to `sys.stdout`.


#### Raises:

* <b>`InfOrNanError`</b>: iff `inf` or `nan` values are seen in any of `outputs` and
    `action` is `"raise"`.
* <b>`ValueError`</b>: iff the value of `action` is invalid.