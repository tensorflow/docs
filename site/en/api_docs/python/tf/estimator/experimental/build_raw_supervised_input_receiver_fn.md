description: Build a supervised_input_receiver_fn for raw features and labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.experimental.build_raw_supervised_input_receiver_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.estimator.experimental.build_raw_supervised_input_receiver_fn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/export/export.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Build a supervised_input_receiver_fn for raw features and labels.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.experimental.build_raw_supervised_input_receiver_fn`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.experimental.build_raw_supervised_input_receiver_fn(
    features, labels, default_batch_size=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function wraps tensor placeholders in a supervised_receiver_fn
with the expectation that the features and labels appear precisely as
the model_fn expects them. Features and labels can therefore be dicts of
tensors, or raw tensors.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`
</td>
<td>
a dict of string to `Tensor` or `Tensor`.
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
a dict of string to `Tensor` or `Tensor`.
</td>
</tr><tr>
<td>
`default_batch_size`
</td>
<td>
the number of query examples expected per batch. Leave
unset for variable batch size (recommended).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A supervised_input_receiver_fn.
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
if features and labels have overlapping keys.
</td>
</tr>
</table>

