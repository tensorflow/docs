

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.sets.set_size

### `tf.contrib.metrics.set_size`
### `tf.sets.set_size`

``` python
set_size(
    a,
    validate_indices=True
)
```



Defined in [`tensorflow/python/ops/sets_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/sets_impl.py).

See the guide: [Metrics (contrib) > Set `Ops`](../../../../api_guides/python/contrib.metrics#Set_Ops_)

Compute number of unique elements along last dimension of `a`.

#### Args:

* <b>`a`</b>: `SparseTensor`, with indices sorted in row-major order.
* <b>`validate_indices`</b>: Whether to validate the order and range of sparse indices
     in `a`.


#### Returns:

  `int32` `Tensor` of set sizes. For `a` ranked `n`, this is a `Tensor` with
  rank `n-1`, and the same 1st `n-1` dimensions as `a`. Each value is the
  number of unique elements in the corresponding `[0...n-1]` dimension of `a`.


#### Raises:

* <b>`TypeError`</b>: If `a` is an invalid types.