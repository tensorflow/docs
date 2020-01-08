page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.zeros

``` python
tf.zeros(
    shape,
    dtype=tf.float32,
    name=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/array_ops.py).

See the guide: [Constants, Sequences, and Random Values > Constant Value Tensors](../../../api_guides/python/constant_op#Constant_Value_Tensors)

Creates a tensor with all elements set to zero.

This operation returns a tensor of type `dtype` with shape `shape` and
all elements set to zero.

For example:

```python
tf.zeros([3, 4], tf.int32)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```

#### Args:

* <b>`shape`</b>: A list of integers, a tuple of integers, or a 1-D `Tensor` of type
    `int32`.
* <b>`dtype`</b>: The type of an element in the resulting `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with all elements set to zero.