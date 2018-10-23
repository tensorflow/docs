

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.linalg.adjoint

``` python
adjoint(
    matrix,
    name=None
)
```



Defined in [`tensorflow/python/ops/linalg/linalg_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/linalg/linalg_impl.py).

Transposes the last two dimensions of and conjugates tensor `matrix`.

For example:

```python
x = tf.constant([[1 + 1j, 2 + 2j, 3 + 3j],
                 [4 + 4j, 5 + 5j, 6 + 6j]])
tf.linalg.adjoint(x)  # [[1 - 1j, 4 - 4j],
                      #  [2 - 2j, 5 - 5j],
                      #  [3 - 3j, 6 - 6j]]

#### Args:

* <b>`matrix`</b>:  A `Tensor`. Must be `float32`, `float64`, `complex64`, or
    `complex128` with shape `[..., M, M]`.
* <b>`name`</b>:  A name to give this `Op` (optional).


#### Returns:

The adjoint (a.k.a. Hermitian transpose a.k.a. conjugate transpose) of
matrix.