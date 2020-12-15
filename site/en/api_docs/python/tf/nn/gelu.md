description: Compute the Gaussian Error Linear Unit (GELU) activation function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.gelu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.gelu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L3505-L3548">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compute the Gaussian Error Linear Unit (GELU) activation function.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.gelu(
    features, approximate=(False), name=None
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
>>> y = tf.nn.gelu(x)
>>> y.numpy()
array([-0.00404951, -0.15865529,  0.        ,  0.8413447 ,  2.9959507 ],
    dtype=float32)
>>> y = tf.nn.gelu(x, approximate=True)
>>> y.numpy()
array([-0.00363752, -0.15880796,  0.        ,  0.841192  ,  2.9963627 ],
    dtype=float32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`
</td>
<td>
A `Tensor` representing preactivation values.
</td>
</tr><tr>
<td>
`approximate`
</td>
<td>
An optional `bool`. Defaults to `False`. Whether to enable
approximation.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with the same type as `features`.
</td>
</tr>

</table>



#### References:

[Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415).
