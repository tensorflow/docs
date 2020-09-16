description: Scatter updates into an existing tensor according to indices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tensor_scatter_nd_update" />
<meta itemprop="path" content="Stable" />
</div>

# tf.tensor_scatter_nd_update

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
<p>`tf.compat.v1.tensor_scatter_nd_update`, `tf.compat.v1.tensor_scatter_update`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tensor_scatter_nd_update(
    tensor, indices, updates, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation creates a new tensor by applying sparse `updates` to the passed
in `tensor`.
This operation is very similar to <a href="../tf/scatter_nd.md"><code>tf.scatter_nd</code></a>, except that the updates are
scattered onto an existing tensor (as opposed to a zero-tensor). If the memory
for the existing tensor cannot be re-used, a copy is made and updated.

If `indices` contains duplicates, then their updates are accumulated (summed).

**WARNING**: The order in which updates are applied is nondeterministic, so the
output will be nondeterministic if `indices` contains duplicates -- because
of some numerical approximation issues, numbers summed in different order
may yield different results.

`indices` is an integer tensor containing indices into a new tensor of shape
`shape`.  The last dimension of `indices` can be at most the rank of `shape`:

    indices.shape[-1] <= shape.rank

The last dimension of `indices` corresponds to indices into elements
(if `indices.shape[-1] = shape.rank`) or slices
(if `indices.shape[-1] < shape.rank`) along dimension `indices.shape[-1]` of
`shape`.  `updates` is a tensor with shape

    indices.shape[:-1] + shape[indices.shape[-1]:]

The simplest form of scatter is to insert individual elements in a tensor by
index. For example, say we want to insert 4 scattered elements in a rank-1
tensor with 8 elements.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/ScatterNd1.png" alt>
</div>

In Python, this scatter operation would look like this:

    ```
    >>> indices = tf.constant([[4], [3], [1], [7]])
    >>> updates = tf.constant([9, 10, 11, 12])
    >>> tensor = tf.ones([8], dtype=tf.int32)
    >>> print(tf.tensor_scatter_nd_update(tensor, indices, updates))
    tf.Tensor([ 1 11  1 10  9  1  1 12], shape=(8,), dtype=int32)
    ```

We can also, insert entire slices of a higher rank tensor all at once. For
example, if we wanted to insert two slices in the first dimension of a
rank-3 tensor with two matrices of new values.

In Python, this scatter operation would look like this:

    ```
    >>> indices = tf.constant([[0], [2]])
    >>> updates = tf.constant([[[5, 5, 5, 5], [6, 6, 6, 6],
    ...                         [7, 7, 7, 7], [8, 8, 8, 8]],
    ...                        [[5, 5, 5, 5], [6, 6, 6, 6],
    ...                         [7, 7, 7, 7], [8, 8, 8, 8]]])
    >>> tensor = tf.ones([4, 4, 4], dtype=tf.int32)
    >>> print(tf.tensor_scatter_nd_update(tensor, indices, updates).numpy())
    [[[5 5 5 5]
      [6 6 6 6]
      [7 7 7 7]
      [8 8 8 8]]
     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]
     [[5 5 5 5]
      [6 6 6 6]
      [7 7 7 7]
      [8 8 8 8]]
     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]]
    ```

Note that on CPU, if an out of bound index is found, an error is returned.
On GPU, if an out of bound index is found, the index is ignored.

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

