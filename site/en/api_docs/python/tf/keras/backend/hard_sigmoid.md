page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.hard_sigmoid

Segment-wise linear approximation of sigmoid.

### Aliases:

* `tf.compat.v1.keras.backend.hard_sigmoid`
* `tf.compat.v2.keras.backend.hard_sigmoid`
* `tf.keras.backend.hard_sigmoid`

``` python
tf.keras.backend.hard_sigmoid(x)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

Faster than sigmoid.
Returns `0.` if `x < -2.5`, `1.` if `x > 2.5`.
In `-2.5 <= x <= 2.5`, returns `0.2 * x + 0.5`.

#### Arguments:


* <b>`x`</b>: A tensor or variable.


#### Returns:

A tensor.
