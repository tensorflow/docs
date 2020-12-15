description: Computes softmax activations. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.math.softmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.math.softmax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/nn_ops.py#L3599-L3641">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes softmax activations. (deprecated arguments)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.softmax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.math.softmax(
    logits, axis=None, name=None, dim=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dim)`. They will be removed in a future version.
Instructions for updating:
dim is deprecated, use axis instead

This function performs the equivalent of

    softmax = tf.exp(logits) / tf.reduce_sum(tf.exp(logits), axis)

See: https://en.wikipedia.org/wiki/Softmax_function

#### Example usage:



```
>>> tf.nn.softmax([-1, 0., 1.])
<tf.Tensor: shape=(3,), dtype=float32,
numpy=array([0.09003057, 0.24472848, 0.66524094], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`logits`
</td>
<td>
A non-empty `Tensor`, or an object whose type has a registered
`Tensor` conversion function. Must be one of the following types:
`half`,`float32`, `float64`. See also `convert_to_tensor`
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The dimension softmax would be performed on. The default is -1 which
indicates the last dimension.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`dim`
</td>
<td>
Deprecated alias for `axis`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type and shape as `logits`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`InvalidArgumentError`
</td>
<td>
if `logits` is empty or `axis` is beyond the last
dimension of `logits`.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If no conversion function is registered for `logits` to
Tensor.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If a registered conversion function returns an invalid
value.
</td>
</tr>
</table>

