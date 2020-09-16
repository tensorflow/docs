description: Normalizes along dimension axis using an L2 norm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.l2_normalize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.l2_normalize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/nn_impl.py#L620-L646">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Normalizes along dimension `axis` using an L2 norm.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.linalg.l2_normalize`, `tf.nn.l2_normalize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.l2_normalize(
    x, axis=None, epsilon=1e-12, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For a 1-D tensor with `axis = 0`, computes

    output = x / sqrt(max(sum(x**2), epsilon))

For `x` with more dimensions, independently normalizes each 1-D slice along
dimension `axis`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Dimension along which to normalize.  A scalar or a vector of
integers.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A lower bound value for the norm. Will use `sqrt(epsilon)` as the
divisor if `norm < sqrt(epsilon)`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with the same shape as `x`.
</td>
</tr>

</table>

