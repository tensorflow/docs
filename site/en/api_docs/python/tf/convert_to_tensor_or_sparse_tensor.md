page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.convert_to_tensor_or_sparse_tensor

Converts value to a `SparseTensor` or `Tensor`.

### Aliases:

* `tf.compat.v1.convert_to_tensor_or_sparse_tensor`
* `tf.contrib.framework.convert_to_tensor_or_sparse_tensor`
* `tf.convert_to_tensor_or_sparse_tensor`

``` python
tf.convert_to_tensor_or_sparse_tensor(
    value,
    dtype=None,
    name=None
)
```



Defined in [`python/framework/sparse_tensor.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/sparse_tensor.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`value`</b>: A `SparseTensor`, `SparseTensorValue`, or an object whose type has a
  registered `Tensor` conversion function.
* <b>`dtype`</b>: Optional element type for the returned tensor. If missing, the type
  is inferred from the type of `value`.
* <b>`name`</b>: Optional name to use if a new `Tensor` is created.


#### Returns:

A `SparseTensor` or `Tensor` based on `value`.



#### Raises:


* <b>`RuntimeError`</b>: If result type is incompatible with `dtype`.