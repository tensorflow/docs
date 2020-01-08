page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ensure_shape

``` python
tf.ensure_shape(
    x,
    shape,
    name=None
)
```



Defined in [`tensorflow/python/ops/check_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/check_ops.py).

Updates the shape of a tensor and checks at runtime that the shape holds.

For example:

```python
x = tf.placeholder(tf.int32)
print(x.shape)
==> TensorShape(None)
y = x * 2
print(y.shape)
==> TensorShape(None)

y = tf.ensure_shape(y, (None, 3, 3))
print(y.shape)
==> TensorShape([Dimension(None), Dimension(3), Dimension(3)])

with tf.Session() as sess:
  # Raises tf.errors.InvalidArgumentError, because the shape (3,) is not
  # compatible with the shape (None, 3, 3)
  sess.run(y, feed_dict={x: [1, 2, 3]})

```

NOTE: This differs from `Tensor.set_shape` in that it sets the static shape
of the resulting tensor and enforces it at runtime, raising an error if the
tensor's runtime shape is incompatible with the specified shape.
`Tensor.set_shape` sets the static shape of the tensor without enforcing it
at runtime, which may result in inconsistencies between the statically-known
shape of tensors and the runtime value of tensors.

#### Args:

* <b>`x`</b>: A `Tensor`.
* <b>`shape`</b>: A `TensorShape` representing the shape of this tensor, a
    `TensorShapeProto`, a list, a tuple, or None.
* <b>`name`</b>: A name for this operation (optional). Defaults to "EnsureShape".


#### Returns:

A `Tensor`. Has the same type and contents as `x`. At runtime, raises a
<a href="../tf/errors/InvalidArgumentError"><code>tf.errors.InvalidArgumentError</code></a> if `shape` is incompatible with the shape
of `x`.