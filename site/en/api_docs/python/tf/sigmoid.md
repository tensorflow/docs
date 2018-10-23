


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.sigmoid

### `tf.nn.sigmoid`

```
tf.nn.sigmoid(x, name=None)
```

### `tf.sigmoid`

```
tf.sigmoid(x, name=None)
```


See the guide: [Neural Network > Activation Functions](../../../api_guides/python/nn#Activation_Functions)

Computes sigmoid of `x` element-wise.

Specifically, `y = 1 / (1 + exp(-x))`.

#### Args:

* <b>`x`</b>: A Tensor with type `float32`, `float64`, `int32`, `complex64`, `int64`,
    or `qint32`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A Tensor with the same type as `x` if `x.dtype != qint32`
    otherwise the return type is `quint8`.



#### numpy compatibility
Equivalent to np.scipy.special.expit



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.tensorflow.org/code/tensorflow/python/ops/math_ops.py).

