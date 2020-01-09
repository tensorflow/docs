page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.slice


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/sparse/slice">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sparse_ops.py#L960-L1007">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Slice a `SparseTensor` based on the `start` and `size.

### Aliases:

* <a href="/api_docs/python/tf/sparse/slice"><code>tf.compat.v1.sparse.slice</code></a>
* <a href="/api_docs/python/tf/sparse/slice"><code>tf.compat.v1.sparse_slice</code></a>
* <a href="/api_docs/python/tf/sparse/slice"><code>tf.compat.v2.sparse.slice</code></a>
* <a href="/api_docs/python/tf/sparse/slice"><code>tf.sparse_slice</code></a>


``` python
tf.sparse.slice(
    sp_input,
    start,
    size,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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
