page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.split


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/sparse/split">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sparse_ops.py#L841-L912">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Split a `SparseTensor` into `num_split` tensors along `axis`. (deprecated arguments)

### Aliases:

* <a href="/api_docs/python/tf/sparse/split"><code>tf.compat.v1.sparse.split</code></a>
* <a href="/api_docs/python/tf/sparse/split"><code>tf.compat.v1.sparse_split</code></a>
* <a href="/api_docs/python/tf/sparse/split"><code>tf.sparse_split</code></a>


``` python
tf.sparse.split(
    keyword_required=KeywordRequired(),
    sp_input=None,
    num_split=None,
    axis=None,
    name=None,
    split_dim=None
)
```



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(split_dim)`. They will be removed in a future version.
Instructions for updating:
split_dim is deprecated, use axis instead

If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split`
each slice starting from 0:`shape[axis] % num_split` gets extra one
dimension. For example, if `axis = 1` and `num_split = 2` and the
input is:

    input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

    output_tensor[0] =
    [    a   ]
    [b c     ]

    output_tensor[1] =
    [ d e  ]
    [      ]

#### Args:


* <b>`keyword_required`</b>: Python 2 standin for * (temporary for argument reorder)
* <b>`sp_input`</b>: The `SparseTensor` to split.
* <b>`num_split`</b>: A Python integer. The number of ways to split.
* <b>`axis`</b>: A 0-D `int32` `Tensor`. The dimension along which to split.
* <b>`name`</b>: A name for the operation (optional).
* <b>`split_dim`</b>: Deprecated old name for axis.


#### Returns:

`num_split` `SparseTensor` objects resulting from splitting `value`.



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.
* <b>`ValueError`</b>: If the deprecated `split_dim` and `axis` are both non None.
