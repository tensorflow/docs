page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.eigh

### Aliases:

* `tf.linalg.eigh`
* `tf.self_adjoint_eig`

``` python
tf.linalg.eigh(
    tensor,
    name=None
)
```



Defined in [`tensorflow/python/ops/linalg_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/linalg_ops.py).

See the guide: [Upgrade to TensorFlow 1.0 > Upgrading your code manually](../../../../api_guides/python/upgrade#Upgrading_your_code_manually)

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