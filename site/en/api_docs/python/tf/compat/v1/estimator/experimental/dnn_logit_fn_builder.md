description: Function builder for a dnn logit_fn.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.experimental.dnn_logit_fn_builder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.estimator.experimental.dnn_logit_fn_builder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/dnn.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Function builder for a dnn logit_fn.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.experimental.dnn_logit_fn_builder(
    units, hidden_units, feature_columns, activation_fn, dropout,
    input_layer_partitioner, batch_norm
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`units`
</td>
<td>
An int indicating the dimension of the logit layer.  In the MultiHead
case, this should be the sum of all component Heads' logit dimensions.
</td>
</tr><tr>
<td>
`hidden_units`
</td>
<td>
Iterable of integer number of hidden units per layer.
</td>
</tr><tr>
<td>
`feature_columns`
</td>
<td>
Iterable of `feature_column._FeatureColumn` model inputs.
</td>
</tr><tr>
<td>
`activation_fn`
</td>
<td>
Activation function applied to each layer.
</td>
</tr><tr>
<td>
`dropout`
</td>
<td>
When not `None`, the probability we will drop out a given
coordinate.
</td>
</tr><tr>
<td>
`input_layer_partitioner`
</td>
<td>
Partitioner for input layer.
</td>
</tr><tr>
<td>
`batch_norm`
</td>
<td>
Whether to use batch normalization after each hidden layer.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A logit_fn (see below).
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
If units is not an int.
</td>
</tr>
</table>

