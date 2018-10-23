

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.leaky_relu

``` python
leaky_relu(
    features,
    alpha=0.2,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/nn_ops.py).

Compute the Leaky ReLU activation function.

"Rectifier Nonlinearities Improve Neural Network Acoustic Models"
AL Maas, AY Hannun, AY Ng - Proc. ICML, 2013
http://web.stanford.edu/~awni/papers/relu_hybrid_icml2013_final.pdf

#### Args:

* <b>`features`</b>: A `Tensor` representing preactivation values.
* <b>`alpha`</b>: Slope of the activation function at x < 0.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The activation value.