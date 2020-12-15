description: Solve systems of linear equations with upper or lower triangular matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.triangular_solve" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.triangular_solve

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg_ops.py#L84-L144">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Solve systems of linear equations with upper or lower triangular matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.triangular_solve`, `tf.compat.v1.matrix_triangular_solve`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.triangular_solve(
    matrix, rhs, lower=(True), adjoint=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`matrix` is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form
square matrices. If `lower` is `True` then the strictly upper triangular part
of each inner-most matrix is assumed to be zero and not accessed. If `lower`
is `False` then the strictly lower triangular part of each inner-most matrix
is assumed to be zero and not accessed. `rhs` is a tensor of shape
`[..., M, N]`.

The output is a tensor of shape `[..., M, N]`. If `adjoint` is `True` then the
innermost matrices in output satisfy matrix equations `
sum_k matrix[..., i, k] * output[..., k, j] = rhs[..., i, j]`.
If `adjoint` is `False` then the
innermost matrices in output satisfy matrix equations
`sum_k adjoint(matrix[..., i, k]) * output[..., k, j] = rhs[..., i, j]`.

#### Example:



```
>>> a = tf.constant([[3,  0,  0,  0],
...   [2,  1,  0,  0],
...   [1,  0,  1,  0],
...   [1,  1,  1,  1]], dtype=tf.float32)
```

```
>>> b = tf.constant([[4], [2], [4], [2]], dtype=tf.float32)
>>> x = tf.linalg.triangular_solve(a, b, lower=True)
>>> x
<tf.Tensor: shape=(4, 1), dtype=float32, numpy=
array([[ 1.3333334 ],
       [-0.66666675],
       [ 2.6666665 ],
       [-1.3333331 ]], dtype=float32)>
>>> tf.matmul(a, x)
<tf.Tensor: shape=(4, 1), dtype=float32, numpy=
array([[4.],
       [2.],
       [4.],
       [2.]], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`matrix`
</td>
<td>
A `Tensor`. Must be one of the following types: `float64`,
`float32`, `half`, `complex64`, `complex128`. Shape is `[..., M, M]`.
</td>
</tr><tr>
<td>
`rhs`
</td>
<td>
A `Tensor`. Must have the same type as `matrix`. Shape is `[..., M,
N]`.
</td>
</tr><tr>
<td>
`lower`
</td>
<td>
An optional `bool`. Defaults to `True`. Boolean indicating whether
the innermost matrices in matrix are lower or upper triangular.
</td>
</tr><tr>
<td>
`adjoint`
</td>
<td>
An optional `bool`. Defaults to `False`. Boolean indicating whether
to solve with matrix or its (block-wise) adjoint.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as matrix, and shape is `[..., M, N]`.
</td>
</tr>

</table>

