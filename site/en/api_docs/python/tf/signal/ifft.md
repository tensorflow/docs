page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.ifft


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/signal/ifft">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_spectral_ops.py`



Inverse fast Fourier transform.

### Aliases:

* <a href="/api_docs/python/tf/signal/ifft"><code>tf.compat.v1.ifft</code></a>
* <a href="/api_docs/python/tf/signal/ifft"><code>tf.compat.v1.signal.ifft</code></a>
* <a href="/api_docs/python/tf/signal/ifft"><code>tf.compat.v1.spectral.ifft</code></a>
* <a href="/api_docs/python/tf/signal/ifft"><code>tf.compat.v2.signal.ifft</code></a>
* <a href="/api_docs/python/tf/signal/ifft"><code>tf.ifft</code></a>
* <a href="/api_docs/python/tf/signal/ifft"><code>tf.spectral.ifft</code></a>


``` python
tf.signal.ifft(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Computes the inverse 1-dimensional discrete Fourier transform over the
inner-most dimension of `input`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
  A complex tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
