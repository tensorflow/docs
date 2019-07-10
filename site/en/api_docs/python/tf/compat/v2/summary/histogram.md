page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.histogram

Write a histogram summary.

``` python
tf.compat.v2.summary.histogram(
    name,
    data,
    step=None,
    buckets=None,
    description=None
)
```



Defined in [`plugins/histogram/summary_v2.py`](https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/histogram/summary_v2.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`name`</b>: A name for this summary. The summary tag used for TensorBoard will
  be this name prefixed by any active name scopes.
* <b>`data`</b>: A `Tensor` of any shape. Must be castable to `float64`.
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to `tf.summary.experimental.get_step()`, which must
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
  `tf.summary.experimental.get_step()` is None.