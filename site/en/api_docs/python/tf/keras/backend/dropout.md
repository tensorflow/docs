description: Sets entries in x to zero at random, while scaling the entire tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.dropout" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.dropout

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L4751-L4768">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sets entries in `x` to zero at random, while scaling the entire tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.dropout`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.dropout(
    x, level, noise_shape=None, seed=None
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
tensor
</td>
</tr><tr>
<td>
`level`
</td>
<td>
fraction of the entries in the tensor
that will be set to 0.
</td>
</tr><tr>
<td>
`noise_shape`
</td>
<td>
shape for randomly generated keep/drop flags,
must be broadcastable to the shape of `x`
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
random seed to ensure determinism.
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

