page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.histogram


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/histogram/summary_v2.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Write a histogram summary.

### Aliases:

* `tf.compat.v2.summary.histogram`


``` python
tf.summary.histogram(
    name,
    data,
    step=None,
    buckets=None,
    description=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`name`</b>: A name for this summary. The summary tag used for TensorBoard will
  be this name prefixed by any active name scopes.
* <b>`data`</b>: A `Tensor` of any shape. Must be castable to `float64`.
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to <a href="../../tf/summary/experimental/get_step"><code>tf.summary.experimental.get_step()</code></a>, which must
  not be None.
* <b>`buckets`</b>: Optional positive `int`. The output will have this
  many buckets, except in two edge cases. If there is no data, then
  there are no buckets. If there is data but all points have the
  same value, then there is one bucket whose left and right
  endpoints are the same.
* <b>`description`</b>: Optional long-form description for this summary, as a
  constant `str`. Markdown is supported. Defaults to empty.


#### Returns:

True on success, or false if no summary was emitted because no default
summary writer was available.



#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  <a href="../../tf/summary/experimental/get_step"><code>tf.summary.experimental.get_step()</code></a> is None.
