page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.fixed_size_partitioner

Partitioner to specify a fixed number of shards along given axis.

### Aliases:

* `tf.compat.v1.fixed_size_partitioner`
* `tf.fixed_size_partitioner`

``` python
tf.fixed_size_partitioner(
    num_shards,
    axis=0
)
```



Defined in [`python/ops/partitioned_variables.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/partitioned_variables.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`num_shards`</b>: `int`, number of shards to partition variable.
* <b>`axis`</b>: `int`, axis to partition on.


#### Returns:

A partition function usable as the `partitioner` argument to
`variable_scope` and `get_variable`.
