page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.eye


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L180-L211">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a two-dimensional sparse tensor with ones along the diagonal.

### Aliases:

* `tf.compat.v1.sparse.eye`
* `tf.compat.v2.sparse.eye`


``` python
tf.sparse.eye(
    num_rows,
    num_columns=None,
    dtype=tf.dtypes.float32,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`num_rows`</b>: Non-negative integer or `int32` scalar `tensor` giving the number
  of rows in the resulting matrix.
* <b>`num_columns`</b>: Optional non-negative integer or `int32` scalar `tensor` giving
  the number of columns in the resulting matrix. Defaults to `num_rows`.
* <b>`dtype`</b>: The type of element in the resulting `Tensor`.
* <b>`name`</b>: A name for this `Op`. Defaults to "eye".


#### Returns:

A `SparseTensor` of shape [num_rows, num_columns] with ones along the
diagonal.
