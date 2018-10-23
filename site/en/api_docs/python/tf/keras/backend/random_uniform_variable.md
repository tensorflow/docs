

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.random_uniform_variable

``` python
tf.keras.backend.random_uniform_variable(
    shape,
    low,
    high,
    dtype=None,
    name=None,
    seed=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/backend.py).

Instantiates a variable with values drawn from a uniform distribution.

#### Arguments:

* <b>`shape`</b>: Tuple of integers, shape of returned Keras variable.
* <b>`low`</b>: Float, lower boundary of the output interval.
* <b>`high`</b>: Float, upper boundary of the output interval.
* <b>`dtype`</b>: String, dtype of returned Keras variable.
* <b>`name`</b>: String, name of returned Keras variable.
* <b>`seed`</b>: Integer, random seed.


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