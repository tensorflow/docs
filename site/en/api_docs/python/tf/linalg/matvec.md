description: Multiplies matrix a by vector b, producing a * b.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.matvec" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.matvec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L3258-L3355">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Multiplies matrix `a` by vector `b`, producing `a` * `b`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.matvec`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.matvec(
    a, b, transpose_a=(False), adjoint_a=(False), a_is_sparse=(False),
    b_is_sparse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The matrix `a` must, following any transpositions, be a tensor of rank >= 2,
with `shape(a)[-1] == shape(b)[-1]`, and `shape(a)[:-2]` able to broadcast
with `shape(b)[:-1]`.

Both `a` and `b` must be of the same type. The supported types are:
`float16`, `float32`, `float64`, `int32`, `complex64`, `complex128`.

Matrix `a` can be transposed or adjointed (conjugated and transposed) on
the fly by setting one of the corresponding flag to `True`. These are `False`
by default.

If one or both of the inputs contain a lot of zeros, a more efficient
multiplication algorithm can be used by setting the corresponding
`a_is_sparse` or `b_is_sparse` flag to `True`. These are `False` by default.
This optimization is only available for plain matrices/vectors (rank-2/1
tensors) with datatypes `bfloat16` or `float32`.

#### For example:



```python
# 2-D tensor `a`
# [[1, 2, 3],
#  [4, 5, 6]]
a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])

# 1-D tensor `b`
# [7, 9, 11]
b = tf.constant([7, 9, 11], shape=[3])

# `a` * `b`
# [ 58,  64]
c = tf.linalg.matvec(a, b)


# 3-D tensor `a`
# [[[ 1,  2,  3],
#   [ 4,  5,  6]],
#  [[ 7,  8,  9],
#   [10, 11, 12]]]
a = tf.constant(np.arange(1, 13, dtype=np.int32),
                shape=[2, 2, 3])

# 2-D tensor `b`
# [[13, 14, 15],
#  [16, 17, 18]]
b = tf.constant(np.arange(13, 19, dtype=np.int32),
                shape=[2, 3])

# `a` * `b`
# [[ 86, 212],
#  [410, 563]]
c = tf.linalg.matvec(a, b)
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
`Tensor` of type `float16`, `float32`, `float64`, `int32`, `complex64`,
`complex128` and rank > 1.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
`Tensor` with same type as `a` and compatible dimensions.
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
`adjoint_a`
</td>
<td>
If `True`, `a` is conjugated and transposed before
multiplication.
</td>
</tr><tr>
<td>
`a_is_sparse`
</td>
<td>
If `True`, `a` is treated as a sparse matrix.
</td>
</tr><tr>
<td>
`b_is_sparse`
</td>
<td>
If `True`, `b` is treated as a sparse matrix.
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
A `Tensor` of the same type as `a` and `b` where each inner-most vector is
the product of the corresponding matrices in `a` and vectors in `b`, e.g. if
all transpose or adjoint attributes are `False`:

`output`[..., i] = sum_k (`a`[..., i, k] * `b`[..., k]), for all indices i.
</td>
</tr>
<tr>
<td>
`Note`
</td>
<td>
This is matrix-vector product, not element-wise product.
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
If transpose_a and adjoint_a are both set to True.
</td>
</tr>
</table>

