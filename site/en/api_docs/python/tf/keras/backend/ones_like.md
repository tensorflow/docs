description: Instantiates an all-ones variable of the same shape as another tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.ones_like" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.ones_like

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L1427-L1449">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates an all-ones variable of the same shape as another tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.ones_like`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.ones_like(
    x, dtype=None, name=None
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
Keras variable or tensor.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
String, dtype of returned Keras variable.
None uses the dtype of x.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String, name for the variable to create.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras variable with the shape of x filled with ones.
</td>
</tr>

</table>



#### Example:



```
>>> kvar = tf.keras.backend.variable(np.random.random((2,3)))
>>> kvar_ones = tf.keras.backend.ones_like(kvar)
>>> tf.keras.backend.eval(kvar_ones)
array([[1.,  1.,  1.],
       [1.,  1.,  1.]], dtype=float32)
```