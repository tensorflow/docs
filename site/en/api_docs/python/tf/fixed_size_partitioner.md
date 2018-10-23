


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.fixed_size_partitioner

### `tf.fixed_size_partitioner`

```
tf.fixed_size_partitioner(num_shards, axis=0)
```


See the guide: [Variables > Variable Partitioners for Sharding](../../../api_guides/python/state_ops#Variable_Partitioners_for_Sharding)

Partitioner to specify a fixed number of shards along given axis.

#### Args:

* <b>`num_shards`</b>: `int`, number of shards to partition variable.
* <b>`axis`</b>: `int`, axis to partition on.


#### Returns:

  A partition function usable as the `partitioner` argument to
  `variable_scope`, `get_variable`, and `get_partitioned_variable_list`.

Defined in [`tensorflow/python/ops/partitioned_variables.py`](https://www.tensorflow.org/code/tensorflow/python/ops/partitioned_variables.py).

