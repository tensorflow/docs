page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.hann_window


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/signal/hann_window">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/signal/window_ops.py#L33-L55">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Generate a [Hann window][hann].

### Aliases:

* <a href="/api_docs/python/tf/signal/hann_window"><code>tf.compat.v1.signal.hann_window</code></a>
* <a href="/api_docs/python/tf/signal/hann_window"><code>tf.compat.v2.signal.hann_window</code></a>
* <a href="/api_docs/python/tf/signal/hann_window"><code>tf.contrib.signal.hann_window</code></a>


``` python
tf.signal.hann_window(
    window_length,
    periodic=True,
    dtype=tf.dtypes.float32,
    name=None
)
```



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
