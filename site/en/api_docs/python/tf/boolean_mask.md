

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.boolean_mask

``` python
tf.boolean_mask(
    tensor,
    mask,
    name='boolean_mask',
    axis=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/ops/array_ops.py).

See the guide: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining)

Apply boolean mask to tensor.  Numpy equivalent is `tensor[mask]`.

```python
# 1-D example
tensor = [0, 1, 2, 3]
mask = np.array([True, False, True, False])
boolean_mask(tensor, mask)  # [0, 2]
```

In general, `0 < dim(mask) = K <= dim(tensor)`, and `mask`'s shape must match
the first K dimensions of `tensor`'s shape.  We then have:
  `boolean_mask(tensor, mask)[i, j1,...,jd] = tensor[i1,...,iK,j1,...,jd]`
where `(i1,...,iK)` is the ith `True` entry of `mask` (row-major order).
The `axis` could be used with `mask` to indicate the axis to mask from.
In that case, `axis + dim(mask) <= dim(tensor)` and `mask`'s shape must match
the first `axis + dim(mask)` dimensions of `tensor`'s shape.

#### Args:

* <b>`tensor`</b>:  N-D tensor.
* <b>`mask`</b>:  K-D boolean tensor, K <= N and K must be known statically.
* <b>`name`</b>:  A name for this operation (optional).
* <b>`axis`</b>:  A 0-D int Tensor representing the axis in `tensor` to mask from.
    By default, axis is 0 which will mask from the first dimension. Otherwise
    K + axis <= N.


#### Returns:

(N-K+1)-dimensional tensor populated by entries in `tensor` corresponding
to `True` values in `mask`.


#### Raises:

* <b>`ValueError`</b>:  If shapes do not conform.

Examples:

```python
# 2-D example
tensor = [[1, 2], [3, 4], [5, 6]]
mask = np.array([True, False, True])
boolean_mask(tensor, mask)  # [[1, 2], [5, 6]]
```