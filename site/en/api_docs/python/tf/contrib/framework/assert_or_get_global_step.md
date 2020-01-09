page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.assert_or_get_global_step


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/ops/variables.py#L99-L120">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Verifies that a global step tensor is valid or gets one if None is given.

``` python
tf.contrib.framework.assert_or_get_global_step(
    graph=None,
    global_step_tensor=None
)
```



<!-- Placeholder for "Used in" -->

If `global_step_tensor` is not None, check that it is a valid global step
tensor (using `assert_global_step`). Otherwise find a global step tensor using
`get_global_step` and return it.

#### Args:


* <b>`graph`</b>: The graph to find the global step tensor for.
* <b>`global_step_tensor`</b>: The tensor to check for suitability as a global step. If
  None is given (the default), find a global step tensor.


#### Returns:

A tensor suitable as a global step, or `None` if none was provided and none
was found.
