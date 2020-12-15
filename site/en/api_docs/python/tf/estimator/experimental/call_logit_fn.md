description: Calls logit_fn (experimental).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.experimental.call_logit_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.estimator.experimental.call_logit_fn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/model_fn.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls logit_fn (experimental).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.experimental.call_logit_fn`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.experimental.call_logit_fn(
    logit_fn, features, mode, params, config
)
</code></pre>



<!-- Placeholder for "Used in" -->

THIS FUNCTION IS EXPERIMENTAL. Keras layers/models are the recommended APIs
for logit and model composition.

A utility function that calls the provided logit_fn with the relevant subset
of provided arguments. Similar to tf.estimator._call_model_fn().

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`logit_fn`
</td>
<td>
A logit_fn as defined above.
</td>
</tr><tr>
<td>
`features`
</td>
<td>
The features dict.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
TRAIN / EVAL / PREDICT ModeKeys.
</td>
</tr><tr>
<td>
`params`
</td>
<td>
The hyperparameter dict.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
The configuration object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A logit Tensor, the output of logit_fn.
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
if logit_fn does not return a Tensor or a dictionary mapping
strings to Tensors.
</td>
</tr>
</table>

