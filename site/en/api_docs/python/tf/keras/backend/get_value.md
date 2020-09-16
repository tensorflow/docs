description: Returns the value of a variable.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.get_value" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.get_value

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L3279-L3310">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the value of a variable.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.get_value`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.get_value(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->

<a href="../../../tf/keras/backend/get_value.md"><code>backend.get_value</code></a> is the compliment of <a href="../../../tf/keras/backend/set_value.md"><code>backend.set_value</code></a>, and provides
a generic interface for reading from variables while abstracting away the
differences between TensorFlow 1.x and 2.x semantics.

```
>>> K = tf.keras.backend  # Common keras convention
>>> v = K.variable(1.)
```

```
>>> # reassign
>>> K.set_value(v, 2.)
>>> print(K.get_value(v))
2.0
```

```
>>> # increment
>>> K.set_value(v, K.get_value(v) + 1)
>>> print(K.get_value(v))
3.0
```

Variable semantics in TensorFlow 2 are eager execution friendly. The above 
code is roughly equivalent to:

```
>>> v = tf.Variable(1.)
```

```
>>> _ = v.assign(2.)
>>> print(v.numpy())
2.0
```

```
>>> _ = v.assign_add(1.)
>>> print(v.numpy())
3.0
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
input variable.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Numpy array.
</td>
</tr>

</table>

