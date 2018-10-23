


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.serialize_sparse

### `tf.serialize_sparse`

```
tf.serialize_sparse(sp_input, name=None)
```


Serialize a `SparseTensor` into a string 3-vector (1-D `Tensor`) object.

#### Args:

* <b>`sp_input`</b>: The input `SparseTensor`.
* <b>`name`</b>: A name prefix for the returned tensors (optional).


#### Returns:

  A string 3-vector (1D `Tensor`), with each column representing the
  serialized `SparseTensor`'s indices, values, and shape (respectively).


#### Raises:

* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.

Defined in [`tensorflow/python/ops/sparse_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/sparse_ops.py).

