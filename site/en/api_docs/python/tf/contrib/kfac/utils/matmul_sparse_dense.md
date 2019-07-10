page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.utils.matmul_sparse_dense

``` python
tf.contrib.kfac.utils.matmul_sparse_dense(
    A,
    B,
    name=None,
    transpose_a=False,
    transpose_b=False
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/utils.py).

Computes matmul(A, B) where A is sparse, B is dense.

#### Args:

* <b>`A`</b>: tf.IndexedSlices with dense shape [m, n].
* <b>`B`</b>: tf.Tensor with shape [n, k].
* <b>`name`</b>: str. Name of op.
* <b>`transpose_a`</b>: Bool. If true we transpose A before multiplying it by B.
    (Default: False)
* <b>`transpose_b`</b>: Bool. If true we transpose B before multiplying it by A.
    (Default: False)


#### Returns:

tf.IndexedSlices resulting from matmul(A, B).


#### Raises:

* <b>`ValueError`</b>: If A doesn't represent a matrix.
* <b>`ValueError`</b>: If B is not rank-2.