page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.relu_layer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_impl.py#L479-L499">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes Relu(x * weight + biases).

### Aliases:

* <a href="/api_docs/python/tf/nn/relu_layer"><code>tf.compat.v1.nn.relu_layer</code></a>


``` python
tf.nn.relu_layer(
    x,
    weights,
    biases,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: a 2D tensor.  Dimensions typically: batch, in_units
* <b>`weights`</b>: a 2D tensor.  Dimensions typically: in_units, out_units
* <b>`biases`</b>: a 1D tensor.  Dimensions: out_units
* <b>`name`</b>: A name for the operation (optional).  If not specified
  "nn_relu_layer" is used.


#### Returns:

A 2-D Tensor computing relu(matmul(x, weights) + biases).
Dimensions typically: batch, out_units.
