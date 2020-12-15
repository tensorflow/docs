description: Prints message and the tensor value when evaluated.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.print_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.print_tensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L3608-L3639">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Prints `message` and the tensor value when evaluated.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.print_tensor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.print_tensor(
    x, message=''
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that `print_tensor` returns a new tensor identical to `x`
which should be used in the following code. Otherwise the
print operation is not taken into account during evaluation.

#### Example:



```
>>> x = tf.constant([[1.0, 2.0], [3.0, 4.0]])
>>> tf.keras.backend.print_tensor(x)
<tf.Tensor: shape=(2, 2), dtype=float32, numpy=
  array([[1., 2.],
         [3., 4.]], dtype=float32)>
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
Tensor to print.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
Message to print jointly with the tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The same tensor `x`, unchanged.
</td>
</tr>

</table>

