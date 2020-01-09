page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.reshape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L731-L814">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Reshapes a `SparseTensor` to represent values in a new dense shape.

### Aliases:

* `tf.compat.v1.sparse.reshape`
* `tf.compat.v1.sparse_reshape`
* `tf.compat.v2.sparse.reshape`


``` python
tf.sparse.reshape(
    sp_input,
    shape,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation has the same semantics as `reshape` on the represented dense
tensor.  The indices of non-empty values in `sp_input` are recomputed based
on the new dense shape, and a new `SparseTensor` is returned containing the
new indices and new shape.  The order of non-empty values in `sp_input` is
unchanged.

If one component of `shape` is the special value -1, the size of that
dimension is computed so that the total dense size remains constant.  At
most one component of `shape` can be -1.  The number of dense elements
implied by `shape` must be the same as the number of dense elements
originally represented by `sp_input`.

For example, if `sp_input` has shape `[2, 3, 6]` and `indices` / `values`:

    [0, 0, 0]: a
    [0, 0, 1]: b
    [0, 1, 0]: c
    [1, 0, 0]: d
    [1, 2, 3]: e

and `shape` is `[9, -1]`, then the output will be a `SparseTensor` of
shape `[9, 4]` and `indices` / `values`:

    [0, 0]: a
    [0, 1]: b
    [1, 2]: c
    [4, 2]: d
    [8, 1]: e

#### Args:


* <b>`sp_input`</b>: The input `SparseTensor`.
* <b>`shape`</b>: A 1-D (vector) int64 `Tensor` specifying the new dense shape of the
  represented `SparseTensor`.
* <b>`name`</b>: A name prefix for the returned tensors (optional)


#### Returns:

A `SparseTensor` with the same non-empty values but with indices calculated
by the new dense shape.



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.
* <b>`ValueError`</b>:  If argument `shape` requests a `SparseTensor` with a different
  number of elements than `sp_input`.
* <b>`ValueError`</b>:  If `shape` has more than one inferred (== -1) dimension.
