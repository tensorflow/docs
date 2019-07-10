page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.learning_phase_scope

Provides a scope within which the learning phase is equal to `value`.

### Aliases:

* `tf.compat.v1.keras.backend.learning_phase_scope`
* `tf.compat.v2.keras.backend.learning_phase_scope`
* `tf.keras.backend.learning_phase_scope`

``` python
tf.keras.backend.learning_phase_scope(value)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

The learning phase gets restored to its original value upon exiting the scope.

#### Arguments:


* <b>`value`</b>: Learning phase value, either 0 or 1 (integers).


#### Yields:

None.



#### Raises:


* <b>`ValueError`</b>: if `value` is neither `0` nor `1`.