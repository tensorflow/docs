description: Instantiates a variable with values drawn from a normal distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.random_normal_variable" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.random_normal_variable

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L1605-L1637">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instantiates a variable with values drawn from a normal distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.random_normal_variable`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.random_normal_variable(
    shape, mean, scale, dtype=None, name=None, seed=None
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
`mean`
</td>
<td>
Float, mean of the normal distribution.
</td>
</tr><tr>
<td>
`scale`
</td>
<td>
Float, standard deviation of the normal distribution.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
String, dtype of returned Keras variable.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String, name of returned Keras variable.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Integer, random seed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras variable, filled with drawn samples.
</td>
</tr>

</table>



#### Example:



```
>>> kvar = tf.keras.backend.random_normal_variable(shape=(2,3),
... mean=0.0, scale=1.0)
>>> kvar
<tf.Variable 'Variable:0' shape=(2, 3) dtype=float32, numpy=...,
dtype=float32)>
```