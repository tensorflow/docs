

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.utils.matmul_sparse_dense

``` python
tf.contrib.kfac.utils.matmul_sparse_dense(
    A,
    B,
    name=None
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/utils.py).

Computes matmul(A, B) where A is sparse, B is dense.

#### Args:

* <b>`A`</b>: tf.IndexedSlices with dense shape [m, n].
* <b>`B`</b>: tf.Tensor with shape [n, k].
* <b>`name`</b>: str. Name of op.


#### Returns:

tf.IndexedSlices resulting from matmul(A, B).


#### Raises:

* <b>`ValueError`</b>: If A doesn't represent a matrix.
* <b>`ValueError`</b>: If B is not rank-2.