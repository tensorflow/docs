page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.inf_callback

``` python
tf.contrib.eager.inf_callback(
    op_type,
    inputs,
    attrs,
    outputs,
    op_name,
    action=_DEFAULT_CALLBACK_ACTION
)
```



Defined in [`tensorflow/python/eager/execution_callbacks.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/eager/execution_callbacks.py).

A specialization of `inf_nan_callback` that checks for `inf`s only.