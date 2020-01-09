page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.nn.xw_plus_b


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L4106-L4126">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes matmul(x, weights) + biases.

``` python
tf.compat.v1.nn.xw_plus_b(
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
  "xw_plus_b" is used.


#### Returns:

A 2-D Tensor computing matmul(x, weights) + biases.
Dimensions typically: batch, out_units.
