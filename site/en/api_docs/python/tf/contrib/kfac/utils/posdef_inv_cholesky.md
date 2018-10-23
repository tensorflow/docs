

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.utils.posdef_inv_cholesky

``` python
posdef_inv_cholesky(
    tensor,
    identity,
    damping
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/kfac/python/ops/utils.py).

Computes inverse(tensor + damping * identity) with Cholesky.