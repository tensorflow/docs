

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.utils.posdef_inv_matrix_inverse

``` python
tf.contrib.kfac.utils.posdef_inv_matrix_inverse(
    tensor,
    identity,
    damping
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/utils.py).

Computes inverse(tensor + damping * identity) directly.