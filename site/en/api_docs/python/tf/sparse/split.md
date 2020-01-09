page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.split


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L899-L941">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Split a `SparseTensor` into `num_split` tensors along `axis`.

### Aliases:

* `tf.compat.v2.sparse.split`


``` python
tf.sparse.split(
    sp_input=None,
    num_split=None,
    axis=None,
    name=None
)
```



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
