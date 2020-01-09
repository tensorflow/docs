page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.eigh


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/linalg_ops.py#L309-L329">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the eigen decomposition of a batch of self-adjoint matrices.

### Aliases:

* `tf.compat.v1.linalg.eigh`
* `tf.compat.v1.self_adjoint_eig`
* `tf.compat.v2.linalg.eigh`


``` python
tf.linalg.eigh(
    tensor,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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
