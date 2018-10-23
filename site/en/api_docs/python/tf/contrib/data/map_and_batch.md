

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.map_and_batch

``` python
tf.contrib.data.map_and_batch(
    map_func,
    batch_size,
    num_parallel_batches=1
)
```



Defined in [`tensorflow/contrib/data/python/ops/batching.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/data/python/ops/batching.py).

See the guide: [Dataset Input Pipeline > Transformations on existing datasets](../../../../../api_guides/python/input_dataset#Transformations_on_existing_datasets)

Fused implementation of `map` and `batch`.

Maps `map_func` across `batch_size` consecutive elements of this dataset
and then combines them into a batch. Functionally, it is equivalent to `map`
followed by `batch`. However, by fusing the two transformations together, the
implementation can be more efficient. Surfacing this transformation in the API
is temporary. Once automatic input pipeline optimization is implemented,
the fusing of `map` and `batch` will happen automatically and this API will be
deprecated.

#### Args:

* <b>`map_func`</b>: A function mapping a nested structure of tensors to another
    nested structure of tensors.
* <b>`batch_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the number of
    consecutive elements of this dataset to combine in a single batch.
* <b>`num_parallel_batches`</b>: A `tf.int64` scalar `tf.Tensor`, representing the
    number of batches to create in parallel. On one hand, higher values can
    help mitigate the effect of stragglers. On the other hand, higher values
    can increase contention if CPU is scarce.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.