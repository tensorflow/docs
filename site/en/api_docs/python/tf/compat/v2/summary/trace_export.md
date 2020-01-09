page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.trace_export


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L1173-L1220">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stops and exports the active trace as a Summary and/or profile file.

``` python
tf.compat.v2.summary.trace_export(
    name,
    step=None,
    profiler_outdir=None
)
```



<!-- Placeholder for "Used in" -->

Stops the trace and exports all metadata collected during the trace to the
default SummaryWriter, if one has been set.

#### Args:


* <b>`name`</b>: A name for the summary to be written.
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to `tf.summary.experimental.get_step()`, which must
  not be None.
* <b>`profiler_outdir`</b>: Output directory for profiler. It is required when profiler
  is enabled when trace was started. Otherwise, it is ignored.


#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  `tf.summary.experimental.get_step()` is None.
