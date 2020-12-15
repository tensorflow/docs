description: TensorFlow variant of NumPy's pad.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.experimental.numpy.pad" />
<meta itemprop="path" content="Stable" />
</div>

# tf.experimental.numpy.pad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/numpy_ops/np_array_ops.py#L920-L934">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



TensorFlow variant of NumPy's `pad`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.experimental.numpy.pad(
    array, pad_width, mode, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Only supports modes 'constant', 'reflect' and 'symmetric' currently.

See the NumPy documentation for [`numpy.pad`](https://numpy.org/doc/1.16/reference/generated/numpy.pad.html).