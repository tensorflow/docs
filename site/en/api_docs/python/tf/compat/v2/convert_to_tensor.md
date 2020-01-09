page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.convert_to_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L1187-L1242">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts the given `value` to a `Tensor`.

``` python
tf.compat.v2.convert_to_tensor(
    value,
    dtype=None,
    dtype_hint=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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

Note: This function diverges from default Numpy behavior for `float` and
  `string` types when `None` is present in a Python list or scalar. Rather
  than silently converting `None` values, an error will be thrown.

#### Args:


* <b>`value`</b>: An object whose type has a registered `Tensor` conversion function.
* <b>`dtype`</b>: Optional element type for the returned tensor. If missing, the type
  is inferred from the type of `value`.
* <b>`dtype_hint`</b>: Optional element type for the returned tensor, used when dtype
  is None. In some cases, a caller may not have a dtype in mind when
  converting to a tensor, so dtype_hint can be used as a soft preference.
  If the conversion to `dtype_hint` is not possible, this argument has no
  effect.
* <b>`name`</b>: Optional name to use if a new `Tensor` is created.


#### Returns:

A `Tensor` based on `value`.



#### Raises:


* <b>`TypeError`</b>: If no conversion function is registered for `value` to `dtype`.
* <b>`RuntimeError`</b>: If a registered conversion function returns an invalid value.
* <b>`ValueError`</b>: If the `value` is a tensor not of given `dtype` in graph mode.
