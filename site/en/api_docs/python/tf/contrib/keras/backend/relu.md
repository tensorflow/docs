

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.relu

### `tf.contrib.keras.backend.relu`

``` python
relu(
    x,
    alpha=0.0,
    max_value=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Rectified linear unit.

With default values, it returns element-wise `max(x, 0)`.

#### Arguments:

    x: A tensor or variable.
    alpha: A scalar, slope of negative section (default=`0.`).
    max_value: Saturation threshold.


#### Returns:

    A tensor.