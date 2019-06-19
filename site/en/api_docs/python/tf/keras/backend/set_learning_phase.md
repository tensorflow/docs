

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.set_learning_phase

``` python
tf.keras.backend.set_learning_phase(value)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/backend.py).

Sets the learning phase to a fixed value.

#### Arguments:

* <b>`value`</b>: Learning phase value, either 0 or 1 (integers).


#### Raises:

* <b>`ValueError`</b>: if `value` is neither `0` nor `1`.