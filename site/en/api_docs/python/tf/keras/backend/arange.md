page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.arange

Creates a 1D tensor containing a sequence of integers.

### Aliases:

* `tf.compat.v1.keras.backend.arange`
* `tf.compat.v2.keras.backend.arange`
* `tf.keras.backend.arange`

``` python
tf.keras.backend.arange(
    start,
    stop=None,
    step=1,
    dtype='int32'
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

The function arguments use the same convention as
Theano's arange: if only one argument is provided,
it is in fact the "stop" argument and "start" is 0.

The default type of the returned tensor is `'int32'` to
match TensorFlow's default.

#### Arguments:


* <b>`start`</b>: Start value.
* <b>`stop`</b>: Stop value.
* <b>`step`</b>: Difference between two successive values.
* <b>`dtype`</b>: Integer dtype to use.


#### Returns:

An integer tensor.
