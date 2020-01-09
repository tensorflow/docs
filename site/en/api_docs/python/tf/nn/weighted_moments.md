page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.weighted_moments


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/weighted_moments">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_impl.py#L1272-L1347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the frequency-weighted mean and variance of `x`.

### Aliases:

* <a href="/api_docs/python/tf/nn/weighted_moments"><code>tf.compat.v1.nn.weighted_moments</code></a>


``` python
tf.nn.weighted_moments(
    x,
    axes,
    frequency_weights,
    name=None,
    keep_dims=None,
    keepdims=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A tensor.
* <b>`axes`</b>: 1-d tensor of int32 values; these are the axes along which
  to compute mean and variance.
* <b>`frequency_weights`</b>: A tensor of positive weights which can be
  broadcast with x.
* <b>`name`</b>: Name used to scope the operation.
* <b>`keep_dims`</b>: Produce moments with the same dimensionality as the input.
* <b>`keepdims`</b>: Alias of keep_dims.


#### Returns:

Two tensors: `weighted_mean` and `weighted_variance`.
