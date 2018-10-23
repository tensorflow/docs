

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.broadcast_to

``` python
tf.broadcast_to(
    input,
    shape,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_array_ops.py`.

Broadcast an array for a compatible shape.

Broadcasting is the process of making arrays to have compatible shapes
for arithmetic operations. Two shapes are compatible if for each
dimension pair they are either equal or one of them is one. When trying
to broadcast a Tensor to a shape, it starts with the trailing dimensions,
and works its way forward.

For example,

```
>>> x = tf.constant([1, 2, 3])
>>> y = tf.broadcast_to(x, [3, 3])
>>> sess.run(y)
array([[1, 2, 3],
       [1, 2, 3],
       [1, 2, 3]], dtype=int32)
```
In the above example, the input Tensor with the shape of `[1, 3]`
is broadcasted to output Tensor with shape of `[3, 3]`.

#### Args:

* <b>`input`</b>: A `Tensor`. A Tensor to broadcast.
* <b>`shape`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    An 1-D `int` Tensor. The shape of the desired output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.