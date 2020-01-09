page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.maximum


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L2448-L2483">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the element-wise max of two SparseTensors.

### Aliases:

* `tf.compat.v1.sparse.maximum`
* `tf.compat.v1.sparse_maximum`
* `tf.compat.v2.sparse.maximum`


``` python
tf.sparse.maximum(
    sp_a,
    sp_b,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Assumes the two SparseTensors have the same shape, i.e., no broadcasting.
Example:

```python
sp_zero = sparse_tensor.SparseTensor([[0]], [0], [7])
sp_one = sparse_tensor.SparseTensor([[1]], [1], [7])
res = tf.sparse.maximum(sp_zero, sp_one).eval()
# "res" should be equal to SparseTensor([[0], [1]], [0, 1], [7]).
```

#### Args:


* <b>`sp_a`</b>: a `SparseTensor` operand whose dtype is real, and indices
  lexicographically ordered.
* <b>`sp_b`</b>: the other `SparseTensor` operand with the same requirements (and the
  same shape).
* <b>`name`</b>: optional name of the operation.

#### Returns:


* <b>`output`</b>: the output SparseTensor.
