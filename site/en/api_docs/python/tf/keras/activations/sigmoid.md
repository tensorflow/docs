description: Sigmoid activation function, sigmoid(x) = 1 / (1 + exp(-x)).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.sigmoid" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.sigmoid

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/activations.py#L371-L401">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sigmoid activation function, `sigmoid(x) = 1 / (1 + exp(-x))`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.sigmoid`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.sigmoid(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->

Applies the sigmoid activation function. For small values (<-5),
`sigmoid` returns a value close to zero, and for large values (>5)
the result of the function gets close to 1.

Sigmoid is equivalent to a 2-element Softmax, where the second element is
assumed to be zero. The sigmoid function always returns a value between
0 and 1.

#### For example:



```
>>> a = tf.constant([-20, -1.0, 0.0, 1.0, 20], dtype = tf.float32)
>>> b = tf.keras.activations.sigmoid(a)
>>> b.numpy()
array([2.0611537e-09, 2.6894143e-01, 5.0000000e-01, 7.3105860e-01,
         1.0000000e+00], dtype=float32)
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
Input tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tensor with the sigmoid activation: `1 / (1 + exp(-x))`.
</td>
</tr>

</table>

