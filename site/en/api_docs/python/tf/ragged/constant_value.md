page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.constant_value

``` python
tf.ragged.constant_value(
    pylist,
    dtype=None,
    ragged_rank=None,
    inner_shape=None
)
```



Defined in [`tensorflow/python/ops/ragged/ragged_factory_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/ragged/ragged_factory_ops.py).

Constructs a RaggedTensorValue from a nested Python list.

Warning: This function returns a `RaggedTensorValue`, not a `RaggedTensor`.
If you wish to construct a constant `RaggedTensor`, use
[`ragged.constant(...)`](constant) instead.

Example:

```python
>>> ragged.constant_value([[1, 2], [3], [4, 5, 6]])
RaggedTensorValue(values=[1, 2, 3, 4, 5, 6], splits=[0, 2, 3, 6])
```

All scalar values in `pylist` must have the same nesting depth `K`, and the
returned `RaggedTensorValue` will have rank `K`.  If `pylist` contains no
scalar values, then `K` is one greater than the maximum depth of empty lists
in `pylist`.  All scalar values in `pylist` must be compatible with `dtype`.

#### Args:

* <b>`pylist`</b>: A nested `list` or `tuple`.  Any nested element that is not a `list`
    or `tuple` must be a scalar value compatible with `dtype`.
* <b>`dtype`</b>: `numpy.dtype`.  The type of elements for the returned `RaggedTensor`.
    If not specified, then a default is chosen based on the scalar values in
    `pylist`.
* <b>`ragged_rank`</b>: An integer specifying the ragged rank of the returned
    `RaggedTensorValue`.  Must be nonnegative and less than `K`. Defaults to
    `max(0, K - 1)` if `inner_shape` is not specified.  Defaults to `max(0, K
    - 1 - len(inner_shape))` if `inner_shape` is specified.
* <b>`inner_shape`</b>: A tuple of integers specifying the shape for individual inner
    values in the returned `RaggedTensorValue`.  Defaults to `()` if
    `ragged_rank` is not specified.  If `ragged_rank` is specified, then a
    default is chosen based on the contents of `pylist`.


#### Returns:

A `RaggedTensorValue` or `numpy.array` with rank `K` and the specified
`ragged_rank`, containing the values from `pylist`.


#### Raises:

* <b>`ValueError`</b>: If the scalar values in `pylist` have inconsistent nesting
    depth; or if ragged_rank or inner_shape are incompatible with `pylist`.