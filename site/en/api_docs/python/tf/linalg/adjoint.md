page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.adjoint

Transposes the last two dimensions of and conjugates tensor `matrix`.

### Aliases:

* `tf.compat.v1.linalg.adjoint`
* `tf.compat.v2.linalg.adjoint`
* `tf.linalg.adjoint`

``` python
tf.linalg.adjoint(
    matrix,
    name=None
)
```



Defined in [`python/ops/linalg/linalg_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/linalg/linalg_impl.py).

<!-- Placeholder for "Used in" -->


#### For example:



```python
x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                 [4 + 4j, 5 + 5j, 6 + 6j]])
tf.linalg.adjoint(x)  # [[1 - 1j, 4 - 4j],
                      #  [2 - 2j, 5 - 5j],
                      #  [3 - 3j, 6 - 6j]]
```

#### Args:


* <b>`matrix`</b>:  A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`,
  or `complex128` with shape `[..., M, M]`.
* <b>`name`</b>:  A name to give this `Op` (optional).


#### Returns:

The adjoint (a.k.a. Hermitian transpose a.k.a. conjugate transpose) of
matrix.
