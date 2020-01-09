page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.logdet


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/linalg/linalg_impl.py#L64-L95">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes log of the determinant of a hermitian positive definite matrix.

### Aliases:

* `tf.compat.v1.linalg.logdet`
* `tf.compat.v2.linalg.logdet`


``` python
tf.linalg.logdet(
    matrix,
    name=None
)
```



<!-- Placeholder for "Used in" -->

```python
# Compute the determinant of a matrix while reducing the chance of over- or
underflow:
A = ... # shape 10 x 10
det = tf.exp(tf.linalg.logdet(A))  # scalar
```

#### Args:


* <b>`matrix`</b>:  A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`,
  or `complex128` with shape `[..., M, M]`.
* <b>`name`</b>:  A name to give this `Op`.  Defaults to `logdet`.


#### Returns:

The natural log of the determinant of `matrix`.




#### Numpy Compatibility
Equivalent to numpy.linalg.slogdet, although no sign is returned since only
hermitian positive definite matrices are supported.
