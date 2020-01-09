page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.remove_squeezable_dimensions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/framework/tensor_util.py#L81-L130">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Squeeze last dim if ranks of `predictions` and `labels` differ by 1. (deprecated)

``` python
tf.contrib.framework.remove_squeezable_dimensions(
    predictions,
    labels,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to remove_squeezable_dimensions from tf.confusion_matrix. Note that the order of the inputs and outputs of labels and predictions have also been switched.

This will use static shape if available. Otherwise, it will add graph
operations, which could result in a performance hit.

#### Args:


* <b>`predictions`</b>: Predicted values, a `Tensor` of arbitrary dimensions.
* <b>`labels`</b>: Label values, a `Tensor` whose dimensions match `predictions`.
* <b>`name`</b>: Name of the op.


#### Returns:

Tuple of `predictions` and `labels`, possibly with last dim squeezed.
