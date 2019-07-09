page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.eigvalsh

### Aliases:

* `tf.linalg.eigvalsh`
* `tf.self_adjoint_eigvals`

``` python
tf.linalg.eigvalsh(
    tensor,
    name=None
)
```



Defined in [`tensorflow/python/ops/linalg_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/linalg_ops.py).

Computes the eigenvalues of one or more self-adjoint matrices.

Note: If your program backpropagates through this function, you should replace
it with a call to tf.linalg.eigvalsh (possibly ignoring the second output) to
avoid computing the eigen decomposition twice. This is because the
eigenvectors are used to compute the gradient w.r.t. the eigenvalues. See
_SelfAdjointEigV2Grad in linalg_grad.py.

#### Args:

* <b>`tensor`</b>: `Tensor` of shape `[..., N, N]`.
* <b>`name`</b>: string, optional name of the operation.


#### Returns:

* <b>`e`</b>: Eigenvalues. Shape is `[..., N]`. The vector `e[..., :]` contains the `N`
    eigenvalues of `tensor[..., :, :]`.