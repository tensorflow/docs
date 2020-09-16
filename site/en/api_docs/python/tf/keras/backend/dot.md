description: Multiplies 2 tensors (and/or variables) and returns a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.dot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.dot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L1639-L1696">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Multiplies 2 tensors (and/or variables) and returns a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.dot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.dot(
    x, y
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
</tr><tr>
<td>
`y`
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
A tensor, dot product of `x` and `y`.
</td>
</tr>

</table>



#### Examples:



```
>>> x = tf.keras.backend.placeholder(shape=(2, 3))
>>> y = tf.keras.backend.placeholder(shape=(3, 4))
>>> xy = tf.keras.backend.dot(x, y)
>>> xy
<tf.Tensor ... shape=(2, 4) dtype=float32>
```

```
>>> x = tf.keras.backend.placeholder(shape=(32, 28, 3))
>>> y = tf.keras.backend.placeholder(shape=(3, 4))
>>> xy = tf.keras.backend.dot(x, y)
>>> xy
<tf.Tensor ... shape=(32, 28, 4) dtype=float32>
```

```
>>> x = tf.keras.backend.random_uniform_variable(shape=(2, 3), low=0, high=1)
>>> y = tf.keras.backend.ones((4, 3, 5))
>>> xy = tf.keras.backend.dot(x, y)
>>> tf.keras.backend.int_shape(xy)
(2, 4, 5)
```