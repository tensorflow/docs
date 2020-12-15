description: An in-process tf.data service worker server.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.service.WorkerServer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="join"/>
<meta itemprop="property" content="start"/>
</div>

# tf.data.experimental.service.WorkerServer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/service/server_lib.py#L145-L256">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An in-process tf.data service worker server.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.service.WorkerServer(
    port, dispatcher_address, worker_address=None, protocol=None, start=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

A <a href="../../../../tf/data/experimental/service/WorkerServer.md"><code>tf.data.experimental.service.WorkerServer</code></a> performs <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>
processing for user-defined datasets, and provides the resulting elements over
RPC. A worker is associated with a single
<a href="../../../../tf/data/experimental/service/DispatchServer.md"><code>tf.data.experimental.service.DispatchServer</code></a>.

```
>>> dispatcher = tf.data.experimental.service.DispatchServer(port=0)
>>> dispatcher_address = dispatcher.target.split("://")[1]
>>> worker = tf.data.experimental.service.WorkerServer(
...     port=0, dispatcher_address=dispatcher_address)
>>> dataset = tf.data.Dataset.range(10)
>>> dataset = dataset.apply(tf.data.experimental.service.distribute(
...     processing_mode="parallel_epochs", service=dispatcher.target))
>>> print(list(dataset.as_numpy_iterator()))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

When starting a dedicated tf.data worker process, use join() to block
indefinitely after starting up the server.

```
worker = tf.data.experimental.service.WorkerServer(
    port=5051, dispatcher_address="grpc://localhost:5050")
worker.join()
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`port`
</td>
<td>
Specifies the port to bind to. A value of 0 indicates that the
worker can bind to any available port.
</td>
</tr><tr>
<td>
`dispatcher_address`
</td>
<td>
Specifies the address of the dispatcher.
</td>
</tr><tr>
<td>
`worker_address`
</td>
<td>
(Optional.) Specifies the address of the worker server.
This address is passed to the dispatcher so that the dispatcher can
tell clients how to connect to this worker. Defaults to
`"localhost:%port%"`, where `%port%` will be replaced with the port used
by the worker.
</td>
</tr><tr>
<td>
`protocol`
</td>
<td>
(Optional.) Specifies the protocol to be used by the server.
Acceptable values include `"grpc", "grpc+local"`. Defaults to `"grpc"`.
</td>
</tr><tr>
<td>
`start`
</td>
<td>
(Optional.) Boolean, indicating whether to start the server after
creating it. Defaults to `True`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`tf.errors.OpError`
</td>
<td>
Or one of its subclasses if an error occurs while
creating the TensorFlow server.
</td>
</tr>
</table>



## Methods

<h3 id="join"><code>join</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/service/server_lib.py#L219-L236">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>join()
</code></pre>

Blocks until the server has shut down.

This is useful when starting a dedicated worker process.

```
worker_server = tf.data.experimental.service.WorkerServer(
    port=5051, dispatcher_address="grpc://localhost:5050")
worker_server.join()
```

This method currently blocks forever.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`tf.errors.OpError`
</td>
<td>
Or one of its subclasses if an error occurs while
joining the server.
</td>
</tr>
</table>



<h3 id="start"><code>start</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/service/server_lib.py#L210-L217">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>start()
</code></pre>

Starts this server.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`tf.errors.OpError`
</td>
<td>
Or one of its subclasses if an error occurs while
starting the server.
</td>
</tr>
</table>





