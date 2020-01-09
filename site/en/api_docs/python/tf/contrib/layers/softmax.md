page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.softmax


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/layers.py#L2888-L2910">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Performs softmax on Nth dimension of N-dimensional logit tensor.

``` python
tf.contrib.layers.softmax(
    logits,
    scope=None
)
```



<!-- Placeholder for "Used in" -->

For two-dimensional logits this reduces to tf.nn.softmax. The N-th dimension
needs to have a specified number of elements (number of classes).

#### Args:


* <b>`logits`</b>: N-dimensional `Tensor` with logits, where N > 1.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

A `Tensor` with same shape and type as logits.
