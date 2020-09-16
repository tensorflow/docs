description: Categorical crossentropy with integer targets.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.sparse_categorical_crossentropy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.sparse_categorical_crossentropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L4586-L4664">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Categorical crossentropy with integer targets.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.sparse_categorical_crossentropy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.sparse_categorical_crossentropy(
    target, output, from_logits=(False), axis=-1
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`target`
</td>
<td>
An integer tensor.
</td>
</tr><tr>
<td>
`output`
</td>
<td>
A tensor resulting from a softmax
(unless `from_logits` is True, in which
case `output` is expected to be the logits).
</td>
</tr><tr>
<td>
`from_logits`
</td>
<td>
Boolean, whether `output` is the
result of a softmax, or is a tensor of logits.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Int specifying the channels axis. `axis=-1` corresponds to data
format `channels_last', and `axis=1` corresponds to data format
`channels_first`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Output tensor.
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
if `axis` is neither -1 nor one of the axes of `output`.
</td>
</tr>
</table>

