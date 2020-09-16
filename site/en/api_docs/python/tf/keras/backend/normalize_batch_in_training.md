description: Computes mean and std for batch then apply batch_normalization on batch.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.normalize_batch_in_training" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.normalize_batch_in_training

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L2583-L2610">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes mean and std for batch then apply batch_normalization on batch.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.normalize_batch_in_training`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.normalize_batch_in_training(
    x, gamma, beta, reduction_axes, epsilon=0.001
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Input tensor or variable.
</td>
</tr><tr>
<td>
`gamma`
</td>
<td>
Tensor by which to scale the input.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
Tensor with which to center the input.
</td>
</tr><tr>
<td>
`reduction_axes`
</td>
<td>
iterable of integers,
axes over which to normalize.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
Fuzz factor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple length of 3, `(normalized_tensor, mean, variance)`.
</td>
</tr>

</table>

