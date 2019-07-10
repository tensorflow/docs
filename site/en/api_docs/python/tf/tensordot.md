page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tensordot

Tensor contraction of a and b along specified axes.

### Aliases:

* `tf.compat.v1.linalg.tensordot`
* `tf.compat.v1.tensordot`
* `tf.compat.v2.linalg.tensordot`
* `tf.compat.v2.tensordot`
* `tf.linalg.tensordot`
* `tf.tensordot`

``` python
tf.tensordot(
    a,
    b,
    axes,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Tensordot (also known as tensor contraction) sums the product of elements
from `a` and `b` over the indices specified by `a_axes` and `b_axes`.
The lists `a_axes` and `b_axes` specify those pairs of axes along which to
contract the tensors. The axis `a_axes[i]` of `a` must have the same dimension
as axis `b_axes[i]` of `b` for all `i` in `range(0, len(a_axes))`. The lists
`a_axes` and `b_axes` must have identical length and consist of unique
integers that specify valid axes for each of the tensors.

This operation corresponds to `numpy.tensordot(a, b, axes)`.

Example 1: When `a` and `b` are matrices (order 2), the case `axes = 1`
is equivalent to matrix multiplication.

Example 2: When `a` and `b` are matrices (order 2), the case
`axes = [[1], [0]]` is equivalent to matrix multiplication.

Example 3: Suppose that \\(a_{ijk}\\) and \\(b_{lmn}\\) represent two
tensors of order 3. Then, `contract(a, b, [[0], [2]])` is the order 4 tensor
\\(c_{jklm}\\) whose entry
corresponding to the indices \\((j,k,l,m)\\) is given by:

\\( c_{jklm} = \sum_i a_{ijk} b_{lmi} \\).

In general, `order(c) = order(a) + order(b) - 2*len(axes[0])`.

#### Args:


* <b>`a`</b>: `Tensor` of type `float32` or `float64`.
* <b>`b`</b>: `Tensor` with the same type as `a`.
* <b>`axes`</b>: Either a scalar `N`, or a list or an `int32` `Tensor` of shape [2, k].
  If axes is a scalar, sum over the last N axes of a and the first N axes of
  b in order. If axes is a list or `Tensor` the first and second row contain
  the set of unique integers specifying axes along which the contraction is
  computed, for `a` and `b`, respectively. The number of axes for `a` and
  `b` must be equal.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with the same type as `a`.



#### Raises:


* <b>`ValueError`</b>: If the shapes of `a`, `b`, and `axes` are incompatible.
* <b>`IndexError`</b>: If the values in axes exceed the rank of the corresponding
  tensor.