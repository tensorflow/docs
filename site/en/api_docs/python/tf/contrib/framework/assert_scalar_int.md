page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.assert_scalar_int


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/framework/tensor_util.py#L302-L319">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert `tensor` is 0-D, of type <a href="../../../tf#int32"><code>tf.int32</code></a> or <a href="../../../tf#int64"><code>tf.int64</code></a>.

``` python
tf.contrib.framework.assert_scalar_int(
    tensor,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`tensor`</b>: `Tensor` to test.
* <b>`name`</b>: Name of the op and of the new `Tensor` if one is created.

#### Returns:

`tensor`, for chaining.


#### Raises:


* <b>`ValueError`</b>: if `tensor` is not 0-D, of integer type.
