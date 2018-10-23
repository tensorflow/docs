

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.fixed_size_partitioner

``` python
tf.fixed_size_partitioner(
    num_shards,
    axis=0
)
```



Defined in [`tensorflow/python/ops/partitioned_variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/ops/partitioned_variables.py).

See the guide: [Variables > Variable Partitioners for Sharding](../../../api_guides/python/state_ops#Variable_Partitioners_for_Sharding)

Partitioner to specify a fixed number of shards along given axis.

#### Args:

* <b>`num_shards`</b>: `int`, number of shards to partition variable.
* <b>`axis`</b>: `int`, axis to partition on.


#### Returns:

A partition function usable as the `partitioner` argument to
`variable_scope`, `get_variable`, and `get_partitioned_variable_list`.