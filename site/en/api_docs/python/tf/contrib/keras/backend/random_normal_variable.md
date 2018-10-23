

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.random_normal_variable

### `tf.contrib.keras.backend.random_normal_variable`

``` python
random_normal_variable(
    shape,
    mean,
    scale,
    dtype=None,
    name=None,
    seed=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Instantiates a variable with values drawn from a normal distribution.

#### Arguments:

    shape: Tuple of integers, shape of returned Keras variable.
    mean: Float, mean of the normal distribution.
    scale: Float, standard deviation of the normal distribution.
    dtype: String, dtype of returned Keras variable.
    name: String, name of returned Keras variable.
    seed: Integer, random seed.


#### Returns:

    A Keras variable, filled with drawn samples.

Example:
```python
    # TensorFlow example
    >>> kvar = K.random_normal_variable((2,3), 0, 1)
    >>> kvar
    <tensorflow.python.ops.variables.Variable object at 0x10ab12dd0>
    >>> K.eval(kvar)
    array([[ 1.19591331,  0.68685907, -0.63814116],
           [ 0.92629528,  0.28055015,  1.70484698]], dtype=float32)
```