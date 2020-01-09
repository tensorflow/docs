page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.trace_on


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/summary_ops_v2.py#L1128-L1170">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Starts a trace to record computation graphs and profiling information.

### Aliases:

* `tf.compat.v2.summary.trace_on`


``` python
tf.summary.trace_on(
    graph=True,
    profiler=False
)
```



<!-- Placeholder for "Used in" -->

Must be invoked in eager mode.

When enabled, TensorFlow runtime will collection information that can later be
exported and consumed by TensorBoard. The trace is activated across the entire
TensorFlow runtime and affects all threads of execution.

To stop the trace and export the collected information, use
<a href="../../tf/summary/trace_export"><code>tf.summary.trace_export</code></a>. To stop the trace without exporting, use
<a href="../../tf/summary/trace_off"><code>tf.summary.trace_off</code></a>.

#### Args:


* <b>`graph`</b>: If True, enables collection of executed graphs. It includes ones from
    tf.function invocation and ones from the legacy graph mode. The default
    is True.
* <b>`profiler`</b>: If True, enables the advanced profiler. Enabling profiler
    implicitly enables the graph collection. The profiler may incur a high
    memory overhead. The default is False.
