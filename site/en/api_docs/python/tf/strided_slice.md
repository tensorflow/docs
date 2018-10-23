

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strided_slice

``` python
tf.strided_slice(
    input_,
    begin,
    end,
    strides=None,
    begin_mask=0,
    end_mask=0,
    ellipsis_mask=0,
    new_axis_mask=0,
    shrink_axis_mask=0,
    var=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/array_ops.py).

See the guide: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining)

Extracts a strided slice of a tensor (generalized python array indexing).

**Instead of calling this op directly most users will want to use the
NumPy-style slicing syntax (e.g. `tensor[..., 3:4:-1, tf.newaxis, 3]`), which
is supported via <a href="../tf/Tensor#__getitem__"><code>tf.Tensor.__getitem__</code></a> and <a href="../tf/Variable#__getitem__"><code>tf.Variable.__getitem__</code></a>.**
The interface of this op is a low-level encoding of the slicing syntax.

Roughly speaking, this op extracts a slice of size `(end-begin)/stride`
from the given `input_` tensor. Starting at the location specified by `begin`
the slice continues by adding `stride` to the index until all dimensions are
not less than `end`.
Note that a stride can be negative, which causes a reverse slice.

Given a Python slice `input[spec0, spec1, ..., specn]`,
this function will be called as follows.

`begin`, `end`, and `strides` will be vectors of length n.
n in general is not equal to the rank of the `input_` tensor.

In each mask field (`begin_mask`, `end_mask`, `ellipsis_mask`,
`new_axis_mask`, `shrink_axis_mask`) the ith bit will correspond to
the ith spec.

If the ith bit of `begin_mask` is set, `begin[i]` is ignored and
the fullest possible range in that dimension is used instead.
`end_mask` works analogously, except with the end range.

`foo[5:,:,:3]` on a 7x8x9 tensor is equivalent to `foo[5:7,0:8,0:3]`.
`foo[::-1]` reverses a tensor with shape 8.

If the ith bit of `ellipsis_mask` is set, as many unspecified dimensions
as needed will be inserted between other dimensions. Only one
non-zero bit is allowed in `ellipsis_mask`.

For example `foo[3:5,...,4:5]` on a shape 10x3x3x10 tensor is
equivalent to `foo[3:5,:,:,4:5]` and
`foo[3:5,...]` is equivalent to `foo[3:5,:,:,:]`.

If the ith bit of `new_axis_mask` is set, then `begin`,
`end`, and `stride` are ignored and a new length 1 dimension is
added at this point in the output tensor.

For example,
`foo[:4, tf.newaxis, :2]` would produce a shape `(4, 1, 2)` tensor.

If the ith bit of `shrink_axis_mask` is set, it implies that the ith
specification shrinks the dimensionality by 1. `begin[i]`, `end[i]` and
`strides[i]` must imply a slice of size 1 in the dimension. For example in
Python one might do `foo[:, 3, :]` which would result in
`shrink_axis_mask` equal to 2.


NOTE: `begin` and `end` are zero-indexed.
`strides` entries must be non-zero.


```python
t = tf.constant([[[1, 1, 1], [2, 2, 2]],
                 [[3, 3, 3], [4, 4, 4]],
                 [[5, 5, 5], [6, 6, 6]]])
tf.strided_slice(t, [1, 0, 0], [2, 1, 3], [1, 1, 1])  # [[[3, 3, 3]]]
tf.strided_slice(t, [1, 0, 0], [2, 2, 3], [1, 1, 1])  # [[[3, 3, 3],
                                                      #   [4, 4, 4]]]
tf.strided_slice(t, [1, -1, 0], [2, -3, 3], [1, -1, 1])  # [[[4, 4, 4],
                                                         #   [3, 3, 3]]]
```

#### Args:

* <b>`input_`</b>: A `Tensor`.
* <b>`begin`</b>: An `int32` or `int64` `Tensor`.
* <b>`end`</b>: An `int32` or `int64` `Tensor`.
* <b>`strides`</b>: An `int32` or `int64` `Tensor`.
* <b>`begin_mask`</b>: An `int32` mask.
* <b>`end_mask`</b>: An `int32` mask.
* <b>`ellipsis_mask`</b>: An `int32` mask.
* <b>`new_axis_mask`</b>: An `int32` mask.
* <b>`shrink_axis_mask`</b>: An `int32` mask.
* <b>`var`</b>: The variable corresponding to `input_` or None
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` the same type as `input`.