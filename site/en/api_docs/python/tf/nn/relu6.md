page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.relu6

``` python
tf.nn.relu6(
    features,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/nn_ops.py).

Computes Rectified Linear 6: `min(max(features, 0), 6)`.

Source: [Convolutional Deep Belief Networks on CIFAR-10. A.
Krizhevsky](http://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf)

#### Args:

* <b>`features`</b>: A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
    `int16`, or `int8`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with the same type as `features`.