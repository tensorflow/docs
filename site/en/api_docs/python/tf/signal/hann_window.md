page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.hann_window

Generate a [Hann window][hann].

### Aliases:

* `tf.compat.v1.signal.hann_window`
* `tf.compat.v2.signal.hann_window`
* `tf.contrib.signal.hann_window`
* `tf.signal.hann_window`

``` python
tf.signal.hann_window(
    window_length,
    periodic=True,
    dtype=tf.dtypes.float32,
    name=None
)
```



Defined in [`python/ops/signal/window_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/signal/window_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`window_length`</b>: A scalar `Tensor` indicating the window length to generate.
* <b>`periodic`</b>: A bool `Tensor` indicating whether to generate a periodic or
  symmetric window. Periodic windows are typically used for spectral
  analysis while symmetric windows are typically used for digital
  filter design.
* <b>`dtype`</b>: The data type to produce. Must be a floating point type.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A `Tensor` of shape `[window_length]` of type `dtype`.



#### Raises:


* <b>`ValueError`</b>: If `dtype` is not a floating point type.

[hann]: https://en.wikipedia.org/wiki/Window_function#Hann_and_Hamming_windows