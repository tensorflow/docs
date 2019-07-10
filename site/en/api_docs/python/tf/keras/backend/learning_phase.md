page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.learning_phase

Returns the learning phase flag.

### Aliases:

* `tf.compat.v1.keras.backend.learning_phase`
* `tf.compat.v2.keras.backend.learning_phase`
* `tf.keras.backend.learning_phase`

``` python
tf.keras.backend.learning_phase()
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

The learning phase flag is a bool tensor (0 = test, 1 = train)
to be passed as input to any Keras function
that uses a different behavior at train time and test time.

#### Returns:

Learning phase (scalar integer tensor or Python integer).
