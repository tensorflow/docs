page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.sparse.split

Split a `SparseTensor` into `num_split` tensors along `axis`.

``` python
tf.compat.v2.sparse.split(
    sp_input=None,
    num_split=None,
    axis=None,
    name=None
)
```



Defined in [`python/ops/sparse_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/sparse_ops.py).

<!-- Placeholder for "Used in" -->

If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split`
each slice starting from 0:`shape[axis] % num_split` gets extra one
dimension. For example, if `axis = 1` and `num_split = 2` and the
input is:

    input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

    output_tensor[0] =
    [    a ]
    [b c   ]

    output_tensor[1] =
    [ d e  ]
    [      ]

#### Args:


* <b>`sp_input`</b>: The `SparseTensor` to split.
* <b>`num_split`</b>: A Python integer. The number of ways to split.
* <b>`axis`</b>: A 0-D `int32` `Tensor`. The dimension along which to split.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`num_split` `SparseTensor` objects resulting from splitting `value`.



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.