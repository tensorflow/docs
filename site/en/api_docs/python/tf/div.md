page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.div


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L1069-L1092">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/RaggedTensor#__div__"><code>tf.RaggedTensor.__div__</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__div__"><code>tf.compat.v1.RaggedTensor.__div__</code></a>
* <a href="/api_docs/python/tf/div"><code>tf.compat.v1.div</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__div__"><code>tf.compat.v2.RaggedTensor.__div__</code></a>


``` python
tf.div(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Deprecated in favor of operator or tf.math.divide.

NOTE: Prefer using the Tensor division operator or tf.divide which obey Python
3 division operator semantics.

This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x`
and `y` are both integers then the result will be an integer. This is in
contrast to Python 3, where division with `/` is always a float while division
with `//` is always an integer.

#### Args:


* <b>`x`</b>: `Tensor` numerator of real numeric type.
* <b>`y`</b>: `Tensor` denominator of real numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` returns the quotient of x and y.
