page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.leaky_relu

``` python
tf.nn.leaky_relu(
    features,
    alpha=0.2,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/nn_ops.py).

Compute the Leaky ReLU activation function.

"Rectifier Nonlinearities Improve Neural Network Acoustic Models"
AL Maas, AY Hannun, AY Ng - Proc. ICML, 2013
https://ai.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf

#### Args:

* <b>`features`</b>: A `Tensor` representing preactivation values. Must be one of
    the following types: `float16`, `float32`, `float64`, `int32`, `int64`.
* <b>`alpha`</b>: Slope of the activation function at x < 0.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The activation value.