page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.cross


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/sparse/cross">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/sparse_ops.py#L519-L548">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Generates sparse cross from a list of sparse and dense tensors.

### Aliases:

* <a href="/api_docs/python/tf/sparse/cross"><code>tf.compat.v1.sparse.cross</code></a>
* <a href="/api_docs/python/tf/sparse/cross"><code>tf.compat.v2.sparse.cross</code></a>


``` python
tf.sparse.cross(
    inputs,
    name=None
)
```



<!-- Placeholder for "Used in" -->

For example, if the inputs are

    * inputs[0]: SparseTensor with shape = [2, 2]
      [0, 0]: "a"
      [1, 0]: "b"
      [1, 1]: "c"
    * inputs[1]: SparseTensor with shape = [2, 1]
      [0, 0]: "d"
      [1, 0]: "e"
    * inputs[2]: Tensor [["f"], ["g"]]

then the output will be:

    shape = [2, 2]
    [0, 0]: "a_X_d_X_f"
    [1, 0]: "b_X_e_X_g"
    [1, 1]: "c_X_e_X_g"

#### Args:


* <b>`inputs`</b>: An iterable of `Tensor` or `SparseTensor`.
* <b>`name`</b>: Optional name for the op.


#### Returns:

A `SparseTensor` of type `string`.
