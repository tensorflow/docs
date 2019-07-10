page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.relu

Rectified linear unit.

### Aliases:

* `tf.compat.v1.keras.backend.relu`
* `tf.compat.v2.keras.backend.relu`
* `tf.keras.backend.relu`

``` python
tf.keras.backend.relu(
    x,
    alpha=0.0,
    max_value=None,
    threshold=0
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

With default values, it returns element-wise `max(x, 0)`.

Otherwise, it follows:
`f(x) = max_value` for `x >= max_value`,
`f(x) = x` for `threshold <= x < max_value`,
`f(x) = alpha * (x - threshold)` otherwise.

#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`alpha`</b>: A scalar, slope of negative section (default=`0.`).
* <b>`max_value`</b>: float. Saturation threshold.
* <b>`threshold`</b>: float. Threshold value for thresholded activation.


#### Returns:

A tensor.
