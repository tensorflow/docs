page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.slice


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L817-L866">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Extracts a slice from a tensor.

### Aliases:

* `tf.compat.v1.slice`
* `tf.compat.v2.slice`


``` python
tf.slice(
    input_,
    begin,
    size,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation extracts a slice of size `size` from a tensor `input_` starting
at the location specified by `begin`. The slice `size` is represented as a
tensor shape, where `size[i]` is the number of elements of the 'i'th dimension
of `input_` that you want to slice. The starting location (`begin`) for the
slice is represented as an offset in each dimension of `input_`. In other
words, `begin[i]` is the offset into the i'th dimension of `input_` that you
want to slice from.

Note that <a href="../tf/Tensor#__getitem__"><code>tf.Tensor.__getitem__</code></a> is typically a more pythonic way to
perform slices, as it allows you to write `foo[3:7, :-2]` instead of
`tf.slice(foo, [3, 0], [4, foo.get_shape()[1]-2])`.

`begin` is zero-based; `size` is one-based. If `size[i]` is -1,
all remaining elements in dimension i are included in the
slice. In other words, this is equivalent to setting:

`size[i] = input_.dim_size(i) - begin[i]`

This operation requires that:

`0 <= begin[i] <= begin[i] + size[i] <= Di  for i in [0, n]`

#### For example:



```python
t = tf.constant([[[1, 1, 1], [2, 2, 2]],
                 [[3, 3, 3], [4, 4, 4]],
                 [[5, 5, 5], [6, 6, 6]]])
tf.slice(t, [1, 0, 0], [1, 1, 3])  # [[[3, 3, 3]]]
tf.slice(t, [1, 0, 0], [1, 2, 3])  # [[[3, 3, 3],
                                   #   [4, 4, 4]]]
tf.slice(t, [1, 0, 0], [2, 1, 3])  # [[[3, 3, 3]],
                                   #  [[5, 5, 5]]]
```

#### Args:


* <b>`input_`</b>: A `Tensor`.
* <b>`begin`</b>: An `int32` or `int64` `Tensor`.
* <b>`size`</b>: An `int32` or `int64` `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` the same type as `input_`.
