

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.utils.posdef_inv_cholesky

``` python
tf.contrib.kfac.utils.posdef_inv_cholesky(
    tensor,
    identity,
    damping
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/utils.py).

Computes inverse(tensor + damping * identity) with Cholesky.