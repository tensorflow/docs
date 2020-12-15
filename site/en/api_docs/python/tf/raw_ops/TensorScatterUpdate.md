description: Scatter updates into an existing tensor according to indices.

robots: noindex

# tf.raw_ops.TensorScatterUpdate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Scatter `updates` into an existing tensor according to `indices`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorScatterUpdate`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorScatterUpdate(
    tensor, indices, updates, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation creates a new tensor by applying sparse `updates` to the passed
in `tensor`.
This operation is very similar to <a href="../../tf/scatter_nd.md"><code>tf.scatter_nd</code></a>, except that the updates are
scattered onto an existing tensor (as opposed to a zero-tensor). If the memory
for the existing tensor cannot be re-used, a copy is made and updated.

If `indices` contains duplicates, then we pick the last update for the index.

If an out of bound index is found on CPU, an error is returned.

**WARNING**: There are some GPU specific semantics for this operation.
- If an out of bound index is found, the index is ignored.
- The order in which updates are applied is nondeterministic, so the output
will be nondeterministic if `indices` contains duplicates.

`indices` is an integer tensor containing indices into a new tensor of shape
`shape`.

* `indices` must have at least 2 axes: `(num_updates, index_depth)`.
* The last axis of `indices` is how deep to index into `tensor` so  this index
  depth must be less than the rank of `tensor`: `indices.shape[-1] <= tensor.ndim`

if `indices.shape[-1] = tensor.rank` this Op indexes and updates scalar elements.
if `indices.shape[-1] < tensor.rank` it indexes and updates slices of the input
`tensor`.

Each `update` has a rank of `tensor.rank - indices.shape[-1]`.
The overall shape of `updates` is:

```
indices.shape[:-1] + tensor.shape[indices.shape[-1]:]
```

For usage examples see the python [tf.tensor_scatter_nd_update](
https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_update) function

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
A `Tensor`. Tensor to copy/update.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Index tensor.
</td>
</tr><tr>
<td>
`updates`
</td>
<td>
A `Tensor`. Must have the same type as `tensor`.
Updates to scatter into output.
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
A `Tensor`. Has the same type as `tensor`.
</td>
</tr>

</table>

