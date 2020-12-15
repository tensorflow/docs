description: Returns the dtype of a Keras tensor or variable, as a string.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.dtype" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.dtype

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L1341-L1371">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the dtype of a Keras tensor or variable, as a string.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.dtype`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.dtype(
    x
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
Tensor or variable.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
String, dtype of `x`.
</td>
</tr>

</table>



#### Examples:



```
>>> tf.keras.backend.dtype(tf.keras.backend.placeholder(shape=(2,4,5)))
'float32'
>>> tf.keras.backend.dtype(tf.keras.backend.placeholder(shape=(2,4,5),
...                                                     dtype='float32'))
'float32'
>>> tf.keras.backend.dtype(tf.keras.backend.placeholder(shape=(2,4,5),
...                                                     dtype='float64'))
'float64'
>>> kvar = tf.keras.backend.variable(np.array([[1, 2], [3, 4]]))
>>> tf.keras.backend.dtype(kvar)
'float32'
>>> kvar = tf.keras.backend.variable(np.array([[1, 2], [3, 4]]),
...                                  dtype='float32')
>>> tf.keras.backend.dtype(kvar)
'float32'
```