description: Function builder for a linear logit_fn.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.experimental.linear_logit_fn_builder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.estimator.experimental.linear_logit_fn_builder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/linear.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Function builder for a linear logit_fn.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.experimental.linear_logit_fn_builder(
    units, feature_columns, sparse_combiner='sum'
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
An int indicating the dimension of the logit layer.
</td>
</tr><tr>
<td>
`feature_columns`
</td>
<td>
An iterable containing all the feature columns used by the
model.
</td>
</tr><tr>
<td>
`sparse_combiner`
</td>
<td>
A string specifying how to reduce if a categorical column
is multivalent.  One of "mean", "sqrtn", and "sum".
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

