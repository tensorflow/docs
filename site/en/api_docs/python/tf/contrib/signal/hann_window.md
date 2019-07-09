page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.signal.hann_window

``` python
tf.contrib.signal.hann_window(
    window_length,
    periodic=True,
    dtype=tf.float32,
    name=None
)
```



Defined in [`tensorflow/contrib/signal/python/ops/window_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/signal/python/ops/window_ops.py).

See the guide: [Signal Processing (contrib) > Reconstructing framed sequences and applying a tapering window](../../../../../api_guides/python/contrib.signal#Reconstructing_framed_sequences_and_applying_a_tapering_window)

Generate a [Hann window][hann].

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