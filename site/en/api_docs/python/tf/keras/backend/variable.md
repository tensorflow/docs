description: Instantiates a variable and returns it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.variable" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.variable

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L918-L965">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates a variable and returns it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.variable`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.variable(
    value, dtype=None, name=None, constraint=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
Numpy array, initial value of the tensor.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Tensor type.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name string for the tensor.
</td>
</tr><tr>
<td>
`constraint`
</td>
<td>
Optional projection function to be
applied to the variable after an optimizer update.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A variable instance (with Keras metadata included).
</td>
</tr>

</table>



#### Examples:



```
>>> val = np.array([[1, 2], [3, 4]])
>>> kvar = tf.keras.backend.variable(value=val, dtype='float64',
...                                  name='example_var')
>>> tf.keras.backend.dtype(kvar)
'float64'
>>> print(kvar)
<tf.Variable 'example_var:...' shape=(2, 2) dtype=float64, numpy=
  array([[1., 2.],
         [3., 4.]])>
```