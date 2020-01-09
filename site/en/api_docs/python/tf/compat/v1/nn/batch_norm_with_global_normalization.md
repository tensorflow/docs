page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.nn.batch_norm_with_global_normalization


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_impl.py#L1529-L1573">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Batch normalization.

``` python
tf.compat.v1.nn.batch_norm_with_global_normalization(
    t=None,
    m=None,
    v=None,
    beta=None,
    gamma=None,
    variance_epsilon=None,
    scale_after_normalization=None,
    name=None,
    input=None,
    mean=None,
    variance=None
)
```



<!-- Placeholder for "Used in" -->

This op is deprecated. See <a href="../../../../tf/nn/batch_normalization"><code>tf.nn.batch_normalization</code></a>.

#### Args:


* <b>`t`</b>: A 4D input Tensor.
* <b>`m`</b>: A 1D mean Tensor with size matching the last dimension of t.
  This is the first output from tf.nn.moments,
  or a saved moving average thereof.
* <b>`v`</b>: A 1D variance Tensor with size matching the last dimension of t.
  This is the second output from tf.nn.moments,
  or a saved moving average thereof.
* <b>`beta`</b>: A 1D beta Tensor with size matching the last dimension of t.
  An offset to be added to the normalized tensor.
* <b>`gamma`</b>: A 1D gamma Tensor with size matching the last dimension of t.
  If "scale_after_normalization" is true, this tensor will be multiplied
  with the normalized tensor.
* <b>`variance_epsilon`</b>: A small float number to avoid dividing by 0.
* <b>`scale_after_normalization`</b>: A bool indicating whether the resulted tensor
  needs to be multiplied with gamma.
* <b>`name`</b>: A name for this operation (optional).
* <b>`input`</b>: Alias for t.
* <b>`mean`</b>: Alias for m.
* <b>`variance`</b>: Alias for v.


#### Returns:

A batch-normalized `t`.
