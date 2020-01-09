page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.random_uniform_variable


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L1444-L1478">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Instantiates a variable with values drawn from a uniform distribution.

### Aliases:

* `tf.compat.v1.keras.backend.random_uniform_variable`
* `tf.compat.v2.keras.backend.random_uniform_variable`


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



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`shape`</b>: Tuple of integers, shape of returned Keras variable.
* <b>`low`</b>: Float, lower boundary of the output interval.
* <b>`high`</b>: Float, upper boundary of the output interval.
* <b>`dtype`</b>: String, dtype of returned Keras variable.
* <b>`name`</b>: String, name of returned Keras variable.
* <b>`seed`</b>: Integer, random seed.


#### Returns:

A Keras variable, filled with drawn samples.



#### Example:


```python
    # TensorFlow example
    >>> kvar = K.random_uniform_variable((2,3), 0, 1)
    >>> kvar
    <tensorflow.python.ops.variables.Variable object at 0x10ab40b10>
    >>> K.eval(kvar)
    array([[ 0.10940075,  0.10047495,  0.476143  ],
           [ 0.66137183,  0.00869417,  0.89220798]], dtype=float32)
```
