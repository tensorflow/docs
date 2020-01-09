page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.serialize_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/serialize_sparse">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sparse_ops.py#L1939-L1956">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

### Aliases:

* <a href="/api_docs/python/tf/io/serialize_sparse"><code>tf.compat.v1.io.serialize_sparse</code></a>
* <a href="/api_docs/python/tf/io/serialize_sparse"><code>tf.compat.v1.serialize_sparse</code></a>
* <a href="/api_docs/python/tf/io/serialize_sparse"><code>tf.serialize_sparse</code></a>


``` python
tf.io.serialize_sparse(
    sp_input,
    name=None,
    out_type=tf.dtypes.string
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sp_input`</b>: The input `SparseTensor`.
* <b>`name`</b>: A name prefix for the returned tensors (optional).
* <b>`out_type`</b>: The `dtype` to use for serialization.


#### Returns:

A 3-vector (1-D `Tensor`), with each column representing the serialized
`SparseTensor`'s indices, values, and shape (respectively).



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.
