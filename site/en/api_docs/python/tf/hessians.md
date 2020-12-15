description: Constructs the Hessian of sum of ys with respect to x in xs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.hessians" />
<meta itemprop="path" content="Stable" />
</div>

# tf.hessians

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/gradients_impl.py#L443-L479">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Constructs the Hessian of sum of `ys` with respect to `x` in `xs`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.hessians(
    ys, xs, gate_gradients=(False), aggregation_method=None, name='hessians'
)
</code></pre>



<!-- Placeholder for "Used in" -->

`hessians()` adds ops to the graph to output the Hessian matrix of `ys`
with respect to `xs`.  It returns a list of `Tensor` of length `len(xs)`
where each tensor is the Hessian of `sum(ys)`.

The Hessian is a matrix of second-order partial derivatives of a scalar
tensor (see https://en.wikipedia.org/wiki/Hessian_matrix for more details).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ys`
</td>
<td>
A `Tensor` or list of tensors to be differentiated.
</td>
</tr><tr>
<td>
`xs`
</td>
<td>
A `Tensor` or list of tensors to be used for differentiation.
</td>
</tr><tr>
<td>
`gate_gradients`
</td>
<td>
See `gradients()` documentation for details.
</td>
</tr><tr>
<td>
`aggregation_method`
</td>
<td>
See `gradients()` documentation for details.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name to use for grouping all the gradient ops together.
defaults to 'hessians'.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of Hessian matrices of `sum(ys)` for each `x` in `xs`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`LookupError`
</td>
<td>
if one of the operations between `xs` and `ys` does not
have a registered gradient function.
</td>
</tr>
</table>

