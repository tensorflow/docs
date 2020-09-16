description: Update '*var' according to the RMSProp algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ApplyRMSProp" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ApplyRMSProp

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Update '*var' according to the RMSProp algorithm.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ApplyRMSProp`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ApplyRMSProp(
    var, ms, mom, lr, rho, momentum, epsilon, grad, use_locking=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that in dense implementation of this algorithm, ms and mom will
update even if the grad is zero, but in this sparse implementation, ms
and mom will not update in iterations during which the grad is zero.

mean_square = decay * mean_square + (1-decay) * gradient ** 2
Delta = learning_rate * gradient / sqrt(mean_square + epsilon)

ms <- rho * ms_{t-1} + (1-rho) * grad * grad
mom <- momentum * mom_{t-1} + lr * grad / sqrt(ms + epsilon)
var <- var - mom

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`var`
</td>
<td>
A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
Should be from a Variable().
</td>
</tr><tr>
<td>
`ms`
</td>
<td>
A mutable `Tensor`. Must have the same type as `var`.
Should be from a Variable().
</td>
</tr><tr>
<td>
`mom`
</td>
<td>
A mutable `Tensor`. Must have the same type as `var`.
Should be from a Variable().
</td>
</tr><tr>
<td>
`lr`
</td>
<td>
A `Tensor`. Must have the same type as `var`.
Scaling factor. Must be a scalar.
</td>
</tr><tr>
<td>
`rho`
</td>
<td>
A `Tensor`. Must have the same type as `var`.
Decay rate. Must be a scalar.
</td>
</tr><tr>
<td>
`momentum`
</td>
<td>
A `Tensor`. Must have the same type as `var`.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A `Tensor`. Must have the same type as `var`.
Ridge term. Must be a scalar.
</td>
</tr><tr>
<td>
`grad`
</td>
<td>
A `Tensor`. Must have the same type as `var`. The gradient.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
An optional `bool`. Defaults to `False`.
If `True`, updating of the var, ms, and mom tensors is protected
by a lock; otherwise the behavior is undefined, but may exhibit less
contention.
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
A mutable `Tensor`. Has the same type as `var`.
</td>
</tr>

</table>

