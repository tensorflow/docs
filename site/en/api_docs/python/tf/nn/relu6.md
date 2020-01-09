page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.relu6


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/relu6">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L2780-L2797">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes Rectified Linear 6: `min(max(features, 0), 6)`.

### Aliases:

* <a href="/api_docs/python/tf/nn/relu6"><code>tf.compat.v1.nn.relu6</code></a>
* <a href="/api_docs/python/tf/nn/relu6"><code>tf.compat.v2.nn.relu6</code></a>


``` python
tf.nn.relu6(
    features,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Source: [Convolutional Deep Belief Networks on CIFAR-10. A.
Krizhevsky](http://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf)

#### Args:


* <b>`features`</b>: A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
  `int16`, or `int8`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with the same type as `features`.
