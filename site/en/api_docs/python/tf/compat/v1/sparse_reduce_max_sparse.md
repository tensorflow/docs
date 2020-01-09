page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.sparse_reduce_max_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L1203-L1251">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

### Aliases:

* `tf.compat.v1.sparse.reduce_max_sparse`


``` python
tf.compat.v1.sparse_reduce_max_sparse(
    sp_input,
    axis=None,
    keepdims=None,
    reduction_axes=None,
    keep_dims=None
)
```



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(keep_dims)`. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

This Op takes a SparseTensor and is the sparse counterpart to
<a href="../../../tf/math/reduce_max"><code>tf.reduce_max()</code></a>.  In contrast to SparseReduceSum, this Op returns a
SparseTensor.

Note: A gradient is not defined for this function, so it can't be used
in training models that need gradient descent.

Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
`keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
`reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
with length 1.

If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
with a single element is returned.  Additionally, the axes can be negative,
which are interpreted according to the indexing rules in Python.

#### Args:


* <b>`sp_input`</b>: The SparseTensor to reduce. Should have numeric type.
* <b>`axis`</b>: The dimensions to reduce; list or scalar. If `None` (the
  default), reduces all dimensions.
* <b>`keepdims`</b>: If true, retain reduced dimensions with length 1.
* <b>`reduction_axes`</b>: Deprecated name of axis.
* <b>`keep_dims`</b>: Deprecated alias for `keepdims`.


#### Returns:

The reduced SparseTensor.
