page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.repeat

Repeats a 2D tensor.

### Aliases:

* `tf.compat.v1.keras.backend.repeat`
* `tf.compat.v2.keras.backend.repeat`
* `tf.keras.backend.repeat`

``` python
tf.keras.backend.repeat(
    x,
    n
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

if `x` has shape (samples, dim) and `n` is `2`,
the output will have shape `(samples, 2, dim)`.

#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`n`</b>: Python integer, number of times to repeat.


#### Returns:

A tensor.
