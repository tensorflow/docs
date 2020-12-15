description: The inverse of fftshift.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.ifftshift" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.ifftshift

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/signal/fft_ops.py#L417-L459">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The inverse of fftshift.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.ifftshift`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.ifftshift(
    x, axes=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Although identical for even-length x,
the functions differ by one sample for odd-length x.



#### For example:



```python
x = tf.signal.ifftshift([[ 0.,  1.,  2.],[ 3.,  4., -4.],[-3., -2., -1.]])
x.numpy() # array([[ 4., -4.,  3.],[-2., -1., -3.],[ 1.,  2.,  0.]])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
`Tensor`, input tensor.
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
`int` or shape `tuple` Axes over which to calculate. Defaults to None,
which shifts all axes.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
An optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`, The shifted tensor.
</td>
</tr>

</table>



#### Numpy Compatibility
Equivalent to numpy.fft.ifftshift.
https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifftshift.html

