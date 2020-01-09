page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.bincount


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/bincount">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L3220-L3250">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Counts the number of occurrences of each value in an integer array.

### Aliases:

* <a href="/api_docs/python/tf/math/bincount"><code>tf.bincount</code></a>
* <a href="/api_docs/python/tf/math/bincount"><code>tf.compat.v1.bincount</code></a>
* <a href="/api_docs/python/tf/math/bincount"><code>tf.compat.v1.math.bincount</code></a>


``` python
tf.math.bincount(
    arr,
    weights=None,
    minlength=None,
    maxlength=None,
    dtype=tf.dtypes.int32
)
```



<!-- Placeholder for "Used in" -->

If `minlength` and `maxlength` are not given, returns a vector with length
`tf.reduce_max(arr) + 1` if `arr` is non-empty, and length 0 otherwise.
If `weights` are non-None, then index `i` of the output stores the sum of the
value in `weights` at each index where the corresponding value in `arr` is
`i`.

#### Args:


* <b>`arr`</b>: An int32 tensor of non-negative values.
* <b>`weights`</b>: If non-None, must be the same shape as arr. For each value in
  `arr`, the bin will be incremented by the corresponding weight instead of
  1.
* <b>`minlength`</b>: If given, ensures the output has length at least `minlength`,
  padding with zeros at the end if necessary.
* <b>`maxlength`</b>: If given, skips values in `arr` that are equal or greater than
  `maxlength`, ensuring that the output has length at most `maxlength`.
* <b>`dtype`</b>: If `weights` is None, determines the type of the output bins.


#### Returns:

A vector with the same dtype as `weights` or the given `dtype`. The bin
values.
