page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.normalize_moments


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_impl.py#L1147-L1176">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Calculate the mean and variance of based on the sufficient statistics.

### Aliases:

* `tf.compat.v1.nn.normalize_moments`
* `tf.compat.v2.nn.normalize_moments`


``` python
tf.nn.normalize_moments(
    counts,
    mean_ss,
    variance_ss,
    shift,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`counts`</b>: A `Tensor` containing the total count of the data (one value).
* <b>`mean_ss`</b>: A `Tensor` containing the mean sufficient statistics: the (possibly
  shifted) sum of the elements to average over.
* <b>`variance_ss`</b>: A `Tensor` containing the variance sufficient statistics: the
  (possibly shifted) squared sum of the data to compute the variance over.
* <b>`shift`</b>: A `Tensor` containing the value by which the data is shifted for
  numerical stability, or `None` if no shift was performed.
* <b>`name`</b>: Name used to scope the operations that compute the moments.


#### Returns:

Two `Tensor` objects: `mean` and `variance`.
