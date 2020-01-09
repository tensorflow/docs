page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.fixed_size_partitioner


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/partitioned_variables.py#L221-L237">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Partitioner to specify a fixed number of shards along given axis.

### Aliases:

* <a href="/api_docs/python/tf/fixed_size_partitioner"><code>tf.compat.v1.fixed_size_partitioner</code></a>


``` python
tf.fixed_size_partitioner(
    num_shards,
    axis=0
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`num_shards`</b>: `int`, number of shards to partition variable.
* <b>`axis`</b>: `int`, axis to partition on.


#### Returns:

A partition function usable as the `partitioner` argument to
`variable_scope` and `get_variable`.
