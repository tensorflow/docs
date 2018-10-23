

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.dense_to_sparse_batch

``` python
dense_to_sparse_batch(
    batch_size,
    row_shape
)
```



Defined in [`tensorflow/contrib/data/python/ops/batching.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/data/python/ops/batching.py).

A transformation that batches ragged elements into `tf.SparseTensor`s.

Like `Dataset.padded_batch()`, this transformation combines multiple
consecutive elements of the dataset, which might have different
shapes, into a single element. The resulting element has three
components (`indices`, `values`, and `dense_shape`), which
comprise a `tf.SparseTensor` that represents the same data. The
`row_shape` represents the dense shape of each row in the
resulting `tf.SparseTensor`, to which the effective batch size is
prepended. For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }

a.apply(tf.contrib.data.dense_to_sparse_batch(batch_size=2, row_shape=[6])) ==
{
    ([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]],  # indices
     ['a', 'b', 'c', 'a', 'b'],                 # values
     [2, 6]),                                   # dense_shape
    ([[0, 0], [0, 1], [0, 2], [0, 3]],
     ['a', 'b', 'c', 'd'],
     [1, 6])
}
```

#### Args:

* <b>`batch_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the
    number of consecutive elements of this dataset to combine in a
    single batch.
* <b>`row_shape`</b>: A `tf.TensorShape` or `tf.int64` vector tensor-like
    object representing the equivalent dense shape of a row in the
    resulting `tf.SparseTensor`. Each element of this dataset must
    have the same rank as `row_shape`, and must have size less
    than or equal to `row_shape` in each dimension.


#### Returns:

A `Dataset` transformation function, which can be passed to
[`tf.data.Dataset.apply`](../../../tf/data/Dataset#apply).