description: Functional interface to the Dot layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.dot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.layers.dot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/merge.py#L934-L951">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functional interface to the `Dot` layer.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.dot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.dot(
    inputs, axes, normalize=(False), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of input tensors (at least 2).
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
Integer or tuple of integers,
axis or axes along which to take the dot product.
</td>
</tr><tr>
<td>
`normalize`
</td>
<td>
Whether to L2-normalize samples along the
dot product axis before taking the dot product.
If set to True, then the output of the dot product
is the cosine proximity between the two samples.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Standard layer keyword arguments.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor, the dot product of the samples from the inputs.
</td>
</tr>

</table>

