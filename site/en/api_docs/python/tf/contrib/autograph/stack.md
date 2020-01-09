page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/lang/special_functions.py#L92-L122">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stacks the input, if it admits the notion of stacking.

``` python
tf.contrib.autograph.stack(
    list_or_tensor,
    element_dtype=None,
    strict=True
)
```



<!-- Placeholder for "Used in" -->

For example, a list of tensors can be stacked into a larger tensor. This
function is similar to tf.stack, but it accepts non-lists and lists of
non-tensors as arguments. In the latter case, the function does nothing.

#### Args:


* <b>`list_or_tensor`</b>: Any
* <b>`element_dtype`</b>: tf.DType, optional dtypedtype for the elements in the list.
    Required if the input is stackable, and the list is untyped.
* <b>`strict`</b>: bool, if True an error is raised if the input is not stackable.
    Otherwise the function is a no-op.


#### Returns:

Any, if the input is stackable, the result will be a tf.Tensor. Otherwise,
if strict=False, the result will be list_or_tensor.



#### Raises:


* <b>`ValueError`</b>: if strict=True and the input is not stackable.
