

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.self_adjoint_eigvals

### Aliases:

* `tf.linalg.eigvalsh`
* `tf.self_adjoint_eigvals`

``` python
tf.self_adjoint_eigvals(
    tensor,
    name=None
)
```



Defined in [`tensorflow/python/ops/linalg_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/linalg_ops.py).

See the guide: [Math > Matrix Math Functions](../../../api_guides/python/math_ops#Matrix_Math_Functions)

Computes the eigenvalues of one or more self-adjoint matrices.

Note: If your program backpropagates through this function, you should replace
it with a call to tf.self_adjoint_eig (possibly ignoring the second output) to
avoid computing the eigen decomposition twice. This is because the
eigenvectors are used to compute the gradient w.r.t. the eigenvalues. See
_SelfAdjointEigV2Grad in linalg_grad.py.

#### Args:

* <b>`tensor`</b>: `Tensor` of shape `[..., N, N]`.
* <b>`name`</b>: string, optional name of the operation.


#### Returns:

* <b>`e`</b>: Eigenvalues. Shape is `[..., N]`. The vector `e[..., :]` contains the `N`
    eigenvalues of `tensor[..., :, :]`.