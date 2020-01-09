page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.dct


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/signal/dct">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/signal/dct_ops.py#L51-L163">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the 1D [Discrete Cosine Transform (DCT)][dct] of `input`.

### Aliases:

* <a href="/api_docs/python/tf/signal/dct"><code>tf.compat.v1.signal.dct</code></a>
* <a href="/api_docs/python/tf/signal/dct"><code>tf.compat.v1.spectral.dct</code></a>
* <a href="/api_docs/python/tf/signal/dct"><code>tf.compat.v2.signal.dct</code></a>
* <a href="/api_docs/python/tf/signal/dct"><code>tf.spectral.dct</code></a>


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



<!-- Placeholder for "Used in" -->

Currently only Types I, II and III are supported.
Type I is implemented using a length `2N` padded <a href="../../tf/signal/rfft"><code>tf.signal.rfft</code></a>.
Type II is implemented using a length `2N` padded <a href="../../tf/signal/rfft"><code>tf.signal.rfft</code></a>, as
described here: [Type 2 DCT using 2N FFT padded (Makhoul)](https://dsp.stackexchange.com/a/10606).
Type III is a fairly straightforward inverse of Type II
(i.e. using a length `2N` padded <a href="../../tf/signal/irfft"><code>tf.signal.irfft</code></a>).



#### Args:


* <b>`input`</b>: A `[..., samples]` `float32` `Tensor` containing the signals to
  take the DCT of.
* <b>`type`</b>: The DCT type to perform. Must be 1, 2 or 3.
* <b>`n`</b>: The length of the transform. If length is less than sequence length,
  only the first n elements of the sequence are considered for the DCT.
  If n is greater than the sequence length, zeros are padded and then
  the DCT is computed as usual.
* <b>`axis`</b>: For future expansion. The axis to compute the DCT along. Must be `-1`.
* <b>`norm`</b>: The normalization to apply. `None` for no normalization or `'ortho'`
  for orthonormal normalization.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A `[..., samples]` `float32` `Tensor` containing the DCT of `input`.



#### Raises:


* <b>`ValueError`</b>: If `type` is not `1`, `2` or `3`, `axis` is
  not `-1`, `n` is not `None` or greater than 0,
  or `norm` is not `None` or `'ortho'`.
* <b>`ValueError`</b>: If `type` is `1` and `norm` is `ortho`.

[dct]: https://en.wikipedia.org/wiki/Discrete_cosine_transform

#### Scipy Compatibility
Equivalent to [scipy.fftpack.dct](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.fftpack.dct.html)
 for Type-I, Type-II and Type-III DCT.
