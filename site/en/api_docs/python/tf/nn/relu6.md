page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.relu6

Computes Rectified Linear 6: `min(max(features, 0), 6)`.

### Aliases:

* `tf.compat.v1.nn.relu6`
* `tf.compat.v2.nn.relu6`
* `tf.nn.relu6`

``` python
tf.nn.relu6(
    features,
    name=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->

Source: [Convolutional Deep Belief Networks on CIFAR-10. A.
Krizhevsky](http://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf)

#### Args:


* <b>`features`</b>: A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
  `int16`, or `int8`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with the same type as `features`.
