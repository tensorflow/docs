description: Computes the singular value decompositions of one or more matrices.

robots: noindex

# tf.raw_ops.Svd

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the singular value decompositions of one or more matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Svd`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Svd(
    input, compute_uv=(True), full_matrices=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the SVD of each inner matrix in `input` such that
`input[..., :, :] = u[..., :, :] * diag(s[..., :, :]) * transpose(v[..., :, :])`

```python
# a is a tensor containing a batch of matrices.
# s is a tensor of singular values for each matrix.
# u is the tensor containing the left singular vectors for each matrix.
# v is the tensor containing the right singular vectors for each matrix.
s, u, v = svd(a)
s, _, _ = svd(a, compute_uv=False)
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
A tensor of shape `[..., M, N]` whose inner-most 2 dimensions
form matrices of size `[M, N]`. Let `P` be the minimum of `M` and `N`.
</td>
</tr><tr>
<td>
`compute_uv`
</td>
<td>
An optional `bool`. Defaults to `True`.
If true, left and right singular vectors will be
computed and returned in `u` and `v`, respectively.
If false, `u` and `v` are not set and should never referenced.
</td>
</tr><tr>
<td>
`full_matrices`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, compute full-sized `u` and `v`. If false
(the default), compute only the leading `P` singular vectors.
Ignored if `compute_uv` is `False`.
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
A tuple of `Tensor` objects (s, u, v).
</td>
</tr>
<tr>
<td>
`s`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`u`
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

