description: Computes the eigen decomposition of one or more square self-adjoint matrices.

robots: noindex

# tf.raw_ops.SelfAdjointEigV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the eigen decomposition of one or more square self-adjoint matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SelfAdjointEigV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SelfAdjointEigV2(
    input, compute_v=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the eigenvalues and (optionally) eigenvectors of each inner matrix in
`input` such that `input[..., :, :] = v[..., :, :] * diag(e[..., :])`. The eigenvalues
are sorted in non-decreasing order.

```python
# a is a tensor.
# e is a tensor of eigenvalues.
# v is a tensor of eigenvectors.
e, v = self_adjoint_eig(a)
e = self_adjoint_eig(a, compute_v=False)
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
A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
`Tensor` input of shape `[N, N]`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`v`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr>
</table>

