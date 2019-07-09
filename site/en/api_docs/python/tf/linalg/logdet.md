page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.logdet

``` python
tf.linalg.logdet(
    matrix,
    name=None
)
```



Defined in [`tensorflow/python/ops/linalg/linalg_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/linalg/linalg_impl.py).

Computes log of the determinant of a hermitian positive definite matrix.

```python
# Compute the determinant of a matrix while reducing the chance of over- or
underflow:
A = ... # shape 10 x 10
det = tf.exp(tf.logdet(A))  # scalar
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

