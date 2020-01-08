page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse_reduce_max

``` python
tf.sparse_reduce_max(
    sp_input,
    axis=None,
    keepdims=None,
    reduction_axes=None,
    keep_dims=None
)
```



Defined in [`tensorflow/python/ops/sparse_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/sparse_ops.py).

Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

This Op takes a SparseTensor and is the sparse counterpart to
`tf.reduce_max()`.  In particular, this Op also returns a dense `Tensor`
instead of a sparse one.

Note: A gradient is not defined for this function, so it can't be used
in training models that need gradient descent.

Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
`keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
`reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
with length 1.

If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
with a single element is returned.  Additionally, the axes can be negative,
similar to the indexing rules in Python.

The values not defined in `sp_input` don't participate in the reduce max,
as opposed to be implicitly assumed 0 -- hence it can return negative values
for sparse `reduction_axes`. But, in case there are no values in
`reduction_axes`, it will reduce to 0. See second example below.

For example:

```python
# 'x' represents [[1, ?, 2]
#                 [?, 3, ?]]
# where ? is implicitly-zero.
tf.sparse_reduce_max(x) ==> 3
tf.sparse_reduce_max(x, 0) ==> [1, 3, 2]
tf.sparse_reduce_max(x, 1) ==> [2, 3]  # Can also use -1 as the axis.
tf.sparse_reduce_max(x, 1, keepdims=True) ==> [[2], [3]]
tf.sparse_reduce_max(x, [0, 1]) ==> 3

# 'y' represents [[-7, ?]
#                 [ 4, 3]
#                 [ ?, ?]
tf.sparse_reduce_max(x, 1) ==> [-7, 4, 0]
```

#### Args:

* <b>`sp_input`</b>: The SparseTensor to reduce. Should have numeric type.
* <b>`axis`</b>: The dimensions to reduce; list or scalar. If `None` (the
    default), reduces all dimensions.
* <b>`keepdims`</b>: If true, retain reduced dimensions with length 1.
* <b>`reduction_axes`</b>: Deprecated name of axis.
* <b>`keep_dims`</b>:  Deprecated alias for `keepdims`.


#### Returns:

The reduced Tensor.