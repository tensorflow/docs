description: Turn a nD tensor into a 2D tensor with same 0th dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.batch_flatten" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.batch_flatten

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L3224-L3247">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Turn a nD tensor into a 2D tensor with same 0th dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.batch_flatten`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.batch_flatten(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->

In other words, it flattens each data samples of a batch.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A tensor or variable.
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



#### Examples:

Flattening a 3D tensor to 2D by collapsing the last dimension.


```
>>> x_batch = tf.keras.backend.ones(shape=(2, 3, 4, 5))
>>> x_batch_flatten = batch_flatten(x_batch)
>>> tf.keras.backend.int_shape(x_batch_flatten)
(2, 60)
```