page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.histogram_fixed_width

``` python
tf.histogram_fixed_width(
    values,
    value_range,
    nbins=100,
    dtype=tf.int32,
    name=None
)
```



Defined in [`tensorflow/python/ops/histogram_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/histogram_ops.py).

Return histogram of values.

Given the tensor `values`, this operation returns a rank 1 histogram counting
the number of entries in `values` that fell into every bin.  The bins are
equal width and determined by the arguments `value_range` and `nbins`.

#### Args:

* <b>`values`</b>:  Numeric `Tensor`.
* <b>`value_range`</b>:  Shape [2] `Tensor` of same `dtype` as `values`.
    values <= value_range[0] will be mapped to hist[0],
    values >= value_range[1] will be mapped to hist[-1].
* <b>`nbins`</b>:  Scalar `int32 Tensor`.  Number of histogram bins.
* <b>`dtype`</b>:  dtype for returned histogram.
* <b>`name`</b>:  A name for this operation (defaults to 'histogram_fixed_width').


#### Returns:

  A 1-D `Tensor` holding histogram of values.

Examples:

```python
# Bins will be:  (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
nbins = 5
value_range = [0.0, 5.0]
new_values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]

with tf.get_default_session() as sess:
  hist = tf.histogram_fixed_width(new_values, value_range, nbins=5)
  variables.global_variables_initializer().run()
  sess.run(hist) => [2, 1, 1, 0, 2]
```