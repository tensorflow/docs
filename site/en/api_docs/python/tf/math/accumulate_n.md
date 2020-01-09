page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.accumulate_n

### Aliases:

* `tf.accumulate_n`
* `tf.math.accumulate_n`

``` python
tf.math.accumulate_n(
    inputs,
    shape=None,
    tensor_dtype=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/math_ops.py).

Returns the element-wise sum of a list of tensors.

Optionally, pass `shape` and `tensor_dtype` for shape and type checking,
otherwise, these are inferred.

<a href="../../tf/math/accumulate_n"><code>tf.math.accumulate_n</code></a> performs the same operation as <a href="../../tf/math/add_n"><code>tf.add_n</code></a>, but does not
wait for all of its inputs to be ready before beginning to sum. This can
save memory if inputs are ready at different times, since minimum temporary
storage is proportional to the output size rather than the inputs size.

`accumulate_n` is differentiable (but wasn't previous to TensorFlow 1.7).

For example:

```python
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 0], [0, 6]])
tf.math.accumulate_n([a, b, a])  # [[7, 4], [6, 14]]

# Explicitly pass shape and type
tf.math.accumulate_n([a, b, a], shape=[2, 2], tensor_dtype=tf.int32)
                                                               # [[7,  4],
                                                               #  [6, 14]]
```

#### Args:

* <b>`inputs`</b>: A list of `Tensor` objects, each with same shape and type.
* <b>`shape`</b>: Shape of elements of `inputs`.
* <b>`tensor_dtype`</b>: The type of `inputs`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of same shape and type as the elements of `inputs`.


#### Raises:

* <b>`ValueError`</b>: If `inputs` don't all have same shape and dtype or the shape
  cannot be inferred.