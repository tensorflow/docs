description: Applies the Gaussian error linear unit (GELU) activation function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.activations.gelu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.activations.gelu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/activations.py#L309-L346">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies the Gaussian error linear unit (GELU) activation function.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.activations.gelu(
    x, approximate=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Gaussian error linear unit (GELU) computes
`x * P(X <= x)`, where `P(X) ~ N(0, 1)`.
The (GELU) nonlinearity weights inputs by their value, rather than gates
inputs by their sign as in ReLU.

#### For example:



```
>>> x = tf.constant([-3.0, -1.0, 0.0, 1.0, 3.0], dtype=tf.float32)
>>> y = tf.keras.activations.gelu(x)
>>> y.numpy()
array([-0.00404951, -0.15865529,  0.        ,  0.8413447 ,  2.9959507 ],
    dtype=float32)
>>> y = tf.keras.activations.gelu(x, approximate=True)
>>> y.numpy()
array([-0.00363752, -0.15880796,  0.        ,  0.841192  ,  2.9963627 ],
    dtype=float32)
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
</tr><tr>
<td>
`approximate`
</td>
<td>
A `bool`, whether to enable approximation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The gaussian error linear activation:
`0.5 * x * (1 + tanh(sqrt(2 / pi) * (x + 0.044715 * x^3)))`
if `approximate` is `True` or
`x * P(X <= x) = 0.5 * x * (1 + erf(x / sqrt(2)))`,
where `P(X) ~ N(0, 1)`,
if `approximate` is `False`.
</td>
</tr>

</table>



#### Reference:

- [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415)
