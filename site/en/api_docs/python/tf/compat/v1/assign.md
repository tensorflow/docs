description: Update ref by assigning value to it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.assign" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.assign

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/state_ops.py#L198-L228">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Update `ref` by assigning `value` to it.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.assign(
    ref, value, validate_shape=None, use_locking=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation outputs a Tensor that holds the new value of `ref` after
the value has been assigned. This makes it easier to chain operations that
need to use the reset value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ref`
</td>
<td>
A mutable `Tensor`. Should be from a `Variable` node. May be
uninitialized.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A `Tensor`. Must have the same shape and dtype as `ref`. The value to
be assigned to the variable.
</td>
</tr><tr>
<td>
`validate_shape`
</td>
<td>
An optional `bool`. Defaults to `True`. If true, the
operation will validate that the shape of 'value' matches the shape of the
Tensor being assigned to.  If false, 'ref' will take on the shape of
'value'.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
An optional `bool`. Defaults to `True`. If True, the assignment
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
A `Tensor` that will hold the new value of `ref` after
the assignment has completed.
</td>
</tr>

</table>

