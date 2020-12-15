description: Abstract class that provides helpers for TensorFlow benchmarks.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.test.Benchmark" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="evaluate"/>
<meta itemprop="property" content="is_abstract"/>
<meta itemprop="property" content="report_benchmark"/>
<meta itemprop="property" content="run_op_benchmark"/>
</div>

# tf.test.Benchmark

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/platform/benchmark.py#L288-L420">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Abstract class that provides helpers for TensorFlow benchmarks.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.test.Benchmark`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.test.Benchmark()
</code></pre>



<!-- Placeholder for "Used in" -->


## Methods

<h3 id="evaluate"><code>evaluate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/platform/benchmark.py#L410-L420">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>evaluate(
    tensors
)
</code></pre>

Evaluates tensors and returns numpy values.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensors`
</td>
<td>
A Tensor or a nested list/tuple of Tensors.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
tensors numpy values.
</td>
</tr>

</table>



<h3 id="is_abstract"><code>is_abstract</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/platform/benchmark.py#L297-L301">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>is_abstract()
</code></pre>




<h3 id="report_benchmark"><code>report_benchmark</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/platform/benchmark.py#L242-L271">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>report_benchmark(
    iters=None, cpu_time=None, wall_time=None, throughput=None, extras=None,
    name=None, metrics=None
)
</code></pre>

Report a benchmark.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`iters`
</td>
<td>
(optional) How many iterations were run
</td>
</tr><tr>
<td>
`cpu_time`
</td>
<td>
(optional) Median or mean cpu time in seconds.
</td>
</tr><tr>
<td>
`wall_time`
</td>
<td>
(optional) Median or mean wall time in seconds.
</td>
</tr><tr>
<td>
`throughput`
</td>
<td>
(optional) Throughput (in MB/s)
</td>
</tr><tr>
<td>
`extras`
</td>
<td>
(optional) Dict mapping string keys to additional benchmark info.
Values may be either floats or values that are convertible to strings.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(optional) Override the BenchmarkEntry name with `name`.
Otherwise it is inferred from the top-level method name.
</td>
</tr><tr>
<td>
`metrics`
</td>
<td>
(optional) A list of dict, where each dict has the keys below
name (required), string, metric name
value (required), double, metric value
min_value (optional), double, minimum acceptable metric value
max_value (optional), double, maximum acceptable metric value
</td>
</tr>
</table>



<h3 id="run_op_benchmark"><code>run_op_benchmark</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/platform/benchmark.py#L303-L408">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run_op_benchmark(
    sess, op_or_tensor, feed_dict=None, burn_iters=2, min_iters=10,
    store_trace=(False), store_memory_usage=(True), name=None, extras=None, mbs=0
)
</code></pre>

Run an op or tensor in the given session.  Report the results.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
`Session` object to use for timing.
</td>
</tr><tr>
<td>
`op_or_tensor`
</td>
<td>
`Operation` or `Tensor` to benchmark.
</td>
</tr><tr>
<td>
`feed_dict`
</td>
<td>
A `dict` of values to feed for each op iteration (see the
`feed_dict` parameter of `Session.run`).
</td>
</tr><tr>
<td>
`burn_iters`
</td>
<td>
Number of burn-in iterations to run.
</td>
</tr><tr>
<td>
`min_iters`
</td>
<td>
Minimum number of iterations to use for timing.
</td>
</tr><tr>
<td>
`store_trace`
</td>
<td>
Boolean, whether to run an extra untimed iteration and
store the trace of iteration in returned extras.
The trace will be stored as a string in Google Chrome trace format
in the extras field "full_trace_chrome_format". Note that trace
will not be stored in test_log_pb2.TestResults proto.
</td>
</tr><tr>
<td>
`store_memory_usage`
</td>
<td>
Boolean, whether to run an extra untimed iteration,
calculate memory usage, and store that in extras fields.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(optional) Override the BenchmarkEntry name with `name`.
Otherwise it is inferred from the top-level method name.
</td>
</tr><tr>
<td>
`extras`
</td>
<td>
(optional) Dict mapping string keys to additional benchmark info.
Values may be either floats or values that are convertible to strings.
</td>
</tr><tr>
<td>
`mbs`
</td>
<td>
(optional) The number of megabytes moved by this op, used to
calculate the ops throughput.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `dict` containing the key-value pairs that were passed to
`report_benchmark`. If `store_trace` option is used, then
`full_chrome_trace_format` will be included in return dictionary even
though it is not passed to `report_benchmark` with `extras`.
</td>
</tr>

</table>





