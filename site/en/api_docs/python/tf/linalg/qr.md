description: Computes the QR decompositions of one or more matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.qr" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.qr

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the QR decompositions of one or more matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.qr`, `tf.compat.v1.qr`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.qr(
    input, full_matrices=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the QR decomposition of each inner matrix in `tensor` such that
`tensor[..., :, :] = q[..., :, :] * r[..., :,:])`

Currently, the gradient for the QR decomposition is well-defined only when
the first `P` columns of the inner matrix are linearly independent, where
`P` is the minimum of `M` and `N`, the 2 inner-most dimmensions of `tensor`.

```python
# a is a tensor.
# q is a tensor of orthonormal matrices.
# r is a tensor of upper triangular matrices.
q, r = qr(a)
q_full, r_full = qr(a, full_matrices=True)
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
`full_matrices`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, compute full-sized `q` and `r`. If false
(the default), compute only the leading `P` columns of `q`.
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
A tuple of `Tensor` objects (q, r).
</td>
</tr>
<tr>
<td>
`q`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`r`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr>
</table>

