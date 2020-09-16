description: Starts profiling.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.experimental.start" />
<meta itemprop="path" content="Stable" />
</div>

# tf.profiler.experimental.start

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/profiler_v2.py#L48-L86">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Starts profiling.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.profiler.experimental.start(
    logdir
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
A log directory read by TensorBoard to export the profile results.
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
If another profiling session is running.
</td>
</tr>
</table>



#### Example usage:


```python
tf.profiler.experimental.start('logdir_path')
# do your training here.
tf.profiler.experimental.stop()
```

Launch TensorBoard and point it to the same logdir you provided to this API.
$ tensorboard --logdir=logdir_path
Open your browser and go to localhost:6006/#profile to view profiling results.