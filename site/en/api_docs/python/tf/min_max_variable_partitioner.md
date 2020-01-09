page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.min_max_variable_partitioner


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/partitioned_variables.py#L157-L218">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Partitioner to allocate minimum size per slice.

### Aliases:

* <a href="/api_docs/python/tf/min_max_variable_partitioner"><code>tf.compat.v1.min_max_variable_partitioner</code></a>


``` python
tf.min_max_variable_partitioner(
    max_partitions=1,
    axis=0,
    min_slice_size=(256 << 10),
    bytes_per_string_element=16
)
```



<!-- Placeholder for "Used in" -->

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
`variable_scope` and `get_variable`.
