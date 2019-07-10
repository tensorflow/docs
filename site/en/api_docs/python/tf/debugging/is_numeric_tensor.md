page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.is_numeric_tensor

Returns `True` if the elements of `tensor` are numbers.

### Aliases:

* `tf.compat.v1.debugging.is_numeric_tensor`
* `tf.compat.v1.is_numeric_tensor`
* `tf.compat.v2.debugging.is_numeric_tensor`
* `tf.debugging.is_numeric_tensor`
* `tf.is_numeric_tensor`

``` python
tf.debugging.is_numeric_tensor(tensor)
```



Defined in [`python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/check_ops.py).

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