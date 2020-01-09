page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.from_dense


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L103-L123">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a dense tensor into a sparse tensor.

### Aliases:

* `tf.compat.v1.sparse.from_dense`
* `tf.compat.v2.sparse.from_dense`


``` python
tf.sparse.from_dense(
    tensor,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Only elements not equal to zero will be present in the result. The resulting
`SparseTensor` has the same dtype and shape as the input.

#### Args:


* <b>`tensor`</b>: A dense `Tensor` to be converted to a `SparseTensor`.
* <b>`name`</b>: Optional name for the op.


#### Returns:

The `SparseTensor`.
