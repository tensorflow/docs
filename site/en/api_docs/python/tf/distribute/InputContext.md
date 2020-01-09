page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.InputContext


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/distribute_lib.py#L343-L404">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `InputContext`

A class wrapping information needed by an input function.



### Aliases:

* Class `tf.compat.v1.distribute.InputContext`
* Class `tf.compat.v2.distribute.InputContext`


<!-- Placeholder for "Used in" -->

This is a context class that is passed to the user's input function and
contains information about the compute replicas and input pipelines. The
number of compute replicas (in sync training) helps compute the local batch
size from the desired global batch size for each replica. The input pipeline
information can be used to return a different subset of the input in each
replica (for e.g. shard the input pipeline, use a different input
source etc).

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/distribute_lib.py#L355-L369">View source</a>

``` python
__init__(
    num_input_pipelines=1,
    input_pipeline_id=0,
    num_replicas_in_sync=1
)
```

Initializes an InputContext object.


#### Args:


* <b>`num_input_pipelines`</b>: the number of input pipelines in a cluster.
* <b>`input_pipeline_id`</b>: the current input pipeline id, should be an int in
  [0,`num_input_pipelines`).
* <b>`num_replicas_in_sync`</b>: the number of replicas that are in sync.



## Properties

<h3 id="input_pipeline_id"><code>input_pipeline_id</code></h3>

Returns the input pipeline ID.


<h3 id="num_input_pipelines"><code>num_input_pipelines</code></h3>

Returns the number of input pipelines.


<h3 id="num_replicas_in_sync"><code>num_replicas_in_sync</code></h3>

Returns the number of compute replicas in sync.




## Methods

<h3 id="get_per_replica_batch_size"><code>get_per_replica_batch_size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/distribute_lib.py#L386-L404">View source</a>

``` python
get_per_replica_batch_size(global_batch_size)
```

Returns the per-replica batch size.


#### Args:


* <b>`global_batch_size`</b>: the global batch size which should be divisible by
  `num_replicas_in_sync`.


#### Returns:

the per-replica batch size.



#### Raises:


* <b>`ValueError`</b>: if `global_batch_size` not divisible by
  `num_replicas_in_sync`.
