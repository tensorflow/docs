page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.batch_scatter_update


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/state_ops.py#L818-L915">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Generalization of <a href="../tf/scatter_update"><code>tf.compat.v1.scatter_update</code></a> to axis different than 0. (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/batch_scatter_update"><code>tf.compat.v1.batch_scatter_update</code></a>


``` python
tf.batch_scatter_update(
    ref,
    indices,
    updates,
    use_locking=True,
    name=None
)
```



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
<a href="../tf/scatter_update"><code>tf.compat.v1.scatter_update</code></a>.

To avoid this operation there would be 2 alternatives:
1) Reshaping the variable by merging the first `ndims` dimensions. However,
   this is not possible because <a href="../tf/reshape"><code>tf.reshape</code></a> returns a Tensor, which we
   cannot use <a href="../tf/scatter_update"><code>tf.compat.v1.scatter_update</code></a> on.
2) Looping over the first `ndims` of the variable and using
   <a href="../tf/scatter_update"><code>tf.compat.v1.scatter_update</code></a> on the subtensors that result of slicing the
   first
   dimension. This is a valid option for `ndims = 1`, but less efficient than
   this implementation.

See also <a href="../tf/scatter_update"><code>tf.compat.v1.scatter_update</code></a> and <a href="../tf/scatter_nd_update"><code>tf.compat.v1.scatter_nd_update</code></a>.

#### Args:


* <b>`ref`</b>: `Variable` to scatter onto.
* <b>`indices`</b>: Tensor containing indices as described above.
* <b>`updates`</b>: Tensor of updates to apply to `ref`.
* <b>`use_locking`</b>: Boolean indicating whether to lock the writing operation.
* <b>`name`</b>: Optional scope name string.


#### Returns:

Ref to `variable` after it has been modified.



#### Raises:


* <b>`ValueError`</b>: If the initial `ndims` of `ref`, `indices`, and `updates` are
    not the same.
