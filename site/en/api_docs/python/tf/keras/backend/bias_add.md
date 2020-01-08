page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.bias_add

``` python
tf.keras.backend.bias_add(
    x,
    bias,
    data_format=None
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/keras/backend.py).

Adds a bias vector to a tensor.

#### Arguments:

* <b>`x`</b>: Tensor or variable.
* <b>`bias`</b>: Bias tensor to add.
* <b>`data_format`</b>: string, `"channels_last"` or `"channels_first"`.


#### Returns:

Output tensor.


#### Raises:

* <b>`ValueError`</b>: In one of the two cases below:
                1. invalid `data_format` argument.
                2. invalid bias shape.
                   the bias should be either a vector or
                   a tensor with ndim(x) - 1 dimension