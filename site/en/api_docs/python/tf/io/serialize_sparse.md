page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.serialize_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L1943-L1966">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

### Aliases:

* `tf.compat.v2.io.serialize_sparse`


``` python
tf.io.serialize_sparse(
    sp_input,
    out_type=tf.dtypes.string,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sp_input`</b>: The input `SparseTensor`.
* <b>`out_type`</b>: The `dtype` to use for serialization.
* <b>`name`</b>: A name prefix for the returned tensors (optional).


#### Returns:

A 3-vector (1-D `Tensor`), with each column representing the serialized
`SparseTensor`'s indices, values, and shape (respectively).



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.
