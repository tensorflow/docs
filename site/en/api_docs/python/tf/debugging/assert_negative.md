page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_negative


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_negative">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L437-L454">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert the condition `x < 0` holds element-wise.

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_negative"><code>tf.assert_negative</code></a>
* <a href="/api_docs/python/tf/debugging/assert_negative"><code>tf.compat.v1.assert_negative</code></a>
* <a href="/api_docs/python/tf/debugging/assert_negative"><code>tf.compat.v1.debugging.assert_negative</code></a>


``` python
tf.debugging.assert_negative(
    x,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

When running in graph mode, you should add a dependency on this operation
to ensure that it runs. Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.debugging.assert_negative(x, y)]):
  output = tf.reduce_sum(x)
```

Negative means, for every element `x[i]` of `x`, we have `x[i] < 0`.
If `x` is empty this is trivially satisfied.

#### Args:


* <b>`x`</b>:  Numeric `Tensor`.
* <b>`data`</b>:  The tensors to print out if the condition is False.  Defaults to
  error message and first few entries of `x`.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_negative".


#### Returns:

Op that raises `InvalidArgumentError` if `x < 0` is False.




#### Raises:


* <b>`InvalidArgumentError`</b>: if the check can be performed immediately and
  `x < 0` is False. The check can be performed immediately during 
  eager execution or if `x` is statically known.

#### Eager Compatibility
returns None
