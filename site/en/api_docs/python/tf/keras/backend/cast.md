description: Casts a tensor to a different dtype and returns it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.cast" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.cast

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L1555-L1580">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Casts a tensor to a different dtype and returns it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.cast`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.cast(
    x, dtype
)
</code></pre>



<!-- Placeholder for "Used in" -->

You can cast a Keras variable but it still returns a Keras tensor.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Keras tensor (or variable).
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
String, either (`'float16'`, `'float32'`, or `'float64'`).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Keras tensor with dtype `dtype`.
</td>
</tr>

</table>



#### Examples:

Cast a float32 variable to a float64 tensor


```
>>> input = tf.keras.backend.ones(shape=(1,3))
>>> print(input)
<tf.Variable 'Variable:0' shape=(1, 3) dtype=float32,
numpy=array([[1., 1., 1.]], dtype=float32)>
>>> cast_input = tf.keras.backend.cast(input, dtype='float64')
>>> print(cast_input)
tf.Tensor([[1. 1. 1.]], shape=(1, 3), dtype=float64)
```