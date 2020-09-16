description: Computes the eigen decomposition of one or more square matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Eig" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Eig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the eigen decomposition of one or more square matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Eig`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Eig(
    input, Tout, compute_v=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the eigenvalues and (optionally) right eigenvectors of each inner matrix in
`input` such that `input[..., :, :] = v[..., :, :] * diag(e[..., :])`. The eigenvalues
are sorted in non-decreasing order.

```python
# a is a tensor.
# e is a tensor of eigenvalues.
# v is a tensor of eigenvectors.
e, v = eig(a)
e = eig(a, compute_v=False)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `complex64`, `complex128`.
`Tensor` input of shape `[N, N]`.
</td>
</tr><tr>
<td>
`Tout`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.complex64, tf.complex128`.
</td>
</tr><tr>
<td>
`compute_v`
</td>
<td>
An optional `bool`. Defaults to `True`.
If `True` then eigenvectors will be computed and returned in `v`.
Otherwise, only the eigenvalues will be computed.
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
A tuple of `Tensor` objects (e, v).
</td>
</tr>
<tr>
<td>
`e`
</td>
<td>
A `Tensor` of type `Tout`.
</td>
</tr><tr>
<td>
`v`
</td>
<td>
A `Tensor` of type `Tout`.
</td>
</tr>
</table>

