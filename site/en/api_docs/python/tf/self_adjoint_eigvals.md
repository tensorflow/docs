


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.self_adjoint_eigvals

### `tf.self_adjoint_eigvals`

```
tf.self_adjoint_eigvals(tensor, name=None)
```


See the guide: [Math > Matrix Math Functions](../../../api_guides/python/math_ops#Matrix_Math_Functions)

Computes the eigenvalues of one or more self-adjoint matrices.

#### Args:

* <b>`tensor`</b>: `Tensor` of shape `[..., N, N]`.
* <b>`name`</b>: string, optional name of the operation.


#### Returns:

* <b>`e`</b>: Eigenvalues. Shape is `[..., N]`. The vector `e[..., :]` contains the `N`
    eigenvalues of `tensor[..., :, :]`.

Defined in [`tensorflow/python/ops/linalg_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/linalg_ops.py).

