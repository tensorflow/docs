page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.invert_permutation


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/invert_permutation">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Computes the inverse permutation of a tensor.

### Aliases:

* <a href="/api_docs/python/tf/math/invert_permutation"><code>tf.compat.v1.invert_permutation</code></a>
* <a href="/api_docs/python/tf/math/invert_permutation"><code>tf.compat.v1.math.invert_permutation</code></a>
* <a href="/api_docs/python/tf/math/invert_permutation"><code>tf.compat.v2.math.invert_permutation</code></a>
* <a href="/api_docs/python/tf/math/invert_permutation"><code>tf.invert_permutation</code></a>


``` python
tf.math.invert_permutation(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation computes the inverse of an index permutation. It takes a 1-D
integer tensor `x`, which represents the indices of a zero-based array, and
swaps each value with its index position. In other words, for an output tensor
`y` and an input tensor `x`, this operation computes the following:

`y[x[i]] = i for i in [0, 1, ..., len(x) - 1]`

The values must include 0. There can be no duplicate values or negative values.

#### For example:



```
# tensor `x` is [3, 4, 0, 2, 1]
invert_permutation(x) ==> [2, 4, 3, 0, 1]
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`. 1-D.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
