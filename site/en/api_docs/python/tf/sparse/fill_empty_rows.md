page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.fill_empty_rows


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/sparse/fill_empty_rows">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sparse_ops.py#L1872-L1936">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Fills empty rows in the input 2-D `SparseTensor` with a default value.

### Aliases:

* <a href="/api_docs/python/tf/sparse/fill_empty_rows"><code>tf.compat.v1.sparse.fill_empty_rows</code></a>
* <a href="/api_docs/python/tf/sparse/fill_empty_rows"><code>tf.compat.v1.sparse_fill_empty_rows</code></a>
* <a href="/api_docs/python/tf/sparse/fill_empty_rows"><code>tf.compat.v2.sparse.fill_empty_rows</code></a>
* <a href="/api_docs/python/tf/sparse/fill_empty_rows"><code>tf.sparse_fill_empty_rows</code></a>


``` python
tf.sparse.fill_empty_rows(
    sp_input,
    default_value,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This op adds entries with the specified `default_value` at index
`[row, 0]` for any row in the input that does not already have a value.

For example, suppose `sp_input` has shape `[5, 6]` and non-empty values:

    [0, 1]: a
    [0, 3]: b
    [2, 0]: c
    [3, 1]: d

Rows 1 and 4 are empty, so the output will be of shape `[5, 6]` with values:

    [0, 1]: a
    [0, 3]: b
    [1, 0]: default_value
    [2, 0]: c
    [3, 1]: d
    [4, 0]: default_value

Note that the input may have empty columns at the end, with no effect on
this op.

The output `SparseTensor` will be in row-major order and will have the
same shape as the input.

This op also returns an indicator vector such that

    empty_row_indicator[i] = True iff row i was an empty row.

#### Args:


* <b>`sp_input`</b>: A `SparseTensor` with shape `[N, M]`.
* <b>`default_value`</b>: The value to fill for empty rows, with the same type as
  `sp_input.`
* <b>`name`</b>: A name prefix for the returned tensors (optional)


#### Returns:


* <b>`sp_ordered_output`</b>: A `SparseTensor` with shape `[N, M]`, and with all empty
  rows filled in with `default_value`.
* <b>`empty_row_indicator`</b>: A bool vector of length `N` indicating whether each
  input row was empty.


#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.
