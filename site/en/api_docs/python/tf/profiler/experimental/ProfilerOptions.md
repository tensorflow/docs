description: Options to control profiler behaviors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.experimental.ProfilerOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="device_tracer_level"/>
<meta itemprop="property" content="host_tracer_level"/>
<meta itemprop="property" content="python_tracer_level"/>
</div>

# tf.profiler.experimental.ProfilerOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/profiler_v2.py#L50-L75">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Options to control profiler behaviors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.profiler.experimental.ProfilerOptions(
    host_tracer_level=2, python_tracer_level=0, device_tracer_level=1
)
</code></pre>



<!-- Placeholder for "Used in" -->

A `tf.profiler.ProfilerOptions` hold the knobs to control tf.profiler's
behavior.

#### Fields:


* <b>`host_tracer_level`</b>: for adjust TraceMe levels. i.e. 1 => critical,
                   2 => info, 3 => verbose. [default to 2]
* <b>`python_tracer_level`</b>: for enable python function call tracing, 1 => enable.
                     0 => disable [default to 0]
* <b>`device_tracer_level`</b>: for adjust device (TPU/GPU) tracer level, 0 => disable
                     1 => enabled. We may introduce fine-tuned level in the
                     future. [default to 1]




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`host_tracer_level`
</td>
<td>

</td>
</tr><tr>
<td>
`python_tracer_level`
</td>
<td>

</td>
</tr><tr>
<td>
`device_tracer_level`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `device_tracer_level` <a id="device_tracer_level"></a>
* `host_tracer_level` <a id="host_tracer_level"></a>
* `python_tracer_level` <a id="python_tracer_level"></a>
