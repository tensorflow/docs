page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.dct

### Aliases:

* `tf.signal.dct`
* `tf.spectral.dct`

``` python
tf.signal.dct(
    input,
    type=2,
    n=None,
    axis=-1,
    norm=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/signal/dct_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/signal/dct_ops.py).

Computes the 1D [Discrete Cosine Transform (DCT)][dct] of `input`.

Currently only Types I, II and III are supported.
Type I is implemented using a length `2N` padded <a href="../../tf/signal/rfft"><code>tf.spectral.rfft</code></a>.
Type II is implemented using a length `2N` padded <a href="../../tf/signal/rfft"><code>tf.spectral.rfft</code></a>, as
described here:
https://dsp.stackexchange.com/a/10606.
Type III is a fairly straightforward inverse of Type II
(i.e. using a length `2N` padded <a href="../../tf/signal/irfft"><code>tf.spectral.irfft</code></a>).



#### Args:

* <b>`input`</b>: A `[..., samples]` `float32` `Tensor` containing the signals to
    take the DCT of.
* <b>`type`</b>: The DCT type to perform. Must be 1, 2 or 3.
* <b>`n`</b>: For future expansion. The length of the transform. Must be `None`.
* <b>`axis`</b>: For future expansion. The axis to compute the DCT along. Must be `-1`.
* <b>`norm`</b>: The normalization to apply. `None` for no normalization or `'ortho'`
    for orthonormal normalization.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A `[..., samples]` `float32` `Tensor` containing the DCT of `input`.


#### Raises:

* <b>`ValueError`</b>: If `type` is not `1`, `2` or `3`, `n` is not `None, `axis` is
    not `-1`, or `norm` is not `None` or `'ortho'`.
* <b>`ValueError`</b>: If `type` is `1` and `norm` is `ortho`.

[dct]: https://en.wikipedia.org/wiki/Discrete_cosine_transform

#### Scipy Compatibility
Equivalent to scipy.fftpack.dct for Type-I, Type-II and Type-III DCT.
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.fftpack.dct.html

