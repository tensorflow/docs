page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse_to_dense


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sparse_ops.py#L1010-L1066">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a sparse representation into a dense tensor. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/sparse_to_dense"><code>tf.compat.v1.sparse_to_dense</code></a>


``` python
tf.sparse_to_dense(
    sparse_indices,
    output_shape,
    sparse_values,
    default_value=0,
    validate_indices=True,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Create a <a href="../tf/sparse/SparseTensor"><code>tf.sparse.SparseTensor</code></a> and use <a href="../tf/sparse/to_dense"><code>tf.sparse.to_dense</code></a> instead.

Builds an array `dense` with shape `output_shape` such that

```python
# If sparse_indices is scalar
dense[i] = (i == sparse_indices ? sparse_values : default_value)

# If sparse_indices is a vector, then for each i
dense[sparse_indices[i]] = sparse_values[i]

# If sparse_indices is an n by d matrix, then for each i in [0, n)
dense[sparse_indices[i][0], ..., sparse_indices[i][d-1]] = sparse_values[i]
```

All other values in `dense` are set to `default_value`.  If `sparse_values`
is a scalar, all sparse indices are set to this single value.

Indices should be sorted in lexicographic order, and indices must not
contain any repeats. If `validate_indices` is True, these properties
are checked during execution.

#### Args:


* <b>`sparse_indices`</b>: A 0-D, 1-D, or 2-D `Tensor` of type `int32` or `int64`.
  `sparse_indices[i]` contains the complete index where `sparse_values[i]`
  will be placed.
* <b>`output_shape`</b>: A 1-D `Tensor` of the same type as `sparse_indices`.  Shape
  of the dense output tensor.
* <b>`sparse_values`</b>: A 0-D or 1-D `Tensor`.  Values corresponding to each row of
  `sparse_indices`, or a scalar value to be used for all sparse indices.
* <b>`default_value`</b>: A 0-D `Tensor` of the same type as `sparse_values`.  Value
  to set for indices not specified in `sparse_indices`.  Defaults to zero.
* <b>`validate_indices`</b>: A boolean value.  If True, indices are checked to make
  sure they are sorted in lexicographic order and that there are no repeats.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

Dense `Tensor` of shape `output_shape`.  Has the same type as
`sparse_values`.
