page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ConfigProto

## Class `ConfigProto`





### Aliases:

* Class `tf.ConfigProto`
* Class `tf.compat.v1.ConfigProto`



Defined in [`core/protobuf/config.proto`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/core/protobuf/config.proto).

<!-- Placeholder for "Used in" -->


## Child Classes
[`class DeviceCountEntry`](../tf/ConfigProto/DeviceCountEntry)

[`class Experimental`](../tf/ConfigProto/Experimental)

## Properties

<h3 id="allow_soft_placement"><code>allow_soft_placement</code></h3>

`bool allow_soft_placement`


<h3 id="cluster_def"><code>cluster_def</code></h3>

`ClusterDef cluster_def`


<h3 id="device_count"><code>device_count</code></h3>

`repeated DeviceCountEntry device_count`


<h3 id="device_filters"><code>device_filters</code></h3>

`repeated string device_filters`


<h3 id="experimental"><code>experimental</code></h3>

`Experimental experimental`


<h3 id="gpu_options"><code>gpu_options</code></h3>

`GPUOptions gpu_options`


<h3 id="graph_options"><code>graph_options</code></h3>

`GraphOptions graph_options`


<h3 id="inter_op_parallelism_threads"><code>inter_op_parallelism_threads</code></h3>

`int32 inter_op_parallelism_threads`


<h3 id="intra_op_parallelism_threads"><code>intra_op_parallelism_threads</code></h3>

`int32 intra_op_parallelism_threads`


<h3 id="isolate_session_state"><code>isolate_session_state</code></h3>

`bool isolate_session_state`


<h3 id="log_device_placement"><code>log_device_placement</code></h3>

`bool log_device_placement`


<h3 id="operation_timeout_in_ms"><code>operation_timeout_in_ms</code></h3>

`int64 operation_timeout_in_ms`


<h3 id="placement_period"><code>placement_period</code></h3>

`int32 placement_period`


<h3 id="rpc_options"><code>rpc_options</code></h3>

`RPCOptions rpc_options`


<h3 id="session_inter_op_thread_pool"><code>session_inter_op_thread_pool</code></h3>

`repeated ThreadPoolOptionProto session_inter_op_thread_pool`


<h3 id="use_per_session_threads"><code>use_per_session_threads</code></h3>

`bool use_per_session_threads`




