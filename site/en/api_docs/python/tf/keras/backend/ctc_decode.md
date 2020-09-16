description: Decodes the output of a softmax.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.ctc_decode" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.ctc_decode

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L6025-L6075">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Decodes the output of a softmax.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.ctc_decode`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.ctc_decode(
    y_pred, input_length, greedy=(True), beam_width=100, top_paths=1
)
</code></pre>



<!-- Placeholder for "Used in" -->

Can use either greedy search (also known as best path)
or a constrained dictionary search.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`y_pred`
</td>
<td>
tensor `(samples, time_steps, num_categories)`
containing the prediction, or output of the softmax.
</td>
</tr><tr>
<td>
`input_length`
</td>
<td>
tensor `(samples, )` containing the sequence length for
each batch item in `y_pred`.
</td>
</tr><tr>
<td>
`greedy`
</td>
<td>
perform much faster best-path search if `true`.
This does not use a dictionary.
</td>
</tr><tr>
<td>
`beam_width`
</td>
<td>
if `greedy` is `false`: a beam search decoder will be used
with a beam of this width.
</td>
</tr><tr>
<td>
`top_paths`
</td>
<td>
if `greedy` is `false`,
how many of the most probable paths will be returned.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`Tuple`
</td>
<td>
List: if `greedy` is `true`, returns a list of one element that
contains the decoded sequence.
If `false`, returns the `top_paths` most probable
decoded sequences.
Each decoded sequence has shape (samples, time_steps).
Important: blank labels are returned as `-1`.
Tensor `(top_paths, )` that contains
the log probability of each decoded sequence.
</td>
</tr>
</table>

