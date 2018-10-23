

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.py_func

``` python
tf.contrib.eager.py_func(
    func,
    inp,
    Tout,
    name=None
)
```



Defined in [`tensorflow/python/ops/script_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/ops/script_ops.py).

Wraps a python function into a TensorFlow op.

When the returned op is executed, `func` is invoked with eager execution
enabled. Inputs are Tensor objects and func must return None or objects
that may be converted to Tensor objects.

This function has the same limitations as `py_func` with respect to
serialization and distribution.

#### Args:

* <b>`func`</b>: A Python function which accepts a list of `Tensor` objects
    having element types that match the corresponding `tf.Tensor` objects
    in `inp` and returns a list of `Tensor` objects (or a single
    `Tensor`, or `None`) having element types that match the
    corresponding values in `Tout`.
* <b>`inp`</b>: A list of `Tensor` objects.
* <b>`Tout`</b>: A list or tuple of tensorflow data types or a single tensorflow data
    type if there is only one, indicating what `func` returns; an empty list
    if no value is returned (i.e., if the return value is `None`).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `Tensor` or a single `Tensor` which `func` computes; an empty list
if `func` returns None.