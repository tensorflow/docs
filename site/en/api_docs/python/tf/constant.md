page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.constant

``` python
tf.constant(
    value,
    dtype=None,
    shape=None,
    name='Const',
    verify_shape=False
)
```



Defined in [`tensorflow/python/framework/constant_op.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/framework/constant_op.py).

Creates a constant tensor.

The resulting tensor is populated with values of type `dtype`, as
specified by arguments `value` and (optionally) `shape` (see examples
below).

The argument `value` can be a constant value, or a list of values of type
`dtype`. If `value` is a list, then the length of the list must be less
than or equal to the number of elements implied by the `shape` argument (if
specified). In the case where the list length is less than the number of
elements specified by `shape`, the last element in the list will be used
to fill the remaining entries.

The argument `shape` is optional. If present, it specifies the dimensions of
the resulting tensor. If not present, the shape of `value` is used.

If the argument `dtype` is not specified, then the type is inferred from
the type of `value`.

For example:

```python
# Constant 1-D Tensor populated with value list.
tensor = tf.constant([1, 2, 3, 4, 5, 6, 7]) => [1 2 3 4 5 6 7]

# Constant 2-D tensor populated with scalar value -1.
tensor = tf.constant(-1.0, shape=[2, 3]) => [[-1. -1. -1.]
                                             [-1. -1. -1.]]
```

<a href="../tf/constant"><code>tf.constant</code></a> differs from <a href="../tf/fill"><code>tf.fill</code></a> in a few ways:

*   <a href="../tf/constant"><code>tf.constant</code></a> supports arbitrary constants, not just uniform scalar
    Tensors like <a href="../tf/fill"><code>tf.fill</code></a>.
*   <a href="../tf/constant"><code>tf.constant</code></a> creates a `Const` node in the computation graph with the
    exact value at graph construction time. On the other hand, <a href="../tf/fill"><code>tf.fill</code></a>
    creates an Op in the graph that is expanded at runtime.
*   Because <a href="../tf/constant"><code>tf.constant</code></a> only embeds constant values in the graph, it does
    not support dynamic shapes based on other runtime Tensors, whereas
    <a href="../tf/fill"><code>tf.fill</code></a> does.

#### Args:

* <b>`value`</b>:          A constant value (or list) of output type `dtype`.

* <b>`dtype`</b>:          The type of the elements of the resulting tensor.

* <b>`shape`</b>:          Optional dimensions of resulting tensor.

* <b>`name`</b>:           Optional name for the tensor.

* <b>`verify_shape`</b>:   Boolean that enables verification of a shape of values.


#### Returns:

A Constant Tensor.


#### Raises:

* <b>`TypeError`</b>: if shape is incorrectly specified or unsupported.