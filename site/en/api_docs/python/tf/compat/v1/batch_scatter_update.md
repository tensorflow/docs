description: Generalization of <a href="../../../tf/compat/v1/scatter_update.md"><code>tf.compat.v1.scatter_update</code></a> to axis different than 0. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.batch_scatter_update" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.batch_scatter_update

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/state_ops.py#L818-L915">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generalization of <a href="../../../tf/compat/v1/scatter_update.md"><code>tf.compat.v1.scatter_update</code></a> to axis different than 0. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.batch_scatter_update(
    ref, indices, updates, use_locking=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-11-29.
Instructions for updating:
Use the batch_scatter_update method of Variable instead.

Analogous to `batch_gather`. This assumes that `ref`, `indices` and `updates`
have a series of leading dimensions that are the same for all of them, and the
updates are performed on the last dimension of indices. In other words, the
dimensions should be the following:

`num_prefix_dims = indices.ndims - 1`
`batch_dim = num_prefix_dims + 1`
`updates.shape = indices.shape + var.shape[batch_dim:]`

where

`updates.shape[:num_prefix_dims]`
`== indices.shape[:num_prefix_dims]`
`== var.shape[:num_prefix_dims]`

And the operation performed can be expressed as:

`var[i_1, ..., i_n, indices[i_1, ..., i_n, j]] = updates[i_1, ..., i_n, j]`

When indices is a 1D tensor, this operation is equivalent to
<a href="../../../tf/compat/v1/scatter_update.md"><code>tf.compat.v1.scatter_update</code></a>.

To avoid this operation there would be 2 alternatives:
1) Reshaping the variable by merging the first `ndims` dimensions. However,
   this is not possible because <a href="../../../tf/reshape.md"><code>tf.reshape</code></a> returns a Tensor, which we
   cannot use <a href="../../../tf/compat/v1/scatter_update.md"><code>tf.compat.v1.scatter_update</code></a> on.
2) Looping over the first `ndims` of the variable and using
   <a href="../../../tf/compat/v1/scatter_update.md"><code>tf.compat.v1.scatter_update</code></a> on the subtensors that result of slicing the
   first
   dimension. This is a valid option for `ndims = 1`, but less efficient than
   this implementation.

See also <a href="../../../tf/compat/v1/scatter_update.md"><code>tf.compat.v1.scatter_update</code></a> and <a href="../../../tf/compat/v1/scatter_nd_update.md"><code>tf.compat.v1.scatter_nd_update</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ref`
</td>
<td>
`Variable` to scatter onto.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
Tensor containing indices as described above.
</td>
</tr><tr>
<td>
`updates`
</td>
<td>
Tensor of updates to apply to `ref`.
</td>
</tr><tr>
<td>
`use_locking`
</td>
<td>
Boolean indicating whether to lock the writing operation.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional scope name string.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Ref to `variable` after it has been modified.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the initial `ndims` of `ref`, `indices`, and `updates` are
not the same.
</td>
</tr>
</table>

