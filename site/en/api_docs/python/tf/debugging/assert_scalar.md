page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_scalar


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_scalar">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L2071-L2102">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Asserts that the given `tensor` is a scalar (i.e. zero-dimensional).

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_scalar"><code>tf.assert_scalar</code></a>
* <a href="/api_docs/python/tf/debugging/assert_scalar"><code>tf.compat.v1.assert_scalar</code></a>
* <a href="/api_docs/python/tf/debugging/assert_scalar"><code>tf.compat.v1.debugging.assert_scalar</code></a>
* <a href="/api_docs/python/tf/debugging/assert_scalar"><code>tf.contrib.framework.assert_scalar</code></a>


``` python
tf.debugging.assert_scalar(
    tensor,
    name=None,
    message=None
)
```



<!-- Placeholder for "Used in" -->

This function raises `ValueError` unless it can be certain that the given
`tensor` is a scalar. `ValueError` is also raised if the shape of `tensor` is
unknown.

#### Args:


* <b>`tensor`</b>: A `Tensor`.
* <b>`name`</b>:  A name for this operation. Defaults to "assert_scalar"
* <b>`message`</b>: A string to prefix to the default message.


#### Returns:

The input tensor (potentially converted to a `Tensor`).



#### Raises:


* <b>`ValueError`</b>: If the tensor is not scalar (rank 0), or if its shape is
  unknown.
