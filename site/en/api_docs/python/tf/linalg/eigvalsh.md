page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.eigvalsh


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/eigvalsh">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg_ops.py#L332-L352">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the eigenvalues of one or more self-adjoint matrices.

### Aliases:

* <a href="/api_docs/python/tf/linalg/eigvalsh"><code>tf.compat.v1.linalg.eigvalsh</code></a>
* <a href="/api_docs/python/tf/linalg/eigvalsh"><code>tf.compat.v1.self_adjoint_eigvals</code></a>
* <a href="/api_docs/python/tf/linalg/eigvalsh"><code>tf.compat.v2.linalg.eigvalsh</code></a>
* <a href="/api_docs/python/tf/linalg/eigvalsh"><code>tf.self_adjoint_eigvals</code></a>


``` python
tf.linalg.eigvalsh(
    tensor,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Note: If your program backpropagates through this function, you should replace
it with a call to tf.linalg.eigh (possibly ignoring the second output) to
avoid computing the eigen decomposition twice. This is because the
eigenvectors are used to compute the gradient w.r.t. the eigenvalues. See
_SelfAdjointEigV2Grad in linalg_grad.py.

#### Args:


* <b>`tensor`</b>: `Tensor` of shape `[..., N, N]`.
* <b>`name`</b>: string, optional name of the operation.


#### Returns:


* <b>`e`</b>: Eigenvalues. Shape is `[..., N]`. The vector `e[..., :]` contains the `N`
  eigenvalues of `tensor[..., :, :]`.
