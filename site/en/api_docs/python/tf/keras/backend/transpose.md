description: Transposes a tensor and returns it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.transpose" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.transpose

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L1887-L1915">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Transposes a tensor and returns it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.transpose`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.transpose(
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
A tensor.
</td>
</tr>

</table>



#### Examples:



```
>>> var = tf.keras.backend.variable([[1, 2, 3], [4, 5, 6]])
>>> tf.keras.backend.eval(var)
array([[1.,  2.,  3.],
       [4.,  5.,  6.]], dtype=float32)
>>> var_transposed = tf.keras.backend.transpose(var)
>>> tf.keras.backend.eval(var_transposed)
array([[1.,  4.],
       [2.,  5.],
       [3.,  6.]], dtype=float32)
>>> input = tf.keras.backend.placeholder((2, 3))
>>> input
<tf.Tensor 'Placeholder_...' shape=(2, 3) dtype=float32>
>>> input_transposed = tf.keras.backend.transpose(input)
>>> input_transposed
<tf.Tensor 'Transpose_...' shape=(3, 2) dtype=float32>
```