page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.cumprod


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/cumprod">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L3305-L3355">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute the cumulative product of the tensor `x` along `axis`.

### Aliases:

* <a href="/api_docs/python/tf/math/cumprod"><code>tf.compat.v1.cumprod</code></a>
* <a href="/api_docs/python/tf/math/cumprod"><code>tf.compat.v1.math.cumprod</code></a>
* <a href="/api_docs/python/tf/math/cumprod"><code>tf.compat.v2.math.cumprod</code></a>
* <a href="/api_docs/python/tf/math/cumprod"><code>tf.cumprod</code></a>


``` python
tf.math.cumprod(
    x,
    axis=0,
    exclusive=False,
    reverse=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

By default, this op performs an inclusive cumprod, which means that the
first element of the input is identical to the first element of the output:

```python
tf.math.cumprod([a, b, c])  # [a, a * b, a * b * c]
```

By setting the `exclusive` kwarg to `True`, an exclusive cumprod is
performed
instead:

```python
tf.math.cumprod([a, b, c], exclusive=True)  # [1, a, a * b]
```

By setting the `reverse` kwarg to `True`, the cumprod is performed in the
opposite direction:

```python
tf.math.cumprod([a, b, c], reverse=True)  # [a * b * c, b * c, c]
```

This is more efficient than using separate <a href="../../tf/reverse"><code>tf.reverse</code></a> ops.
The `reverse` and `exclusive` kwargs can also be combined:

```python
tf.math.cumprod([a, b, c], exclusive=True, reverse=True)  # [b * c, c, 1]
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`,
  `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`,
  `complex128`, `qint8`, `quint8`, `qint32`, `half`.
* <b>`axis`</b>: A `Tensor` of type `int32` (default: 0). Must be in the range
  `[-rank(x), rank(x))`.
* <b>`exclusive`</b>: If `True`, perform exclusive cumprod.
* <b>`reverse`</b>: A `bool` (default: False).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
