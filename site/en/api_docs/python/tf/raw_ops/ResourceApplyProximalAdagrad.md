description: Update '*var' and '*accum' according to FOBOS with Adagrad learning rate.

robots: noindex

# tf.raw_ops.ResourceApplyProximalAdagrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Update '*var' and '*accum' according to FOBOS with Adagrad learning rate.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ResourceApplyProximalAdagrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ResourceApplyProximalAdagrad(
    var, accum, lr, l1, l2, grad, use_locking=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

accum += grad * grad
prox_v = var - lr * grad * (1 / sqrt(accum))
var = sign(prox_v)/(1+lr*l2) * max{|prox_v|-lr*l1,0}

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`var`
</td>
<td>
A `Tensor` of type `resource`. Should be from a Variable().
</td>
</tr><tr>
<td>
`accum`
</td>
<td>
A `Tensor` of type `resource`. Should be from a Variable().
</td>
</tr><tr>
<td>
`lr`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
Scaling factor. Must be a scalar.
</td>
</tr><tr>
<td>
`l1`
</td>
<td>
A `Tensor`. Must have the same type as `lr`.
L1 regularization. Must be a scalar.
</td>
</tr><tr>
<td>
`l2`
</td>
<td>
A `Tensor`. Must have the same type as `lr`.
L2 regularization. Must be a scalar.
</td>
</tr><tr>
<td>
`grad`
</td>
<td>
A `Tensor`. Must have the same type as `lr`. The gradient.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
An optional `bool`. Defaults to `False`.
If True, updating of the var and accum tensors will be protected by
a lock; otherwise the behavior is undefined, but may exhibit less contention.
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
The created Operation.
</td>
</tr>

</table>

