page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.transpose

``` python
tf.keras.backend.transpose(x)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/keras/backend.py).

Transposes a tensor and returns it.

#### Arguments:

* <b>`x`</b>: Tensor or variable.


#### Returns:

    A tensor.

Examples:

```python
    >>> var = K.variable([[1, 2, 3], [4, 5, 6]])
    >>> K.eval(var)
    array([[ 1.,  2.,  3.],
           [ 4.,  5.,  6.]], dtype=float32)
    >>> var_transposed = K.transpose(var)
    >>> K.eval(var_transposed)
    array([[ 1.,  4.],
           [ 2.,  5.],
           [ 3.,  6.]], dtype=float32)
```

```python
    >>> input = K.placeholder((2, 3))
    >>> input
    <tf.Tensor 'Placeholder_11:0' shape=(2, 3) dtype=float32>
    >>> input_transposed = K.transpose(input)
    >>> input_transposed
    <tf.Tensor 'transpose_4:0' shape=(3, 2) dtype=float32>

```