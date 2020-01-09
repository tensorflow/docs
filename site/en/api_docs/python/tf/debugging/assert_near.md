page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_near


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_near">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L761-L837">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert the condition `x` and `y` are close element-wise.

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_near"><code>tf.assert_near</code></a>
* <a href="/api_docs/python/tf/debugging/assert_near"><code>tf.compat.v1.assert_near</code></a>
* <a href="/api_docs/python/tf/debugging/assert_near"><code>tf.compat.v1.debugging.assert_near</code></a>


``` python
tf.debugging.assert_near(
    x,
    y,
    rtol=None,
    atol=None,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_near(x, y)]):
  output = tf.reduce_sum(x)
```

This condition holds if for every pair of (possibly broadcast) elements
`x[i]`, `y[i]`, we have

```tf.abs(x[i] - y[i]) <= atol + rtol * tf.abs(y[i])```.

If both `x` and `y` are empty, this is trivially satisfied.

The default `atol` and `rtol` is `10 * eps`, where `eps` is the smallest
representable positive number such that `1 + eps != 1`.  This is about
`1.2e-6` in `32bit`, `2.22e-15` in `64bit`, and `0.00977` in `16bit`.
See `numpy.finfo`.

#### Args:


* <b>`x`</b>:  Float or complex `Tensor`.
* <b>`y`</b>:  Float or complex `Tensor`, same `dtype` as, and broadcastable to, `x`.
* <b>`rtol`</b>:  `Tensor`.  Same `dtype` as, and broadcastable to, `x`.
  The relative tolerance.  Default is `10 * eps`.
* <b>`atol`</b>:  `Tensor`.  Same `dtype` as, and broadcastable to, `x`.
  The absolute tolerance.  Default is `10 * eps`.
* <b>`data`</b>:  The tensors to print out if the condition is False.  Defaults to
  error message and first few entries of `x`, `y`.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_near".


#### Returns:

Op that raises `InvalidArgumentError` if `x` and `y` are not close enough.




#### Numpy Compatibility
Similar to `numpy.assert_allclose`, except tolerance depends on data type.
This is due to the fact that `TensorFlow` is often used with `32bit`, `64bit`,
and even `16bit` data.
