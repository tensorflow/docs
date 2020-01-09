page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.fft


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/signal/fft">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_spectral_ops.py`



Fast Fourier transform.

### Aliases:

* <a href="/api_docs/python/tf/signal/fft"><code>tf.compat.v1.fft</code></a>
* <a href="/api_docs/python/tf/signal/fft"><code>tf.compat.v1.signal.fft</code></a>
* <a href="/api_docs/python/tf/signal/fft"><code>tf.compat.v1.spectral.fft</code></a>
* <a href="/api_docs/python/tf/signal/fft"><code>tf.compat.v2.signal.fft</code></a>
* <a href="/api_docs/python/tf/signal/fft"><code>tf.fft</code></a>
* <a href="/api_docs/python/tf/signal/fft"><code>tf.spectral.fft</code></a>


``` python
tf.signal.fft(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Computes the 1-dimensional discrete Fourier transform over the inner-most
dimension of `input`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
  A complex tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
