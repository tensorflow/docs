page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.serialize_many_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/serialize_many_sparse">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sparse_ops.py#L1985-L2011">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Serialize `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor`.

### Aliases:

* <a href="/api_docs/python/tf/io/serialize_many_sparse"><code>tf.compat.v1.io.serialize_many_sparse</code></a>
* <a href="/api_docs/python/tf/io/serialize_many_sparse"><code>tf.compat.v1.serialize_many_sparse</code></a>
* <a href="/api_docs/python/tf/io/serialize_many_sparse"><code>tf.serialize_many_sparse</code></a>


``` python
tf.io.serialize_many_sparse(
    sp_input,
    name=None,
    out_type=tf.dtypes.string
)
```



<!-- Placeholder for "Used in" -->

The `SparseTensor` must have rank `R` greater than 1, and the first dimension
is treated as the minibatch dimension.  Elements of the `SparseTensor`
must be sorted in increasing order of this first dimension.  The serialized
`SparseTensor` objects going into each row of the output `Tensor` will have
rank `R-1`.

The minibatch size `N` is extracted from `sparse_shape[0]`.

#### Args:


* <b>`sp_input`</b>: The input rank `R` `SparseTensor`.
* <b>`name`</b>: A name prefix for the returned tensors (optional).
* <b>`out_type`</b>: The `dtype` to use for serialization.


#### Returns:

A matrix (2-D `Tensor`) with `N` rows and `3` columns. Each column
represents serialized `SparseTensor`'s indices, values, and shape
(respectively).



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.
