page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.conv1d

1D convolution.

### Aliases:

* `tf.compat.v1.keras.backend.conv1d`
* `tf.compat.v2.keras.backend.conv1d`
* `tf.keras.backend.conv1d`

``` python
tf.keras.backend.conv1d(
    x,
    kernel,
    strides=1,
    padding='valid',
    data_format=None,
    dilation_rate=1
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`kernel`</b>: kernel tensor.
* <b>`strides`</b>: stride integer.
* <b>`padding`</b>: string, `"same"`, `"causal"` or `"valid"`.
* <b>`data_format`</b>: string, one of "channels_last", "channels_first".
* <b>`dilation_rate`</b>: integer dilate rate.


#### Returns:

A tensor, result of 1D convolution.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is neither `channels_last` or
`channels_first`.