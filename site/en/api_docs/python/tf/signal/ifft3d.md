page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.ifft3d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/signal/ifft3d">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_spectral_ops.py`



Inverse 3D fast Fourier transform.

### Aliases:

* <a href="/api_docs/python/tf/signal/ifft3d"><code>tf.compat.v1.ifft3d</code></a>
* <a href="/api_docs/python/tf/signal/ifft3d"><code>tf.compat.v1.signal.ifft3d</code></a>
* <a href="/api_docs/python/tf/signal/ifft3d"><code>tf.compat.v1.spectral.ifft3d</code></a>
* <a href="/api_docs/python/tf/signal/ifft3d"><code>tf.compat.v2.signal.ifft3d</code></a>
* <a href="/api_docs/python/tf/signal/ifft3d"><code>tf.ifft3d</code></a>
* <a href="/api_docs/python/tf/signal/ifft3d"><code>tf.spectral.ifft3d</code></a>


``` python
tf.signal.ifft3d(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Computes the inverse 3-dimensional discrete Fourier transform over the
inner-most 3 dimensions of `input`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
  A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
