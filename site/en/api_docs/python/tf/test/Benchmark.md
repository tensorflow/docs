page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.Benchmark


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/benchmark.py#L231-L349">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Benchmark`

Abstract class that provides helpers for TensorFlow benchmarks.



### Aliases:

* Class `tf.compat.v1.test.Benchmark`
* Class `tf.compat.v2.test.Benchmark`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/benchmark.py#L234-L238">View source</a>

``` python
__init__()
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="evaluate"><code>evaluate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/benchmark.py#L339-L349">View source</a>

``` python
evaluate(tensors)
```

Evaluates tensors and returns numpy values.


#### Args:


* <b>`tensors`</b>: A Tensor or a nested list/tuple of Tensors.


#### Returns:

tensors numpy values.


<h3 id="is_abstract"><code>is_abstract</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/benchmark.py#L240-L244">View source</a>

``` python
@classmethod
is_abstract(cls)
```




<h3 id="report_benchmark"><code>report_benchmark</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/benchmark.py#L185-L214">View source</a>

``` python
report_benchmark(
    iters=None,
    cpu_time=None,
    wall_time=None,
    throughput=None,
    extras=None,
    name=None,
    metrics=None
)
```

Report a benchmark.


#### Args:


* <b>`iters`</b>: (optional) How many iterations were run
* <b>`cpu_time`</b>: (optional) Median or mean cpu time in seconds.
* <b>`wall_time`</b>: (optional) Median or mean wall time in seconds.
* <b>`throughput`</b>: (optional) Throughput (in MB/s)
* <b>`extras`</b>: (optional) Dict mapping string keys to additional benchmark info.
  Values may be either floats or values that are convertible to strings.
* <b>`name`</b>: (optional) Override the BenchmarkEntry name with `name`.
  Otherwise it is inferred from the top-level method name.
* <b>`metrics`</b>: (optional) A list of dict, where each dict has the keys below
  name (required), string, metric name
  value (required), double, metric value
  min_value (optional), double, minimum acceptable metric value
  max_value (optional), double, maximum acceptable metric value

<h3 id="run_op_benchmark"><code>run_op_benchmark</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/platform/benchmark.py#L246-L337">View source</a>

``` python
run_op_benchmark(
    sess,
    op_or_tensor,
    feed_dict=None,
    burn_iters=2,
    min_iters=10,
    store_trace=False,
    store_memory_usage=True,
    name=None,
    extras=None,
    mbs=0
)
```

Run an op or tensor in the given session.  Report the results.


#### Args:


* <b>`sess`</b>: `Session` object to use for timing.
* <b>`op_or_tensor`</b>: `Operation` or `Tensor` to benchmark.
* <b>`feed_dict`</b>: A `dict` of values to feed for each op iteration (see the
  `feed_dict` parameter of `Session.run`).
* <b>`burn_iters`</b>: Number of burn-in iterations to run.
* <b>`min_iters`</b>: Minimum number of iterations to use for timing.
* <b>`store_trace`</b>: Boolean, whether to run an extra untimed iteration and
  store the trace of iteration in returned extras.
  The trace will be stored as a string in Google Chrome trace format
  in the extras field "full_trace_chrome_format". Note that trace
  will not be stored in test_log_pb2.TestResults proto.
* <b>`store_memory_usage`</b>: Boolean, whether to run an extra untimed iteration,
  calculate memory usage, and store that in extras fields.
* <b>`name`</b>: (optional) Override the BenchmarkEntry name with `name`.
  Otherwise it is inferred from the top-level method name.
* <b>`extras`</b>: (optional) Dict mapping string keys to additional benchmark info.
  Values may be either floats or values that are convertible to strings.
* <b>`mbs`</b>: (optional) The number of megabytes moved by this op, used to
  calculate the ops throughput.


#### Returns:

A `dict` containing the key-value pairs that were passed to
`report_benchmark`. If `store_trace` option is used, then
`full_chrome_trace_format` will be included in return dictionary even
though it is not passed to `report_benchmark` with `extras`.
