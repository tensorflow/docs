

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.nan_callback

``` python
tf.contrib.eager.nan_callback(
    op_type,
    op_name,
    attrs,
    inputs,
    outputs,
    action=_DEFAULT_CALLBACK_ACTION
)
```



Defined in [`tensorflow/python/eager/execution_callbacks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/eager/execution_callbacks.py).

A specialization of `inf_nan_callback` that checks for `nan`s only.