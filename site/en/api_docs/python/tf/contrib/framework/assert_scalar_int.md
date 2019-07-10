page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.assert_scalar_int

Assert `tensor` is 0-D, of type <a href="../../../tf#int32"><code>tf.int32</code></a> or <a href="../../../tf#int64"><code>tf.int64</code></a>.

``` python
tf.contrib.framework.assert_scalar_int(
    tensor,
    name=None
)
```



Defined in [`contrib/framework/python/framework/tensor_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/framework/python/framework/tensor_util.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`tensor`</b>: `Tensor` to test.
* <b>`name`</b>: Name of the op and of the new `Tensor` if one is created.

#### Returns:

`tensor`, for chaining.


#### Raises:


* <b>`ValueError`</b>: if `tensor` is not 0-D, of integer type.