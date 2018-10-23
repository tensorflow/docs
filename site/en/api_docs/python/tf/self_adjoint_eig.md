


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.self_adjoint_eig

### `tf.self_adjoint_eig`

```
tf.self_adjoint_eig(tensor, name=None)
```


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

* <b>`e`</b>: Eigenvalues. Shape is `[..., N]`.
* <b>`v`</b>: Eigenvectors. Shape is `[..., N, N]`. The columns of the inner most
    matrices contain eigenvectors of the corresponding matrices in `tensor`

Defined in [`tensorflow/python/ops/linalg_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/linalg_ops.py).

