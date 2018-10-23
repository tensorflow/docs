

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.set_floatx

### `tf.contrib.keras.backend.set_floatx`

``` python
set_floatx(value)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Sets the default float type.

#### Arguments:

    value: String; 'float16', 'float32', or 'float64'.

Example:

```python
    >>> from keras import backend as K
    >>> K.floatx()
    'float32'
    >>> K.set_floatx('float16')
    >>> K.floatx()
    'float16'
```


#### Raises:

    ValueError: In case of invalid value.