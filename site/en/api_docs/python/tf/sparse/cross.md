page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.cross

``` python
tf.sparse.cross(
    inputs,
    name=None
)
```



Defined in [`tensorflow/python/ops/sparse_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/sparse_ops.py).

Generates sparse cross from a list of sparse and dense tensors.

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