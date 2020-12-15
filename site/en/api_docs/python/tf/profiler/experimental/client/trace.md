description: Sends grpc requests to profiler server to perform on-demand profiling.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.experimental.client.trace" />
<meta itemprop="path" content="Stable" />
</div>

# tf.profiler.experimental.client.trace

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/profiler/profiler_client.py#L28-L95">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sends grpc requests to profiler server to perform on-demand profiling.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.profiler.experimental.client.trace(
    service_addr, logdir, duration_ms, worker_list='', num_tracing_attempts=3,
    options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This method will block caller thread until it receives tracing result. This
method supports CPU, GPU, and Cloud TPU. This method supports profiling a
single host for CPU, GPU, TPU, as well as multiple TPU workers.
The profiled results will be saved to your specified TensorBoard log
directory (e.g. the directory you save your model checkpoints). Use the
TensorBoard profile plugin to view the visualization and analysis results.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`service_addr`
</td>
<td>
gRPC address of profiler service e.g. grpc://localhost:6009.
</td>
</tr><tr>
<td>
`logdir`
</td>
<td>
Path of TensorBoard log directory e.g. /tmp/tb_log.
</td>
</tr><tr>
<td>
`duration_ms`
</td>
<td>
Duration of tracing or monitoring in ms.
</td>
</tr><tr>
<td>
`worker_list`
</td>
<td>
Optional. The list of workers that we are about to profile in
the current session (TPU only).
</td>
</tr><tr>
<td>
`num_tracing_attempts`
</td>
<td>
Optional. Automatically retry N times when no trace
event is collected (default 3).
</td>
</tr><tr>
<td>
`options`
</td>
<td>
profiler.experimental.ProfilerOptions namedtuple for miscellaneous
profiler options.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`UnavailableError`
</td>
<td>
If no trace event is collected.
</td>
</tr>
</table>


Example usage (CPU/GPU):
# Start a profiler server before your model runs.
```python
tf.profiler.experimental.server.start(6009)
# your model code.
# Send gRPC request to the profiler server to collect a trace of your model.
```python
tf.profiler.experimental.client.trace('grpc://localhost:6009',
                                      '/tmp/tb_log', 2000)

Example usage (TPU):
# Send gRPC request to a TPU worker to collect a trace of your model. A
# profiler service has been started in the TPU worker at port 8466.
```python
# E.g. your TPU IP address is 10.0.0.2 and you want to profile for 2 seconds.
tf.profiler.experimental.client.trace('grpc://10.0.0.2:8466',
                                      'gs://your_tb_dir', 2000)

Example usage (Multiple TPUs):
# Send gRPC request to a TPU pod to collect a trace of your model on multiple
# TPUs. A profiler service has been started in all the TPU workers at the
# port 8466.
```python
# E.g. your TPU IP addresses are 10.0.0.2, 10.0.0.3, 10.0.0.4, and you want to
# profile for 2 seconds.
tf.profiler.experimental.client.trace('grpc://10.0.0.2:8466',
                                      'gs://your_tb_dir',
                                      2000, '10.0.0.3,10.0.0.4')

Launch TensorBoard and point it to the same logdir you provided to this API.
$ tensorboard --logdir=/tmp/tb_log (or gs://your_tb_dir in the above examples)
Open your browser and go to localhost:6006/#profile to view profiling results.