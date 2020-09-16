description: Instantiates a placeholder tensor and returns it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.placeholder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.placeholder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L1141-L1234">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates a placeholder tensor and returns it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.placeholder`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.placeholder(
    shape=None, ndim=None, dtype=None, sparse=(False), name=None, ragged=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
Shape of the placeholder
(integer tuple, may include `None` entries).
</td>
</tr><tr>
<td>
`ndim`
</td>
<td>
Number of axes of the tensor.
At least one of {`shape`, `ndim`} must be specified.
If both are specified, `shape` is used.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Placeholder type.
</td>
</tr><tr>
<td>
`sparse`
</td>
<td>
Boolean, whether the placeholder should have a sparse type.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name string for the placeholder.
</td>
</tr><tr>
<td>
`ragged`
</td>
<td>
Boolean, whether the placeholder should have a ragged type.
In this case, values of 'None' in the 'shape' argument represent
ragged dimensions. For more information about RaggedTensors, see this
[guide](https://www.tensorflow.org/guide/ragged_tensors).
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
If called with eager execution
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If called with sparse = True and ragged = True.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tensor instance (with Keras metadata included).
</td>
</tr>

</table>



#### Examples:




```
>>> input_ph = tf.keras.backend.placeholder(shape=(2, 4, 5))
>>> input_ph
<tf.Tensor 'Placeholder_...' shape=(2, 4, 5) dtype=float32>
```