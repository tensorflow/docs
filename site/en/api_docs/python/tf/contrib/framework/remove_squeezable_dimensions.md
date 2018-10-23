


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.framework.remove_squeezable_dimensions

### `tf.contrib.framework.remove_squeezable_dimensions`

```
tf.contrib.framework.remove_squeezable_dimensions(predictions, labels, name=None)
```


See the guide: [Framework (contrib)](../../../../../api_guides/python/contrib.framework)

Squeeze last dim if ranks of `predictions` and `labels` differ by 1.

This will use static shape if available. Otherwise, it will add graph
operations, which could result in a performance hit.

#### Args:

* <b>`predictions`</b>: Predicted values, a `Tensor` of arbitrary dimensions.
* <b>`labels`</b>: Label values, a `Tensor` whose dimensions match `predictions`.
* <b>`name`</b>: Name of the op.


#### Returns:

  Tuple of `predictions` and `labels`, possibly with last dim squeezed.

Defined in [`tensorflow/contrib/framework/python/framework/tensor_util.py`](https://www.tensorflow.org/code/tensorflow/contrib/framework/python/framework/tensor_util.py).

