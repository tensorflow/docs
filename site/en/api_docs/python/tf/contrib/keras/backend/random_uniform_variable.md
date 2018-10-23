

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.random_uniform_variable

### `tf.contrib.keras.backend.random_uniform_variable`

``` python
random_uniform_variable(
    shape,
    low,
    high,
    dtype=None,
    name=None,
    seed=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Instantiates a variable with values drawn from a uniform distribution.

#### Arguments:

    shape: Tuple of integers, shape of returned Keras variable.
    low: Float, lower boundary of the output interval.
    high: Float, upper boundary of the output interval.
    dtype: String, dtype of returned Keras variable.
    name: String, name of returned Keras variable.
    seed: Integer, random seed.


#### Returns:

    A Keras variable, filled with drawn samples.

Example:
```python
    # TensorFlow example
    >>> kvar = K.random_uniform_variable((2,3), 0, 1)
    >>> kvar
    <tensorflow.python.ops.variables.Variable object at 0x10ab40b10>
    >>> K.eval(kvar)
    array([[ 0.10940075,  0.10047495,  0.476143  ],
           [ 0.66137183,  0.00869417,  0.89220798]], dtype=float32)
```