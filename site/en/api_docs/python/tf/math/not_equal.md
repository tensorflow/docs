page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.not_equal


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/not_equal">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L1309-L1325">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the truth value of (x != y) element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/not_equal"><code>tf.compat.v1.math.not_equal</code></a>
* <a href="/api_docs/python/tf/math/not_equal"><code>tf.compat.v1.not_equal</code></a>
* <a href="/api_docs/python/tf/math/not_equal"><code>tf.compat.v2.math.not_equal</code></a>
* <a href="/api_docs/python/tf/math/not_equal"><code>tf.compat.v2.not_equal</code></a>
* <a href="/api_docs/python/tf/math/not_equal"><code>tf.not_equal</code></a>


``` python
tf.math.not_equal(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

**NOTE**: `NotEqual` supports broadcasting. More about broadcasting [here](
https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`y`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type bool with the same size as that of x or y.
