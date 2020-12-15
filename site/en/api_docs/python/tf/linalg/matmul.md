description: Multiplies matrix a by matrix b, producing a * b.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.matmul" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.matmul

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L3123-L3315">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.matmul`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.matmul`, `tf.compat.v1.matmul`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.matmul(
    a, b, transpose_a=(False), transpose_b=(False), adjoint_a=(False),
    adjoint_b=(False), a_is_sparse=(False), b_is_sparse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The inputs must, following any transpositions, be tensors of rank >= 2
where the inner 2 dimensions specify valid matrix multiplication dimensions,
and any further outer dimensions specify matching batch size.

Both matrices must be of the same type. The supported types are:
`float16`, `float32`, `float64`, `int32`, `complex64`, `complex128`.

Either matrix can be transposed or adjointed (conjugated and transposed) on
the fly by setting one of the corresponding flag to `True`. These are `False`
by default.

If one or both of the matrices contain a lot of zeros, a more efficient
multiplication algorithm can be used by setting the corresponding
`a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default.
This optimization is only available for plain matrices (rank-2 tensors) with
datatypes `bfloat16` or `float32`.

A simple 2-D tensor matrix multiplication:

```
>>> a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
>>> a  # 2-D tensor
<tf.Tensor: shape=(2, 3), dtype=int32, numpy=
array([[1, 2, 3],
       [4, 5, 6]], dtype=int32)>
>>> b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
>>> b  # 2-D tensor
<tf.Tensor: shape=(3, 2), dtype=int32, numpy=
array([[ 7,  8],
       [ 9, 10],
       [11, 12]], dtype=int32)>
>>> c = tf.matmul(a, b)
>>> c  # `a` * `b`
<tf.Tensor: shape=(2, 2), dtype=int32, numpy=
array([[ 58,  64],
       [139, 154]], dtype=int32)>
```

A batch matrix multiplication with batch shape [2]:

```
>>> a = tf.constant(np.arange(1, 13, dtype=np.int32), shape=[2, 2, 3])
>>> a  # 3-D tensor
<tf.Tensor: shape=(2, 2, 3), dtype=int32, numpy=
array([[[ 1,  2,  3],
        [ 4,  5,  6]],
       [[ 7,  8,  9],
        [10, 11, 12]]], dtype=int32)>
>>> b = tf.constant(np.arange(13, 25, dtype=np.int32), shape=[2, 3, 2])
>>> b  # 3-D tensor
<tf.Tensor: shape=(2, 3, 2), dtype=int32, numpy=
array([[[13, 14],
        [15, 16],
        [17, 18]],
       [[19, 20],
        [21, 22],
        [23, 24]]], dtype=int32)>
>>> c = tf.matmul(a, b)
>>> c  # `a` * `b`
<tf.Tensor: shape=(2, 2, 2), dtype=int32, numpy=
array([[[ 94, 100],
        [229, 244]],
       [[508, 532],
        [697, 730]]], dtype=int32)>
```

Since python >= 3.5 the @ operator is supported
(see [PEP 465](https://www.python.org/dev/peps/pep-0465/)). In TensorFlow,
it simply calls the <a href="../../tf/linalg/matmul.md"><code>tf.matmul()</code></a> function, so the following lines are
equivalent:

```
>>> d = a @ b @ [[10], [11]]
>>> d = tf.matmul(tf.matmul(a, b), [[10], [11]])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type `float16`, `float32`, `float64`, `int32`,
`complex64`, `complex128` and rank > 1.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> with same type and rank as `a`.
</td>
</tr><tr>
<td>
`transpose_a`
</td>
<td>
If `True`, `a` is transposed before multiplication.
</td>
</tr><tr>
<td>
`transpose_b`
</td>
<td>
If `True`, `b` is transposed before multiplication.
</td>
</tr><tr>
<td>
`adjoint_a`
</td>
<td>
If `True`, `a` is conjugated and transposed before
multiplication.
</td>
</tr><tr>
<td>
`adjoint_b`
</td>
<td>
If `True`, `b` is conjugated and transposed before
multiplication.
</td>
</tr><tr>
<td>
`a_is_sparse`
</td>
<td>
If `True`, `a` is treated as a sparse matrix. Notice, this
**does not support <a href="../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>**, it just makes optimizations
that assume most values in `a` are zero.
See <a href="../../tf/sparse/sparse_dense_matmul.md"><code>tf.sparse.sparse_dense_matmul</code></a>
for some support for <a href="../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> multiplication.
</td>
</tr><tr>
<td>
`b_is_sparse`
</td>
<td>
If `True`, `b` is treated as a sparse matrix. Notice, this
**does not support <a href="../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>**, it just makes optimizations
that assume most values in `a` are zero.
See <a href="../../tf/sparse/sparse_dense_matmul.md"><code>tf.sparse.sparse_dense_matmul</code></a>
for some support for <a href="../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> multiplication.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of the same type as `a` and `b` where each inner-most matrix
is the product of the corresponding matrices in `a` and `b`, e.g. if all
transpose or adjoint attributes are `False`:

`output[..., i, j] = sum_k (a[..., i, k] * b[..., k, j])`,
for all indices `i`, `j`.
</td>
</tr>
<tr>
<td>
`Note`
</td>
<td>
This is matrix product, not element-wise product.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `transpose_a` and `adjoint_a`, or `transpose_b` and
`adjoint_b` are both set to `True`.
</td>
</tr>
</table>

