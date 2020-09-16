description: Computes the eigen decomposition of a batch of matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.eig" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.eig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/linalg_ops.py#L378-L406">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the eigen decomposition of a batch of matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.eig`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.eig(
    tensor, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The eigenvalues
and eigenvectors for a non-Hermitian matrix in general are complex. The
eigenvectors are not guaranteed to be linearly independent.

Computes the eigenvalues and right eigenvectors of the innermost
N-by-N matrices in `tensor` such that
`tensor[...,:,:] * v[..., :,i] = e[..., i] * v[...,:,i]`, for i=0...N-1.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
`Tensor` of shape `[..., N, N]`. Only the lower triangular part of
each inner inner matrix is referenced.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
string, optional name of the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`e`
</td>
<td>
Eigenvalues. Shape is `[..., N]`. Sorted in non-decreasing order.
</td>
</tr><tr>
<td>
`v`
</td>
<td>
Eigenvectors. Shape is `[..., N, N]`. The columns of the inner most
matrices contain eigenvectors of the corresponding matrices in `tensor`
</td>
</tr>
</table>

