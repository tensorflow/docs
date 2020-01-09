page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.histogram_fixed_width


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/histogram_fixed_width">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/histogram_ops.py#L103-L150">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return histogram of values.

### Aliases:

* <a href="/api_docs/python/tf/histogram_fixed_width"><code>tf.compat.v1.histogram_fixed_width</code></a>
* <a href="/api_docs/python/tf/histogram_fixed_width"><code>tf.compat.v2.histogram_fixed_width</code></a>


``` python
tf.histogram_fixed_width(
    values,
    value_range,
    nbins=100,
    dtype=tf.dtypes.int32,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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



#### Raises:


* <b>`TypeError`</b>: If any unsupported dtype is provided.
* <b><a href="/api_docs/python/tf/errors/InvalidArgumentError"><code>tf.errors.InvalidArgumentError</code></a></b>: If value_range does not
    satisfy value_range[0] < value_range[1].


#### Examples:



```python
# Bins will be:  (-inf, 1), [1, 2), [2, 3), [3, 4), [4, inf)
nbins = 5
value_range = [0.0, 5.0]
new_values = [-1.0, 0.0, 1.5, 2.0, 5.0, 15]

with tf.compat.v1.get_default_session() as sess:
  hist = tf.histogram_fixed_width(new_values, value_range, nbins=5)
  variables.global_variables_initializer().run()
  sess.run(hist) => [2, 1, 1, 0, 2]
```
