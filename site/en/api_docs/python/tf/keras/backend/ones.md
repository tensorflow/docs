description: Instantiates an all-ones variable and returns it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.ones" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.ones

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L1337-L1368">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates an all-ones variable and returns it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.ones`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.ones(
    shape, dtype=None, name=None
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
Tuple of integers, shape of returned Keras variable.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
String, data type of returned Keras variable.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String, name of returned Keras variable.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras variable, filled with `1.0`.
Note that if `shape` was symbolic, we cannot return a variable,
and will return a dynamically-shaped tensor instead.
</td>
</tr>

</table>



#### Example:




```
>>> kvar = tf.keras.backend.ones((3,4))
>>> tf.keras.backend.eval(kvar)
array([[1.,  1.,  1.,  1.],
       [1.,  1.,  1.,  1.],
       [1.,  1.,  1.,  1.]], dtype=float32)
```