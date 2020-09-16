description: Returns whether x is a Keras tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.is_keras_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.is_keras_tensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L973-L1021">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns whether `x` is a Keras tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.is_keras_tensor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.is_keras_tensor(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->

A "Keras tensor" is a tensor that was returned by a Keras layer,
(`Layer` class) or by `Input`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A candidate tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A boolean: Whether the argument is a Keras tensor.
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
In case `x` is not a symbolic tensor.
</td>
</tr>
</table>



#### Examples:



```
>>> np_var = np.array([1, 2])
>>> # A numpy array is not a symbolic tensor.
>>> tf.keras.backend.is_keras_tensor(np_var)
Traceback (most recent call last):
...
ValueError: Unexpectedly found an instance of type `<class 'numpy.ndarray'>`.
Expected a symbolic tensor instance.
>>> keras_var = tf.keras.backend.variable(np_var)
>>> # A variable created with the keras backend is not a Keras tensor.
>>> tf.keras.backend.is_keras_tensor(keras_var)
False
>>> keras_placeholder = tf.keras.backend.placeholder(shape=(2, 4, 5))
>>> # A placeholder is not a Keras tensor.
>>> tf.keras.backend.is_keras_tensor(keras_placeholder)
False
>>> keras_input = tf.keras.layers.Input([10])
>>> # An Input is a Keras tensor.
>>> tf.keras.backend.is_keras_tensor(keras_input)
True
>>> keras_layer_output = tf.keras.layers.Dense(10)(keras_input)
>>> # Any Keras layer output is a Keras tensor.
>>> tf.keras.backend.is_keras_tensor(keras_layer_output)
True
```