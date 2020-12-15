description: Softsign activation function, softsign(x) = x / (abs(x) + 1).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.softsign" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.softsign

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/activations.py#L216-L234">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Softsign activation function, `softsign(x) = x / (abs(x) + 1)`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.softsign`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.softsign(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example Usage:



```
>>> a = tf.constant([-1.0, 0.0, 1.0], dtype = tf.float32)
>>> b = tf.keras.activations.softsign(a)
>>> b.numpy()
array([-0.5,  0. ,  0.5], dtype=float32)
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
The softsign activation: `x / (abs(x) + 1)`.
</td>
</tr>

</table>

