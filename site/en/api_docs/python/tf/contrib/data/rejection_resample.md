page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.rejection_resample


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/data/python/ops/resampling.py#L24-L46">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A transformation that resamples a dataset to achieve a target distribution. (deprecated)

``` python
tf.contrib.data.rejection_resample(
    class_func,
    target_dist,
    initial_dist=None,
    seed=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/rejection_resample"><code>tf.data.experimental.rejection_resample(...)</code></a>.

**NOTE** Resampling is performed via rejection sampling; some fraction
of the input values will be dropped.

#### Args:


* <b>`class_func`</b>: A function mapping an element of the input dataset to a scalar
  <a href="../../../tf#int32"><code>tf.int32</code></a> tensor. Values should be in `[0, num_classes)`.
* <b>`target_dist`</b>: A floating point type tensor, shaped `[num_classes]`.
* <b>`initial_dist`</b>: (Optional.)  A floating point type tensor, shaped
  `[num_classes]`.  If not provided, the true class distribution is
  estimated live in a streaming fashion.
* <b>`seed`</b>: (Optional.) Python integer seed for the resampler.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
