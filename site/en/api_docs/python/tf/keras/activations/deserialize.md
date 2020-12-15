description: Returns activation function given a string identifier.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.deserialize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.deserialize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/activations.py#L504-L536">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns activation function given a string identifier.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.deserialize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.deserialize(
    name, custom_objects=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
The name of the activation function.
</td>
</tr><tr>
<td>
`custom_objects`
</td>
<td>
Optional `{function_name: function_obj}`
dictionary listing user-provided activation functions.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Corresponding activation function.
</td>
</tr>

</table>



#### For example:



```
>>> tf.keras.activations.deserialize('linear')
 <function linear at 0x1239596a8>
>>> tf.keras.activations.deserialize('sigmoid')
 <function sigmoid at 0x123959510>
>>> tf.keras.activations.deserialize('abcd')
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
`Unknown activation function` if the input string does not
denote any defined Tensorflow activation function.
</td>
</tr>
</table>

