page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.slice

### Aliases:

* `tf.sparse.slice`
* `tf.sparse_slice`

``` python
tf.sparse.slice(
    sp_input,
    start,
    size,
    name=None
)
```



Defined in [`tensorflow/python/ops/sparse_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/sparse_ops.py).

Slice a `SparseTensor` based on the `start` and `size.

For example, if the input is

    input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

    sparse.slice([0, 0], [2, 4]) = shape = [2, 4]
    [    a  ]
    [b c    ]

    sparse.slice([0, 4], [2, 3]) = shape = [2, 3]
    [ d e  ]
    [      ]

#### Args:

* <b>`sp_input`</b>: The `SparseTensor` to split.
* <b>`start`</b>: 1-D. tensor represents the start of the slice.
* <b>`size`</b>: 1-D. tensor represents the size of the slice.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `SparseTensor` objects resulting from splicing.


#### Raises:

* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.