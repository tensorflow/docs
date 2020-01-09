page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.leaky_relu


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L2800-L2822">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute the Leaky ReLU activation function.

### Aliases:

* `tf.compat.v1.nn.leaky_relu`
* `tf.compat.v2.nn.leaky_relu`


``` python
tf.nn.leaky_relu(
    features,
    alpha=0.2,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Source: [Rectifier Nonlinearities Improve Neural Network Acoustic Models.
AL Maas, AY Hannun, AY Ng - Proc. ICML, 2013](https://ai.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf).

#### Args:


* <b>`features`</b>: A `Tensor` representing preactivation values. Must be one of
  the following types: `float16`, `float32`, `float64`, `int32`, `int64`.
* <b>`alpha`</b>: Slope of the activation function at x < 0.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The activation value.
