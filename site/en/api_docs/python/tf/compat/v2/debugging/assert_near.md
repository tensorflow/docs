page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.debugging.assert_near

Assert the condition `x` and `y` are close element-wise.

``` python
tf.compat.v2.debugging.assert_near(
    x,
    y,
    rtol=None,
    atol=None,
    message=None,
    summarize=None,
    name=None
)
```



Defined in [`python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/check_ops.py).

<!-- Placeholder for "Used in" -->

This Op checks that `x[i] - y[i] < atol + rtol * tf.abs(y[i])` holds for every
pair of (possibly broadcast) elements of `x` and `y`. If both `x` and `y` are
empty, this is trivially satisfied.

If any elements of `x` and `y` are not close, `message`, as well as the first
`summarize` entries of `x` and `y` are printed, and `InvalidArgumentError`
is raised.

The default `atol` and `rtol` is `10 * eps`, where `eps` is the smallest
representable positive number such that `1 + eps != 1`.  This is about
`1.2e-6` in `32bit`, `2.22e-15` in `64bit`, and `0.00977` in `16bit`.
See `numpy.finfo`.

#### Args:


* <b>`x`</b>: Float or complex `Tensor`.
* <b>`y`</b>: Float or complex `Tensor`, same dtype as and broadcastable to `x`.
* <b>`rtol`</b>:  `Tensor`.  Same `dtype` as, and broadcastable to, `x`.
  The relative tolerance.  Default is `10 * eps`.
* <b>`atol`</b>:  `Tensor`.  Same `dtype` as, and broadcastable to, `x`.
  The absolute tolerance.  Default is `10 * eps`.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_near".


#### Returns:

Op that raises `InvalidArgumentError` if `x` and `y` are not close enough.
  This can be used with <a href="../../../../tf/control_dependencies"><code>tf.control_dependencies</code></a> inside of <a href="../../../../tf/function"><code>tf.function</code></a>s
  to block followup computation until the check has executed.




#### Raises:


* <b>`InvalidArgumentError`</b>: if the check can be performed immediately and
  `x != y` is False for any pair of elements in `x` and `y`. The check can
  be performed immediately during eager execution or if `x` and `y` are
  statically known.



#### Eager Compatibility
returns None



#### Numpy Compatibility
Similar to `numpy.assert_allclose`, except tolerance depends on data type.
This is due to the fact that `TensorFlow` is often used with `32bit`, `64bit`,
and even `16bit` data.

