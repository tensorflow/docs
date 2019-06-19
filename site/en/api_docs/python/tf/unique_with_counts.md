page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.unique_with_counts

``` python
tf.unique_with_counts(
    x,
    out_idx=tf.int32,
    name=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/array_ops.py).

See the guide: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining)

Finds unique elements in a 1-D tensor.

This operation returns a tensor `y` containing all of the unique elements of `x`
sorted in the same order that they occur in `x`. This operation also returns a
tensor `idx` the same size as `x` that contains the index of each value of `x`
in the unique output `y`. Finally, it returns a third tensor `count` that
contains the count of each element of `y` in `x`. In other words:

`y[idx[i]] = x[i] for i in [0, 1,...,rank(x) - 1]`

For example:

```
# tensor 'x' is [1, 1, 2, 4, 4, 4, 7, 8, 8]
y, idx, count = unique_with_counts(x)
y ==> [1, 2, 4, 7, 8]
idx ==> [0, 0, 1, 2, 2, 2, 3, 4, 4]
count ==> [2, 1, 3, 1, 2]
```

#### Args:

* <b>`x`</b>: A `Tensor`. 1-D.
* <b>`out_idx`</b>: An optional <a href="../tf/DType"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../tf/int32"><code>tf.int32</code></a>.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (y, idx, count).

* <b>`y`</b>: A `Tensor`. Has the same type as `x`.
* <b>`idx`</b>: A `Tensor` of type `out_idx`.
* <b>`count`</b>: A `Tensor` of type `out_idx`.