page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.dot


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L1635-L1704">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Multiplies 2 tensors (and/or variables) and returns a *tensor*.

### Aliases:

* `tf.compat.v1.keras.backend.dot`
* `tf.compat.v2.keras.backend.dot`


``` python
tf.keras.backend.dot(
    x,
    y
)
```



<!-- Placeholder for "Used in" -->

When attempting to multiply a nD tensor
with a nD tensor, it reproduces the Theano behavior.
(e.g. `(2, 3) * (4, 3, 5) -> (2, 4, 5)`)

#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`y`</b>: Tensor or variable.


#### Returns:

A tensor, dot product of `x` and `y`.



#### Examples:


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
