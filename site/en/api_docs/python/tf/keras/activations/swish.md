description: Swish activation function, swish(x) = x * sigmoid(x).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.swish" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.swish

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/activations.py#L237-L265">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Swish activation function, `swish(x) = x * sigmoid(x)`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.activations.swish`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.swish(
    x
)
</code></pre>



<!-- Placeholder for "Used in" -->

Swish activation function which returns `x*sigmoid(x)`.
It is a smooth, non-monotonic function that consistently matches
or outperforms ReLU on deep networks, it is unbounded above and
bounded below.


#### Example Usage:



```
>>> a = tf.constant([-20, -1.0, 0.0, 1.0, 20], dtype = tf.float32)
>>> b = tf.keras.activations.swish(a)
>>> b.numpy()
array([-4.1223075e-08, -2.6894143e-01,  0.0000000e+00,  7.3105860e-01,
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
The swish activation applied to `x` (see reference paper for details).
</td>
</tr>

</table>



#### Reference:

- [Ramachandran et al., 2017](https://arxiv.org/abs/1710.05941)
