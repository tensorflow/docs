

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.shape

``` python
tf.keras.backend.shape(x)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/backend.py).

Returns the symbolic shape of a tensor or variable.

#### Arguments:

* <b>`x`</b>: A tensor or variable.


#### Returns:

    A symbolic shape (which is itself a tensor).

Examples:

```python
    # TensorFlow example
    >>> from keras import backend as K
    >>> tf_session = K.get_session()
    >>> val = np.array([[1, 2], [3, 4]])
    >>> kvar = K.variable(value=val)
    >>> input = keras.backend.placeholder(shape=(2, 4, 5))
    >>> K.shape(kvar)
    <tf.Tensor 'Shape_8:0' shape=(2,) dtype=int32>
    >>> K.shape(input)
    <tf.Tensor 'Shape_9:0' shape=(3,) dtype=int32>
    # To get integer shape (Instead, you can use K.int_shape(x))
    >>> K.shape(kvar).eval(session=tf_session)
    array([2, 2], dtype=int32)
    >>> K.shape(input).eval(session=tf_session)
    array([2, 4, 5], dtype=int32)
```