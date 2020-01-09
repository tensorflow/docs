page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.assert_less


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L840-L872">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert the condition `x < y` holds element-wise.

### Aliases:

* <a href="/api_docs/python/tf/compat/v2/assert_less"><code>tf.compat.v2.debugging.assert_less</code></a>


``` python
tf.compat.v2.assert_less(
    x,
    y,
    message=None,
    summarize=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This Op checks that `x[i] < y[i]` holds for every pair of (possibly
broadcast) elements of `x` and `y`. If both `x` and `y` are empty, this is
trivially satisfied.

If `x` is not less than `y` element-wise, `message`, as well as the first
`summarize` entries of `x` and `y` are printed, and `InvalidArgumentError` is
raised.

#### Args:


* <b>`x`</b>:  Numeric `Tensor`.
* <b>`y`</b>:  Numeric `Tensor`, same dtype as and broadcastable to `x`.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_less".


#### Returns:

Op that raises `InvalidArgumentError` if `x < y` is False.
This can be used with <a href="../../../tf/control_dependencies"><code>tf.control_dependencies</code></a> inside of <a href="../../../tf/function"><code>tf.function</code></a>s
to block followup computation until the check has executed.




#### Raises:


* <b>`InvalidArgumentError`</b>: if the check can be performed immediately and
  `x < y` is False. The check can be performed immediately during eager
  execution or if `x` and `y` are statically known.

#### Eager Compatibility
returns None
