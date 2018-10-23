

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.set_floatx

``` python
tf.keras.backend.set_floatx(value)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/backend.py).

Sets the default float type.

#### Arguments:

* <b>`value`</b>: String; 'float16', 'float32', or 'float64'.

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

* <b>`ValueError`</b>: In case of invalid value.