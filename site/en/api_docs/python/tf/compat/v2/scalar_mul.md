page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.scalar_mul


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L427-L431">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

### Aliases:

* <a href="/api_docs/python/tf/compat/v2/scalar_mul"><code>tf.compat.v2.math.scalar_mul</code></a>


``` python
tf.compat.v2.scalar_mul(
    scalar,
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Intended for use in gradient code which might deal with `IndexedSlices`
objects, which are easy to multiply by a scalar but more expensive to
multiply with arbitrary tensors.

#### Args:


* <b>`scalar`</b>: A 0-D scalar `Tensor`. Must have known shape.
* <b>`x`</b>: A `Tensor` or `IndexedSlices` to be scaled.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`scalar * x` of the same type (`Tensor` or `IndexedSlices`) as `x`.



#### Raises:


* <b>`ValueError`</b>: if scalar is not a 0-D `scalar`.
