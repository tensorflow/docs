description: Applies batch normalization on x given mean, var, beta and gamma.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.batch_normalization" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.batch_normalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L2783-L2840">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies batch normalization on x given mean, var, beta and gamma.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.batch_normalization`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.batch_normalization(
    x, mean, var, beta, gamma, axis=-1, epsilon=0.001
)
</code></pre>



<!-- Placeholder for "Used in" -->

I.e. returns:
`output = (x - mean) / (sqrt(var) + epsilon) * gamma + beta`

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
`mean`
</td>
<td>
Mean of batch.
</td>
</tr><tr>
<td>
`var`
</td>
<td>
Variance of batch.
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
`gamma`
</td>
<td>
Tensor by which to scale the input.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Integer, the axis that should be normalized.
(typically the features axis).
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
A tensor.
</td>
</tr>

</table>

