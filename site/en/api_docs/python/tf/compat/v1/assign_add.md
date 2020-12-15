description: Update ref by adding value to it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.assign_add" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.assign_add

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/state_ops.py#L167-L195">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Update `ref` by adding `value` to it.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.assign_add(
    ref, value, use_locking=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation outputs "ref" after the update is done.
This makes it easier to chain operations that need to use the reset value.
Unlike <a href="../../../tf/math/add.md"><code>tf.math.add</code></a>, this op does not broadcast. `ref` and `value` must have
the same shape.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ref`
</td>
<td>
A mutable `Tensor`. Must be one of the following types: `float32`,
`float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`,
`complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`. Should be
from a `Variable` node.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A `Tensor`. Must have the same shape and dtype as `ref`. The value to
be added to the variable.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
An optional `bool`. Defaults to `False`. If True, the addition
will be protected by a lock; otherwise the behavior is undefined, but may
exhibit less contention.
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
Same as "ref".  Returned as a convenience for operations that want
to use the new value after the variable has been updated.
</td>
</tr>

</table>

