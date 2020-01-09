page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.l2_normalize


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/l2_normalize">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_impl.py#L591-L616">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Normalizes along dimension `axis` using an L2 norm. (deprecated arguments)

### Aliases:

* <a href="/api_docs/python/tf/math/l2_normalize"><code>tf.compat.v1.linalg.l2_normalize</code></a>
* <a href="/api_docs/python/tf/math/l2_normalize"><code>tf.compat.v1.math.l2_normalize</code></a>
* <a href="/api_docs/python/tf/math/l2_normalize"><code>tf.compat.v1.nn.l2_normalize</code></a>
* <a href="/api_docs/python/tf/math/l2_normalize"><code>tf.linalg.l2_normalize</code></a>
* <a href="/api_docs/python/tf/math/l2_normalize"><code>tf.nn.l2_normalize</code></a>


``` python
tf.math.l2_normalize(
    x,
    axis=None,
    epsilon=1e-12,
    name=None,
    dim=None
)
```



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dim)`. They will be removed in a future version.
Instructions for updating:
dim is deprecated, use axis instead

For a 1-D tensor with `axis = 0`, computes

    output = x / sqrt(max(sum(x**2), epsilon))

For `x` with more dimensions, independently normalizes each 1-D slice along
dimension `axis`.

#### Args:


* <b>`x`</b>: A `Tensor`.
* <b>`axis`</b>: Dimension along which to normalize.  A scalar or a vector of
  integers.
* <b>`epsilon`</b>: A lower bound value for the norm. Will use `sqrt(epsilon)` as the
  divisor if `norm < sqrt(epsilon)`.
* <b>`name`</b>: A name for this operation (optional).
* <b>`dim`</b>: Deprecated alias for axis.


#### Returns:

A `Tensor` with the same shape as `x`.
