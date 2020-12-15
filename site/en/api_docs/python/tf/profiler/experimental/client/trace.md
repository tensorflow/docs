description: Sends gRPC requests to one or more profiler servers to perform on-demand profiling.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.experimental.client.trace" />
<meta itemprop="path" content="Stable" />
</div>

# tf.profiler.experimental.client.trace

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/profiler/profiler_client.py#L29-L133">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sends gRPC requests to one or more profiler servers to perform on-demand profiling.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.profiler.experimental.client.trace(
    service_addr, logdir, duration_ms, worker_list='', num_tracing_attempts=3,
    options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This method will block the calling thread until it receives responses from all
servers or until deadline expiration. Both single host and multiple host
profiling are supported on CPU, GPU, and TPU.
The profiled results will be saved by each server to the specified TensorBoard
log directory (i.e. the directory you save your model checkpoints). Use the
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
A comma delimited string of gRPC addresses of the workers to
profile.
e.g. service_addr='grpc://localhost:6009'
service_addr='grpc://10.0.0.2:8466,grpc://10.0.0.3:8466'
service_addr='grpc://localhost:12345,grpc://localhost:23456'
</td>
</tr><tr>
<td>
`logdir`
</td>
<td>
Path to save profile data to, typically a TensorBoard log directory.
This path must be accessible to both the client and server.
e.g. logdir='gs://your_tb_dir'
</td>
</tr><tr>
<td>
`duration_ms`
</td>
<td>
Duration of tracing or monitoring in milliseconds. Must be
greater than zero.
</td>
</tr><tr>
<td>
`worker_list`
</td>
<td>
An optional TPU only configuration. The list of workers to
profile in the current session.
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
`InvalidArgumentError`
</td>
<td>
For when arguments fail validation checks.
</td>
</tr><tr>
<td>
`UnavailableError`
</td>
<td>
If no trace event was collected.
</td>
</tr>
</table>


Example usage (CPU/GPU):

```python
  # Start a profiler server before your model runs.
  tf.profiler.experimental.server.start(6009)
  # (Model code goes here).
  # Send gRPC request to the profiler server to collect a trace of your model.
  tf.profiler.experimental.client.trace('grpc://localhost:6009',
                                        '/nfs/tb_log', 2000)
```

Example usage (Multiple GPUs):

```python
  # E.g. your worker IP addresses are 10.0.0.2, 10.0.0.3, 10.0.0.4, and you
  # would like to schedule start of profiling 1 second from now, for a
  # duration of 2 seconds.
  options['delay_ms'] = 1000
  tf.profiler.experimental.client.trace(
      'grpc://10.0.0.2:8466,grpc://10.0.0.3:8466,grpc://10.0.0.4:8466',
      'gs://your_tb_dir',
      2000,
      options=options)
```

Example usage (TPU):

```python
  # Send gRPC request to a TPU worker to collect a trace of your model. A
  # profiler service has been started in the TPU worker at port 8466.
  # E.g. your TPU IP address is 10.0.0.2 and you want to profile for 2 seconds
  # .
  tf.profiler.experimental.client.trace('grpc://10.0.0.2:8466',
                                        'gs://your_tb_dir', 2000)
```

Example usage (Multiple TPUs):

```python
  # Send gRPC request to a TPU pod to collect a trace of your model on
  # multipleTPUs. A profiler service has been started in all the TPU workers
  # at theport 8466.
  # E.g. your TPU IP addresses are 10.0.0.2, 10.0.0.3, 10.0.0.4, and you want
  # to profile for 2 seconds.
  tf.profiler.experimental.client.trace('grpc://10.0.0.2:8466',
                                        'gs://your_tb_dir',
                                        2000, '10.0.0.2,10.0.0.3,10.0.0.4')
```

Launch TensorBoard and point it to the same logdir you provided to this API.

```shell
  # logdir can be gs://your_tb_dir as in the above examples.
  $ tensorboard --logdir=/tmp/tb_log
```

Open your browser and go to localhost:6006/#profile to view profiling results.