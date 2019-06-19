page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.self_adjoint_eig

### Aliases:

* `tf.linalg.eigh`
* `tf.self_adjoint_eig`

``` python
tf.self_adjoint_eig(
    tensor,
    name=None
)
```



Defined in [`tensorflow/python/ops/linalg_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/linalg_ops.py).

See the guide: [Math > Matrix Math Functions](../../../api_guides/python/math_ops#Matrix_Math_Functions)

Computes the eigen decomposition of a batch of self-adjoint matrices.

Computes the eigenvalues and eigenvectors of the innermost N-by-N matrices
in `tensor` such that
`tensor[...,:,:] * v[..., :,i] = e[..., i] * v[...,:,i]`, for i=0...N-1.

#### Args:

* <b>`tensor`</b>: `Tensor` of shape `[..., N, N]`. Only the lower triangular part of
    each inner inner matrix is referenced.
* <b>`name`</b>: string, optional name of the operation.


#### Returns:

* <b>`e`</b>: Eigenvalues. Shape is `[..., N]`. Sorted in non-decreasing order.
* <b>`v`</b>: Eigenvectors. Shape is `[..., N, N]`. The columns of the inner most
    matrices contain eigenvectors of the corresponding matrices in `tensor`