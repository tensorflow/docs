description: This op consumes a lock created by MutexLock.

robots: noindex

# tf.raw_ops.ConsumeMutexLock

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



This op consumes a lock created by `MutexLock`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ConsumeMutexLock`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ConsumeMutexLock(
    mutex_lock, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op exists to consume a tensor created by `MutexLock` (other than
direct control dependencies).  It should be the only that consumes the tensor,
and will raise an error if it is not.  Its only purpose is to keep the
mutex lock tensor alive until it is consumed by this op.

**NOTE**: This operation must run on the same device as its input.  This may
be enforced via the `colocate_with` mechanism.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`mutex_lock`
</td>
<td>
A `Tensor` of type `variant`.
A tensor returned by `MutexLock`.
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

