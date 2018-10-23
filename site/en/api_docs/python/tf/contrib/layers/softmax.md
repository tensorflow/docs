

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.softmax

``` python
tf.contrib.layers.softmax(
    logits,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/layers/python/layers/layers.py).

Performs softmax on Nth dimension of N-dimensional logit tensor.

For two-dimensional logits this reduces to tf.nn.softmax. The N-th dimension
needs to have a specified number of elements (number of classes).

#### Args:

* <b>`logits`</b>: N-dimensional `Tensor` with logits, where N > 1.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

A `Tensor` with same shape and type as logits.