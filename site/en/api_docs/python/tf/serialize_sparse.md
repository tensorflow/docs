

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.serialize_sparse

``` python
tf.serialize_sparse(
    sp_input,
    name=None,
    out_type=tf.string
)
```



Defined in [`tensorflow/python/ops/sparse_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/ops/sparse_ops.py).

Serialize a `SparseTensor` into a 3-vector (1-D `Tensor`) object.

#### Args:

* <b>`sp_input`</b>: The input `SparseTensor`.
* <b>`name`</b>: A name prefix for the returned tensors (optional).
* <b>`out_type`</b>: The `dtype` to use for serialization.


#### Returns:

A 3-vector (1-D `Tensor`), with each column representing the serialized
`SparseTensor`'s indices, values, and shape (respectively).


#### Raises:

* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.