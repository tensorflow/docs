page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.expm


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/expm">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/linalg/linalg_impl.py#L231-L342">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the matrix exponential of one or more square matrices.

### Aliases:

* <a href="/api_docs/python/tf/linalg/expm"><code>tf.compat.v1.linalg.expm</code></a>
* <a href="/api_docs/python/tf/linalg/expm"><code>tf.compat.v2.linalg.expm</code></a>


``` python
tf.linalg.expm(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

exp(A) = \sum_{n=0}^\infty A^n/n!

The exponential is computed using a combination of the scaling and squaring
method and the Pade approximation. Details can be found in:
Nicholas J. Higham, "The scaling and squaring method for the matrix
exponential revisited," SIAM J. Matrix Anal. Applic., 26:1179-1193, 2005.

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor of the same shape as the input
containing the exponential for all input submatrices `[..., :, :]`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or
  `complex128` with shape `[..., M, M]`.
* <b>`name`</b>:  A name to give this `Op` (optional).


#### Returns:

the matrix exponential of the input.



#### Raises:


* <b>`ValueError`</b>: An unsupported type is provided as input.



#### Scipy Compatibility
Equivalent to scipy.linalg.expm
