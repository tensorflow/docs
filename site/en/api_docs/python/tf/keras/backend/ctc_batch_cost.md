description: Runs CTC loss algorithm on each batch element.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.ctc_batch_cost" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.ctc_batch_cost

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L5992-L6022">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Runs CTC loss algorithm on each batch element.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.ctc_batch_cost`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.ctc_batch_cost(
    y_true, y_pred, input_length, label_length
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`y_true`
</td>
<td>
tensor `(samples, max_string_length)`
containing the truth labels.
</td>
</tr><tr>
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
tensor `(samples, 1)` containing the sequence length for
each batch item in `y_pred`.
</td>
</tr><tr>
<td>
`label_length`
</td>
<td>
tensor `(samples, 1)` containing the sequence length for
each batch item in `y_true`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tensor with shape (samples,1) containing the
CTC loss of each element.
</td>
</tr>

</table>

