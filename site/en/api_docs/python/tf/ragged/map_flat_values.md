page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.map_flat_values

Applies `op` to the values of one or more RaggedTensors.

### Aliases:

* `tf.compat.v1.ragged.map_flat_values`
* `tf.compat.v2.ragged.map_flat_values`
* `tf.ragged.map_flat_values`

``` python
tf.ragged.map_flat_values(
    op,
    *args,
    **kwargs
)
```



Defined in [`python/ops/ragged/ragged_functional_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/ragged/ragged_functional_ops.py).

<!-- Placeholder for "Used in" -->

Replaces any `RaggedTensor` in `args` or `kwargs` with its `flat_values`
tensor, and then calls `op`.  Returns a `RaggedTensor` that is constructed
from the input `RaggedTensor`s' `nested_row_splits` and the value returned by
the `op`.

If the input arguments contain multiple `RaggedTensor`s, then they must have
identical `nested_row_splits`.

#### Examples:



```python
>>> rt = ragged.constant([[1, 2, 3], [], [4, 5], [6]])
>>> ragged.map_flat_values(tf.ones_like, rt).eval().tolist()
[[1, 1, 1], [], [1, 1], [1]]
>>> ragged.map_flat_values(tf.multiply, rt, rt).eval().tolist()
[[1, 4, 9], [], [16, 25], [36]]
>>> ragged.map_flat_values(tf.add, rt, 5).eval().tolist()
[[6, 7, 8], [], [9, 10], [11]]
```

#### Args:


* <b>`op`</b>: The operation that should be applied to the RaggedTensor `flat_values`.
  `op` is typically an element-wise operation (such as math_ops.add), but
  any operation that preserves the size of the outermost dimension can be
  used.  I.e., `shape[0]` of the value returned by `op` must match
  `shape[0]` of the `RaggedTensor`s' `flat_values` tensors.
* <b>`*args`</b>: Arguments for `op`.
* <b>`**kwargs`</b>: Keyword arguments for `op`.


#### Returns:

A `RaggedTensor` whose `ragged_rank` matches the `ragged_rank` of all
input `RaggedTensor`s.


#### Raises:


* <b>`ValueError`</b>: If args contains no `RaggedTensors`, or if the `nested_splits`
  of the input `RaggedTensor`s are not identical.