page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse_transpose

``` python
tf.sparse_transpose(
    sp_input,
    perm=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/sparse_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/sparse_ops.py).

See the guide: [Sparse Tensors > Manipulation](../../../api_guides/python/sparse_ops#Manipulation)

Transposes a `SparseTensor`

The returned tensor's dimension i will correspond to the input dimension
`perm[i]`. If `perm` is not given, it is set to (n-1...0), where n is
the rank of the input tensor. Hence by default, this operation performs a
regular matrix transpose on 2-D input Tensors.

For example, if `sp_input` has shape `[4, 5]` and `indices` / `values`:

    [0, 3]: b
    [0, 1]: a
    [3, 1]: d
    [2, 0]: c

then the output will be a `SparseTensor` of shape `[5, 4]` and
`indices` / `values`:

    [0, 2]: c
    [1, 0]: a
    [1, 3]: d
    [3, 0]: b

#### Args:

* <b>`sp_input`</b>: The input `SparseTensor`.
* <b>`perm`</b>: A permutation of the dimensions of `sp_input`.
* <b>`name`</b>: A name prefix for the returned tensors (optional)

#### Returns:

A transposed `SparseTensor`.


#### Raises:

* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.