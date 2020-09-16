description: Update '*var' according to the adagrad scheme.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ApplyAdagrad" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ApplyAdagrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Update '*var' according to the adagrad scheme.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ApplyAdagrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ApplyAdagrad(
    var, accum, lr, grad, use_locking=(False), update_slots=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

accum += grad * grad
var -= lr * grad * (1 / sqrt(accum))

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
`accum`
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
If `True`, updating of the var and accum tensors will be protected
by a lock; otherwise the behavior is undefined, but may exhibit less
contention.
</td>
</tr><tr>
<td>
`update_slots`
</td>
<td>
An optional `bool`. Defaults to `True`.
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

