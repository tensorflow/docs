description: Computes the eigenvalues of one or more matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.eigvals" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.eigvals

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/linalg_ops.py#L409-L433">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the eigenvalues of one or more matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.eigvals`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.eigvals(
    tensor, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: If your program backpropagates through this function, you should replace
it with a call to tf.linalg.eig (possibly ignoring the second output) to
avoid computing the eigen decomposition twice. This is because the
eigenvectors are used to compute the gradient w.r.t. the eigenvalues. See
_SelfAdjointEigV2Grad in linalg_grad.py.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
`Tensor` of shape `[..., N, N]`.
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
Eigenvalues. Shape is `[..., N]`. The vector `e[..., :]` contains the `N`
eigenvalues of `tensor[..., :, :]`.
</td>
</tr>
</table>

