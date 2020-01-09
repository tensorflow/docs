page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.sufficient_statistics


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_impl.py#L1118-L1144">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Calculate the sufficient statistics for the mean and variance of `x`.

### Aliases:

* `tf.compat.v2.nn.sufficient_statistics`


``` python
tf.nn.sufficient_statistics(
    x,
    axes,
    shift=None,
    keepdims=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

These sufficient statistics are computed using the one pass algorithm on
an input that's optionally shifted. See:
https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Computing_shifted_data

#### Args:


* <b>`x`</b>: A `Tensor`.
* <b>`axes`</b>: Array of ints. Axes along which to compute mean and variance.
* <b>`shift`</b>: A `Tensor` containing the value by which to shift the data for
  numerical stability, or `None` if no shift is to be performed. A shift
  close to the true mean provides the most numerically stable results.
* <b>`keepdims`</b>: produce statistics with the same dimensionality as the input.
* <b>`name`</b>: Name used to scope the operations that compute the sufficient stats.


#### Returns:

Four `Tensor` objects of the same type as `x`:

* the count (number of elements to average over).
* the (possibly shifted) sum of the elements in the array.
* the (possibly shifted) sum of squares of the elements in the array.
* the shift by which the mean must be corrected or None if `shift` is None.
