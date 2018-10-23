

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.min_max_variable_partitioner

### `tf.min_max_variable_partitioner`

``` python
min_max_variable_partitioner(
    max_partitions=1,
    axis=0,
    min_slice_size=256 << 10,
    bytes_per_string_element=16
)
```



Defined in [`tensorflow/python/ops/partitioned_variables.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/partitioned_variables.py).

See the guide: [Variables > Variable Partitioners for Sharding](../../../api_guides/python/state_ops#Variable_Partitioners_for_Sharding)

Partitioner to allocate minimum size per slice.

Returns a partitioner that partitions the variable of given shape and dtype
such that each partition has a minimum of `min_slice_size` slice of the
variable. The maximum number of such partitions (upper bound) is given by
`max_partitions`.

#### Args:

* <b>`max_partitions`</b>: Upper bound on the number of partitions. Defaults to 1.
* <b>`axis`</b>: Axis along which to partition the variable. Defaults to 0.
* <b>`min_slice_size`</b>: Minimum size of the variable slice per partition. Defaults
    to 256K.
* <b>`bytes_per_string_element`</b>: If the `Variable` is of type string, this provides
    an estimate of how large each scalar in the `Variable` is.


#### Returns:

  A partition function usable as the `partitioner` argument to
  `variable_scope`, `get_variable`, and `get_partitioned_variable_list`.