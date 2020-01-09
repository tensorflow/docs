page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.retain


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/sparse_ops.py#L1704-L1748">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Retains specified non-empty values within a `SparseTensor`.

### Aliases:

* `tf.compat.v1.sparse.retain`
* `tf.compat.v1.sparse_retain`
* `tf.compat.v2.sparse.retain`


``` python
tf.sparse.retain(
    sp_input,
    to_retain
)
```



<!-- Placeholder for "Used in" -->

For example, if `sp_input` has shape `[4, 5]` and 4 non-empty string values:

    [0, 1]: a
    [0, 3]: b
    [2, 0]: c
    [3, 1]: d

and `to_retain = [True, False, False, True]`, then the output will
be a `SparseTensor` of shape `[4, 5]` with 2 non-empty values:

    [0, 1]: a
    [3, 1]: d

#### Args:


* <b>`sp_input`</b>: The input `SparseTensor` with `N` non-empty elements.
* <b>`to_retain`</b>: A bool vector of length `N` with `M` true values.


#### Returns:

A `SparseTensor` with the same shape as the input and `M` non-empty
elements corresponding to the true positions in `to_retain`.



#### Raises:


* <b>`TypeError`</b>: If `sp_input` is not a `SparseTensor`.
