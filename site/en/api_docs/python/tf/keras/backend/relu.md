

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.relu

``` python
relu(
    x,
    alpha=0.0,
    max_value=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/backend.py).

Rectified linear unit.

With default values, it returns element-wise `max(x, 0)`.

#### Arguments:

* <b>`x`</b>: A tensor or variable.
* <b>`alpha`</b>: A scalar, slope of negative section (default=`0.`).
* <b>`max_value`</b>: Saturation threshold.


#### Returns:

A tensor.