page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_integer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/check_ops.py#L1530-L1547">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert that `x` is of integer dtype.

### Aliases:

* `tf.compat.v2.debugging.assert_integer`


``` python
tf.debugging.assert_integer(
    x,
    message=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

If `x` has a non-integer type, `message`, as well as the dtype of `x` are
printed, and `InvalidArgumentError` is raised.

This can always be checked statically, so this method returns nothing.

#### Args:


* <b>`x`</b>: A `Tensor`.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional). Defaults to "assert_integer".


#### Raises:


* <b>`TypeError`</b>:  If `x.dtype` is not a non-quantized integer type.
