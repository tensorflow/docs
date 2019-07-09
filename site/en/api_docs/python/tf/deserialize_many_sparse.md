page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.deserialize_many_sparse

``` python
tf.deserialize_many_sparse(
    serialized_sparse,
    dtype,
    rank=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/sparse_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/sparse_ops.py).

Deserialize and concatenate `SparseTensors` from a serialized minibatch.

The input `serialized_sparse` must be a string matrix of shape `[N x 3]` where
`N` is the minibatch size and the rows correspond to packed outputs of
`serialize_sparse`.  The ranks of the original `SparseTensor` objects
must all match.  When the final `SparseTensor` is created, it has rank one
higher than the ranks of the incoming `SparseTensor` objects (they have been
concatenated along a new row dimension).

The output `SparseTensor` object's shape values for all dimensions but the
first are the max across the input `SparseTensor` objects' shape values
for the corresponding dimensions.  Its first shape value is `N`, the minibatch
size.

The input `SparseTensor` objects' indices are assumed ordered in
standard lexicographic order.  If this is not the case, after this
step run `sparse_reorder` to restore index ordering.

For example, if the serialized input is a `[2, 3]` matrix representing two
original `SparseTensor` objects:

    index = [ 0]
            [10]
            [20]
    values = [1, 2, 3]
    shape = [50]

and

    index = [ 2]
            [10]
    values = [4, 5]
    shape = [30]

then the final deserialized `SparseTensor` will be:

    index = [0  0]
            [0 10]
            [0 20]
            [1  2]
            [1 10]
    values = [1, 2, 3, 4, 5]
    shape = [2 50]

#### Args:

* <b>`serialized_sparse`</b>: 2-D `Tensor` of type `string` of shape `[N, 3]`.
    The serialized and packed `SparseTensor` objects.
* <b>`dtype`</b>: The `dtype` of the serialized `SparseTensor` objects.
* <b>`rank`</b>: (optional) Python int, the rank of the `SparseTensor` objects.
* <b>`name`</b>: A name prefix for the returned tensors (optional)


#### Returns:

A `SparseTensor` representing the deserialized `SparseTensor`s,
concatenated along the `SparseTensor`s' first dimension.

All of the serialized `SparseTensor`s must have had the same rank and type.