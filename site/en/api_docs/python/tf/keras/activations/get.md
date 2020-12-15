description: Returns function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.get" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.get

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/activations.py#L495-L537">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.get`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.get(
    identifier
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`identifier`
</td>
<td>
Function or string
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Function corresponding to the input string or input function.
</td>
</tr>

</table>



#### For example:



```
>>> tf.keras.activations.get('softmax')
 <function softmax at 0x1222a3d90>
>>> tf.keras.activations.get(tf.keras.activations.softmax)
 <function softmax at 0x1222a3d90>
>>> tf.keras.activations.get(None)
 <function linear at 0x1239596a8>
>>> tf.keras.activations.get(abs)
 <built-in function abs>
>>> tf.keras.activations.get('abcd')
Traceback (most recent call last):
...
ValueError: Unknown activation function:abcd
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
Input is an unknown function or string, i.e., the input does
not denote any defined function.
</td>
</tr>
</table>

