page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.in_test_phase

Selects `x` in test phase, and `alt` otherwise.

### Aliases:

* `tf.compat.v1.keras.backend.in_test_phase`
* `tf.compat.v2.keras.backend.in_test_phase`
* `tf.keras.backend.in_test_phase`

``` python
tf.keras.backend.in_test_phase(
    x,
    alt,
    training=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

Note that `alt` should have the *same shape* as `x`.

#### Arguments:


* <b>`x`</b>: What to return in test phase
    (tensor or callable that returns a tensor).
* <b>`alt`</b>: What to return otherwise
    (tensor or callable that returns a tensor).
* <b>`training`</b>: Optional scalar tensor
    (or Python boolean, or Python integer)
    specifying the learning phase.


#### Returns:

Either `x` or `alt` based on `K.learning_phase`.
