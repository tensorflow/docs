

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.dot

``` python
dot(
    x,
    y
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Multiplies 2 tensors (and/or variables) and returns a *tensor*.

When attempting to multiply a nD tensor
with a nD tensor, it reproduces the Theano behavior.
(e.g. `(2, 3) * (4, 3, 5) -> (2, 4, 5)`)

#### Arguments:

    x: Tensor or variable.
    y: Tensor or variable.


#### Returns:

    A tensor, dot product of `x` and `y`.

Examples:

```python
    # dot product between tensors
    >>> x = K.placeholder(shape=(2, 3))
    >>> y = K.placeholder(shape=(3, 4))
    >>> xy = K.dot(x, y)
    >>> xy
    <tf.Tensor 'MatMul_9:0' shape=(2, 4) dtype=float32>
```

```python
    # dot product between tensors
    >>> x = K.placeholder(shape=(32, 28, 3))
    >>> y = K.placeholder(shape=(3, 4))
    >>> xy = K.dot(x, y)
    >>> xy
    <tf.Tensor 'MatMul_9:0' shape=(32, 28, 4) dtype=float32>
```

```python
    # Theano-like behavior example
    >>> x = K.random_uniform_variable(shape=(2, 3), low=0, high=1)
    >>> y = K.ones((4, 3, 5))
    >>> xy = K.dot(x, y)
    >>> K.int_shape(xy)
    (2, 4, 5)
```