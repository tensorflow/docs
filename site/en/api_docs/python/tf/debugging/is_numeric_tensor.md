page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.is_numeric_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/is_numeric_tensor">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L1872-L1896">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns `True` if the elements of `tensor` are numbers.

### Aliases:

* <a href="/api_docs/python/tf/debugging/is_numeric_tensor"><code>tf.compat.v1.debugging.is_numeric_tensor</code></a>
* <a href="/api_docs/python/tf/debugging/is_numeric_tensor"><code>tf.compat.v1.is_numeric_tensor</code></a>
* <a href="/api_docs/python/tf/debugging/is_numeric_tensor"><code>tf.compat.v2.debugging.is_numeric_tensor</code></a>
* <a href="/api_docs/python/tf/debugging/is_numeric_tensor"><code>tf.is_numeric_tensor</code></a>


``` python
tf.debugging.is_numeric_tensor(tensor)
```



<!-- Placeholder for "Used in" -->

Specifically, returns `True` if the dtype of `tensor` is one of the following:

* <a href="../../tf#float32"><code>tf.float32</code></a>
* <a href="../../tf#float64"><code>tf.float64</code></a>
* <a href="../../tf#int8"><code>tf.int8</code></a>
* <a href="../../tf#int16"><code>tf.int16</code></a>
* <a href="../../tf#int32"><code>tf.int32</code></a>
* <a href="../../tf#int64"><code>tf.int64</code></a>
* <a href="../../tf#uint8"><code>tf.uint8</code></a>
* <a href="../../tf#qint8"><code>tf.qint8</code></a>
* <a href="../../tf#qint32"><code>tf.qint32</code></a>
* <a href="../../tf#quint8"><code>tf.quint8</code></a>
* <a href="../../tf#complex64"><code>tf.complex64</code></a>

Returns `False` if `tensor` is of a non-numeric type or if `tensor` is not
a <a href="../../tf/Tensor"><code>tf.Tensor</code></a> object.
