description: Update 'ref' by assigning 'value' to it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Assign" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Assign

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Update 'ref' by assigning 'value' to it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Assign`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Assign(
    ref, value, validate_shape=(True), use_locking=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation outputs "ref" after the assignment is done.
This makes it easier to chain operations that need to use the reset value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ref`
</td>
<td>
A mutable `Tensor`.
Should be from a `Variable` node. May be uninitialized.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A `Tensor`. Must have the same type as `ref`.
The value to be assigned to the variable.
</td>
</tr><tr>
<td>
`validate_shape`
</td>
<td>
An optional `bool`. Defaults to `True`.
If true, the operation will validate that the shape
of 'value' matches the shape of the Tensor being assigned to.  If false,
'ref' will take on the shape of 'value'.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
An optional `bool`. Defaults to `True`.
If True, the assignment will be protected by a lock;
otherwise the behavior is undefined, but may exhibit less contention.
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
A mutable `Tensor`. Has the same type as `ref`.
</td>
</tr>

</table>

