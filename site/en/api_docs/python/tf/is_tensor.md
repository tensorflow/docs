page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.is_tensor

Checks whether `x` is a tensor or "tensor-like".

### Aliases:

* `tf.compat.v1.is_tensor`
* `tf.compat.v2.is_tensor`
* `tf.contrib.framework.is_tensor`
* `tf.is_tensor`

``` python
tf.is_tensor(x)
```



Defined in [`python/framework/tensor_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/tensor_util.py).

<!-- Placeholder for "Used in" -->

If `is_tensor(x)` returns `True`, it is safe to assume that `x` is a tensor or
can be converted to a tensor using `ops.convert_to_tensor(x)`.

#### Args:


* <b>`x`</b>: A python object to check.


#### Returns:

`True` if `x` is a tensor or "tensor-like", `False` if not.
