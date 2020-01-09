page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.fftshift


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/signal/fftshift">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/signal/fft_ops.py#L329-L367">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Shift the zero-frequency component to the center of the spectrum.

### Aliases:

* <a href="/api_docs/python/tf/signal/fftshift"><code>tf.compat.v1.signal.fftshift</code></a>
* <a href="/api_docs/python/tf/signal/fftshift"><code>tf.compat.v2.signal.fftshift</code></a>


``` python
tf.signal.fftshift(
    x,
    axes=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This function swaps half-spaces for all axes listed (defaults to all).
Note that ``y[0]`` is the Nyquist component only if ``len(x)`` is even.



#### For example:



```python
x = tf.signal.fftshift([ 0.,  1.,  2.,  3.,  4., -5., -4., -3., -2., -1.])
x.numpy() # array([-5., -4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])
```

#### Args:


* <b>`x`</b>: `Tensor`, input tensor.
* <b>`axes`</b>: `int` or shape `tuple`, optional Axes over which to shift.  Default is
  None, which shifts all axes.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A `Tensor`, The shifted tensor.


#### Numpy Compatibility
Equivalent to numpy.fft.fftshift.
https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftshift.html
