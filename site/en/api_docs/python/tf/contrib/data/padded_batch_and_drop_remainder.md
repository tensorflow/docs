

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.padded_batch_and_drop_remainder

``` python
padded_batch_and_drop_remainder(
    batch_size,
    padded_shapes,
    padding_values=None
)
```



Defined in [`tensorflow/contrib/data/python/ops/batching.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/data/python/ops/batching.py).

A batching and padding transformation that omits the final small batch.

Like <a href="../../../tf/data/Dataset#padded_batch"><code>tf.data.Dataset.padded_batch</code></a>, this transformation combines
consecutive elements of this dataset into batches. However, if the batch
size does not evenly divide the input dataset size, this transformation will
drop the final smaller element.

See `<a href="../../../tf/contrib/data/batch_and_drop_remainder"><code>tf.contrib.data.batch_and_drop_remainder</code></a>` for more details.

#### Args:

* <b>`batch_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the number of
    consecutive elements of this dataset to combine in a single batch.
* <b>`padded_shapes`</b>: A nested structure of `tf.TensorShape` or
    `tf.int64` vector tensor-like objects. See
    <a href="../../../tf/data/Dataset#padded_batch"><code>tf.data.Dataset.padded_batch</code></a> for details.
* <b>`padding_values`</b>: (Optional.) A nested structure of scalar-shaped
    `tf.Tensor`. See <a href="../../../tf/data/Dataset#padded_batch"><code>tf.data.Dataset.padded_batch</code></a> for details.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>