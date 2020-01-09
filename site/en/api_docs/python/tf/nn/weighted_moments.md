page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.weighted_moments


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_impl.py#L1358-L1379">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the frequency-weighted mean and variance of `x`.

### Aliases:

* `tf.compat.v2.nn.weighted_moments`


``` python
tf.nn.weighted_moments(
    x,
    axes,
    frequency_weights,
    keepdims=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A tensor.
* <b>`axes`</b>: 1-d tensor of int32 values; these are the axes along which
  to compute mean and variance.
* <b>`frequency_weights`</b>: A tensor of positive weights which can be
  broadcast with x.
* <b>`keepdims`</b>: Produce moments with the same dimensionality as the input.
* <b>`name`</b>: Name used to scope the operation.


#### Returns:

Two tensors: `weighted_mean` and `weighted_variance`.
