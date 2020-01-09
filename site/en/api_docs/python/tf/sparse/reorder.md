page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.reorder


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/sparse/reorder">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sparse_ops.py#L681-L729">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Reorders a `SparseTensor` into the canonical, row-major ordering.

### Aliases:

* <a href="/api_docs/python/tf/sparse/reorder"><code>tf.compat.v1.sparse.reorder</code></a>
* <a href="/api_docs/python/tf/sparse/reorder"><code>tf.compat.v1.sparse_reorder</code></a>
* <a href="/api_docs/python/tf/sparse/reorder"><code>tf.compat.v2.sparse.reorder</code></a>
* <a href="/api_docs/python/tf/sparse/reorder"><code>tf.sparse_reorder</code></a>


``` python
tf.sparse.reorder(
    sp_input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Note that by convention, all sparse ops preserve the canonical ordering
along increasing dimension number. The only time ordering can be violated
is during manual manipulation of the indices and values to add entries.

Reordering does not affect the shape of the `SparseTensor`.

For example, if `sp_input` has shape `[4, 5]` and `indices` / `values`:

    [0, 3]: b
    [0, 1]: a
    [3, 1]: d
    [2, 0]: c

then the output will be a `SparseTensor` of shape `[4, 5]` and
`indices` / `values`:

    [0, 1]: a
    [0, 3]: b
    [2, 0]: c
    [3, 1]: d

#### Args:


* <b>`sp_input`</b>: The input `SparseTensor`.
* <b>`name`</b>: A name prefix for the returned tensors (optional)


#### Returns:

A `SparseTensor` with the same shape and non-empty values, but in
canonical ordering.



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.
