

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.convert_to_tensor

### `tf.convert_to_tensor`

``` python
convert_to_tensor(
    value,
    dtype=None,
    name=None,
    preferred_dtype=None
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/framework/ops.py).

See the guides: [Building Graphs > Utility functions](../../../api_guides/python/framework#Utility_functions), [Constants, Sequences, and Random Values](../../../api_guides/python/constant_op), [Control Flow](../../../api_guides/python/control_flow_ops), [Higher Order Functions](../../../api_guides/python/functional_ops), [Images](../../../api_guides/python/image), [Inputs and Readers](../../../api_guides/python/io_ops), [Math](../../../api_guides/python/math_ops), [Neural Network](../../../api_guides/python/nn), [Sparse Tensors](../../../api_guides/python/sparse_ops), [Strings](../../../api_guides/python/string_ops), [Tensor Handle Operations](../../../api_guides/python/session_ops), [Tensor Transformations](../../../api_guides/python/array_ops), [Variables](../../../api_guides/python/state_ops), [Wraps python functions](../../../api_guides/python/script_ops)

Converts the given `value` to a `Tensor`.

This function converts Python objects of various types to `Tensor`
objects. It accepts `Tensor` objects, numpy arrays, Python lists,
and Python scalars. For example:

```python
import numpy as np

def my_func(arg):
  arg = tf.convert_to_tensor(arg, dtype=tf.float32)
  return tf.matmul(arg, arg) + arg

# The following calls are equivalent.
value_1 = my_func(tf.constant([[1.0, 2.0], [3.0, 4.0]]))
value_2 = my_func([[1.0, 2.0], [3.0, 4.0]])
value_3 = my_func(np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32))
```

This function can be useful when composing a new operation in Python
(such as `my_func` in the example above). All standard Python op
constructors apply this function to each of their Tensor-valued
inputs, which allows those ops to accept numpy arrays, Python lists,
and scalars in addition to `Tensor` objects.

#### Args:

* <b>`value`</b>: An object whose type has a registered `Tensor` conversion function.
* <b>`dtype`</b>: Optional element type for the returned tensor. If missing, the
    type is inferred from the type of `value`.
* <b>`name`</b>: Optional name to use if a new `Tensor` is created.
* <b>`preferred_dtype`</b>: Optional element type for the returned tensor,
    used when dtype is None. In some cases, a caller may not have a
    dtype in mind when converting to a tensor, so preferred_dtype
    can be used as a soft preference.  If the conversion to
    `preferred_dtype` is not possible, this argument has no effect.


#### Returns:

  An `Output` based on `value`.


#### Raises:

* <b>`TypeError`</b>: If no conversion function is registered for `value`.
* <b>`RuntimeError`</b>: If a registered conversion function returns an invalid value.