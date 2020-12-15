description: Start profiling TensorFlow performance.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.experimental.start" />
<meta itemprop="path" content="Stable" />
</div>

# tf.profiler.experimental.start

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/profiler/profiler_v2.py#L85-L131">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Start profiling TensorFlow performance.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.profiler.experimental.start(
    logdir, options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`logdir`
</td>
<td>
Profiling results log directory.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
`ProfilerOptions` namedtuple to specify miscellaneous profiler
options. See example usage below.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`AlreadyExistsError`
</td>
<td>
If a profiling session is already running.
</td>
</tr>
</table>



#### Example usage:


```python
options = tf.profiler.experimental.ProfilerOptions(host_tracer_level = 3,
                                                   python_tracer_level = 1,
                                                   device_tracer_level = 1)
tf.profiler.experimental.start('logdir_path', options = options)
# Training code here
tf.profiler.experimental.stop()
```

To view the profiling results, launch TensorBoard and point it to `logdir`.
Open your browser and go to `localhost:6006/#profile` to view profiling
results.