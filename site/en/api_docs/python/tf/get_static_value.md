page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.get_static_value


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/tensor_util.py#L767-L802">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the constant value of the given tensor, if efficiently calculable.

### Aliases:

* `tf.compat.v1.get_static_value`
* `tf.compat.v2.get_static_value`


``` python
tf.get_static_value(
    tensor,
    partial=False
)
```



<!-- Placeholder for "Used in" -->

This function attempts to partially evaluate the given tensor, and
returns its value as a numpy ndarray if this succeeds.

Compatibility(V1): If `constant_value(tensor)` returns a non-`None` result, it
will no longer be possible to feed a different value for `tensor`. This allows
the result of this function to influence the graph that is constructed, and
permits static shape optimizations.

#### Args:


* <b>`tensor`</b>: The Tensor to be evaluated.
* <b>`partial`</b>: If True, the returned numpy array is allowed to have partially
  evaluated values. Values that can't be evaluated will be None.


#### Returns:

A numpy ndarray containing the constant value of the given `tensor`,
or None if it cannot be calculated.



#### Raises:


* <b>`TypeError`</b>: if tensor is not an ops.Tensor.
