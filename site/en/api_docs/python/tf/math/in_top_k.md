description: Says whether the targets are in the top K predictions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.in_top_k" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.in_top_k

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L5740-L5743">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Says whether the targets are in the top `K` predictions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.nn.in_top_k`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.in_top_k(
    targets, predictions, k, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This outputs a `batch_size` bool array, an entry `out[i]` is `true` if the
prediction for the target class is finite (not inf, -inf, or nan) and among
the top `k` predictions among all predictions for example `i`. Note that the
behavior of `InTopK` differs from the `TopK` op in its handling of ties; if
multiple classes have the same prediction value and straddle the top-`k`
boundary, all of those classes are considered to be in the top `k`.

More formally, let

  \\(predictions_i\\) be the predictions for all classes for example `i`,
  \\(targets_i\\) be the target class for example `i`,
  \\(out_i\\) be the output for example `i`,

$$out_i = predictions_{i, targets_i} \in TopKIncludingTies(predictions_i)$$

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`predictions`
</td>
<td>
A `Tensor` of type `float32`.
A `batch_size` x `classes` tensor.
</td>
</tr><tr>
<td>
`targets`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A `batch_size` vector of class ids.
</td>
</tr><tr>
<td>
`k`
</td>
<td>
An `int`. Number of top elements to look at for computing precision.
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
A `Tensor` of type `bool`. Computed Precision at `k` as a `bool Tensor`.
</td>
</tr>

</table>

