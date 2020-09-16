description: Creates a 1D tensor containing a sequence of integers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.arange" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.arange

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L3141-L3177">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a 1D tensor containing a sequence of integers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.arange`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.arange(
    start, stop=None, step=1, dtype='int32'
)
</code></pre>



<!-- Placeholder for "Used in" -->

The function arguments use the same convention as
Theano's arange: if only one argument is provided,
it is in fact the "stop" argument and "start" is 0.

The default type of the returned tensor is `'int32'` to
match TensorFlow's default.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`start`
</td>
<td>
Start value.
</td>
</tr><tr>
<td>
`stop`
</td>
<td>
Stop value.
</td>
</tr><tr>
<td>
`step`
</td>
<td>
Difference between two successive values.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Integer dtype to use.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
An integer tensor.
</td>
</tr>

</table>



#### Example:


```
>>> tf.keras.backend.arange(start=0, stop=10, step=1.5)
<tf.Tensor: shape=(7,), dtype=float32,
    numpy=array([0. , 1.5, 3. , 4.5, 6. , 7.5, 9. ], dtype=float32)>
```
