

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.utils.posdef_inv_matrix_inverse

``` python
tf.contrib.kfac.utils.posdef_inv_matrix_inverse(
    tensor,
    identity,
    damping
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/kfac/python/ops/utils.py).

Computes inverse(tensor + damping * identity) directly.