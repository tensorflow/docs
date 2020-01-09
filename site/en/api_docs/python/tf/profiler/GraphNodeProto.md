page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.profiler.GraphNodeProto


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/core/profiler/tfprof_output.proto">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GraphNodeProto`

A ProtocolMessage



### Aliases:

* Class <a href="/api_docs/python/tf/profiler/GraphNodeProto"><code>tf.compat.v1.profiler.GraphNodeProto</code></a>


<!-- Placeholder for "Used in" -->


## Child Classes
[`class InputShapesEntry`](../../tf/profiler/GraphNodeProto/InputShapesEntry)

## Properties

<h3 id="accelerator_exec_micros"><code>accelerator_exec_micros</code></h3>

`int64 accelerator_exec_micros`


<h3 id="children"><code>children</code></h3>

`repeated GraphNodeProto children`


<h3 id="cpu_exec_micros"><code>cpu_exec_micros</code></h3>

`int64 cpu_exec_micros`


<h3 id="devices"><code>devices</code></h3>

`repeated string devices`


<h3 id="exec_micros"><code>exec_micros</code></h3>

`int64 exec_micros`


<h3 id="float_ops"><code>float_ops</code></h3>

`int64 float_ops`


<h3 id="input_shapes"><code>input_shapes</code></h3>

`repeated InputShapesEntry input_shapes`


<h3 id="name"><code>name</code></h3>

`string name`


<h3 id="output_bytes"><code>output_bytes</code></h3>

`int64 output_bytes`


<h3 id="parameters"><code>parameters</code></h3>

`int64 parameters`


<h3 id="peak_bytes"><code>peak_bytes</code></h3>

`int64 peak_bytes`


<h3 id="requested_bytes"><code>requested_bytes</code></h3>

`int64 requested_bytes`


<h3 id="residual_bytes"><code>residual_bytes</code></h3>

`int64 residual_bytes`


<h3 id="run_count"><code>run_count</code></h3>

`int64 run_count`


<h3 id="shapes"><code>shapes</code></h3>

`repeated TensorShapeProto shapes`


<h3 id="tensor_value"><code>tensor_value</code></h3>

`TFProfTensorProto tensor_value`


<h3 id="total_accelerator_exec_micros"><code>total_accelerator_exec_micros</code></h3>

`int64 total_accelerator_exec_micros`


<h3 id="total_cpu_exec_micros"><code>total_cpu_exec_micros</code></h3>

`int64 total_cpu_exec_micros`


<h3 id="total_definition_count"><code>total_definition_count</code></h3>

`int64 total_definition_count`


<h3 id="total_exec_micros"><code>total_exec_micros</code></h3>

`int64 total_exec_micros`


<h3 id="total_float_ops"><code>total_float_ops</code></h3>

`int64 total_float_ops`


<h3 id="total_output_bytes"><code>total_output_bytes</code></h3>

`int64 total_output_bytes`


<h3 id="total_parameters"><code>total_parameters</code></h3>

`int64 total_parameters`


<h3 id="total_peak_bytes"><code>total_peak_bytes</code></h3>

`int64 total_peak_bytes`


<h3 id="total_requested_bytes"><code>total_requested_bytes</code></h3>

`int64 total_requested_bytes`


<h3 id="total_residual_bytes"><code>total_residual_bytes</code></h3>

`int64 total_residual_bytes`


<h3 id="total_run_count"><code>total_run_count</code></h3>

`int64 total_run_count`
