page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.autograph.stack

``` python
tf.contrib.autograph.stack(
    list_or_tensor,
    element_dtype=None,
    strict=True
)
```



Defined in [`tensorflow/python/autograph/lang/special_functions.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/autograph/lang/special_functions.py).

Stacks the input, if it admits the notion of stacking.

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