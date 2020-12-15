description: Softplus activation function, softplus(x) = log(exp(x) + 1).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.softplus" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.softplus

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/activations.py#L194-L213">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Softplus activation function, `softplus(x) = log(exp(x) + 1)`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.softplus`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.softplus(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example Usage:



```
>>> a = tf.constant([-20, -1.0, 0.0, 1.0, 20], dtype = tf.float32)
>>> b = tf.keras.activations.softplus(a) 
>>> b.numpy()
array([2.0611537e-09, 3.1326166e-01, 6.9314718e-01, 1.3132616e+00,
         2.0000000e+01], dtype=float32)
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
The softplus activation: `log(exp(x) + 1)`.
</td>
</tr>

</table>

