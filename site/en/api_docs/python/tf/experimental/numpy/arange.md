description: TensorFlow variant of NumPy's arange.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.numpy.arange" />
<meta itemprop="path" content="Stable" />
</div>

# tf.experimental.numpy.arange

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_array_ops.py#L260-L298">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



TensorFlow variant of NumPy's `arange`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.experimental.numpy.arange(
    start, stop=None, step=1, dtype=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns `step`-separated values in the range [start, stop).

  Args:
    start: Start of the interval. Included in the range.
    stop: End of the interval. If not specified, `start` is treated as 0 and
      `start` value is used as `stop`. If specified, it is not included in the
      range if `step` is integer. When `step` is floating point, it may or may
      not be included.
    step: The difference between 2 consecutive values in the output range. It is
      recommended to use `linspace` instead of using non-integer values for
      `step`.
    dtype: Optional. Type of the resulting ndarray. Could be a python type, a
      NumPy type or a TensorFlow `DType`. If not provided, the largest type of
      `start`, `stop`, `step` is used.

  Raises:
    ValueError: If step is zero.
  

See the NumPy documentation for [`numpy.arange`](https://numpy.org/doc/1.16/reference/generated/numpy.arange.html).