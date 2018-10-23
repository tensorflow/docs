


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.layers.softmax

### `tf.contrib.layers.softmax`

```
tf.contrib.layers.softmax(*args, **kwargs)
```


Performs softmax on Nth dimension of N-dimensional logit tensor.

For two-dimensional logits this reduces to tf.nn.softmax. The N-th dimension
needs to have a specified number of elements (number of classes).

#### Args:

* <b>`logits`</b>: N-dimensional `Tensor` with logits, where N > 1.
* <b>`scope`</b>: Optional scope for variable_scope.


#### Returns:

  a `Tensor` with same shape and type as logits.

Defined in [`tensorflow/contrib/framework/python/ops/arg_scope.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/python/ops/arg_scope.py).

