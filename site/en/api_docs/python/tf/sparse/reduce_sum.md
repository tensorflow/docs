page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.reduce_sum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L1254-L1318">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the sum of elements across dimensions of a SparseTensor.

### Aliases:

* `tf.compat.v2.sparse.reduce_sum`


``` python
tf.sparse.reduce_sum(
    sp_input,
    axis=None,
    keepdims=None,
    output_is_sparse=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This Op takes a SparseTensor and is the sparse counterpart to
<a href="../../tf/math/reduce_sum"><code>tf.reduce_sum()</code></a>.  In particular, this Op also returns a dense `Tensor`
if `output_is_sparse` is `False`, or a `SparseTensor` if `output_is_sparse`
is `True`.

Note: if `output_is_sparse` is True, a gradient is not defined for this
function, so it can't be used in training models that need gradient descent.

Reduces `sp_input` along the dimensions given in `axis`.  Unless `keepdims` is
true, the rank of the tensor is reduced by 1 for each entry in `axis`. If
`keepdims` is true, the reduced dimensions are retained with length 1.

If `axis` has no entries, all dimensions are reduced, and a tensor
with a single element is returned.  Additionally, the axes can be negative,
similar to the indexing rules in Python.

#### For example:



```python
# 'x' represents [[1, ?, 1]
#                 [?, 1, ?]]
# where ? is implicitly-zero.
tf.sparse.reduce_sum(x) ==> 3
tf.sparse.reduce_sum(x, 0) ==> [1, 1, 1]
tf.sparse.reduce_sum(x, 1) ==> [2, 1]  # Can also use -1 as the axis.
tf.sparse.reduce_sum(x, 1, keepdims=True) ==> [[2], [1]]
tf.sparse.reduce_sum(x, [0, 1]) ==> 3
```

#### Args:


* <b>`sp_input`</b>: The SparseTensor to reduce. Should have numeric type.
* <b>`axis`</b>: The dimensions to reduce; list or scalar. If `None` (the
  default), reduces all dimensions.
* <b>`keepdims`</b>: If true, retain reduced dimensions with length 1.
* <b>`output_is_sparse`</b>: If true, returns a `SparseTensor` instead of a dense
  `Tensor` (the default).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The reduced Tensor or the reduced SparseTensor if `output_is_sparse` is
True.
