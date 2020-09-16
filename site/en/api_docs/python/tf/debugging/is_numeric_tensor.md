description: Returns True if the elements of tensor are numbers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.is_numeric_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.is_numeric_tensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/check_ops.py#L1886-L1910">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns `True` if the elements of `tensor` are numbers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.debugging.is_numeric_tensor`, `tf.compat.v1.is_numeric_tensor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.debugging.is_numeric_tensor(
    tensor
)
</code></pre>



<!-- Placeholder for "Used in" -->

Specifically, returns `True` if the dtype of `tensor` is one of the following:

* <a href="../../tf.md#float32"><code>tf.float32</code></a>
* <a href="../../tf.md#float64"><code>tf.float64</code></a>
* <a href="../../tf.md#int8"><code>tf.int8</code></a>
* <a href="../../tf.md#int16"><code>tf.int16</code></a>
* <a href="../../tf.md#int32"><code>tf.int32</code></a>
* <a href="../../tf.md#int64"><code>tf.int64</code></a>
* <a href="../../tf.md#uint8"><code>tf.uint8</code></a>
* <a href="../../tf.md#qint8"><code>tf.qint8</code></a>
* <a href="../../tf.md#qint32"><code>tf.qint32</code></a>
* <a href="../../tf.md#quint8"><code>tf.quint8</code></a>
* <a href="../../tf.md#complex64"><code>tf.complex64</code></a>

Returns `False` if `tensor` is of a non-numeric type or if `tensor` is not
a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> object.