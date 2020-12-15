description: Configuration class for tf.data service dispatchers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.service.WorkerConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="dispatcher_address"/>
<meta itemprop="property" content="dispatcher_timeout_ms"/>
<meta itemprop="property" content="heartbeat_interval_ms"/>
<meta itemprop="property" content="port"/>
<meta itemprop="property" content="protocol"/>
<meta itemprop="property" content="worker_address"/>
</div>

# tf.data.experimental.service.WorkerConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/service/server_lib.py#L217-L259">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration class for tf.data service dispatchers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.service.WorkerConfig`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.service.WorkerConfig(
    dispatcher_address, worker_address=None, port=0, protocol='grpc',
    heartbeat_interval_ms=None, dispatcher_timeout_ms=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Fields:


* <b>`dispatcher_address`</b>: Specifies the address of the dispatcher.
* <b>`worker_address`</b>: Specifies the address of the worker server. This address is
  passed to the dispatcher so that the dispatcher can tell clients how to
  connect to this worker.
* <b>`port`</b>: Specifies the port to bind to. A value of 0 indicates that the worker
  can bind to any available port.
* <b>`protocol`</b>: (Optional.) Specifies the protocol to be used by the server.
  Defaults to `"grpc"`.
* <b>`heartbeat_interval_ms`</b>: How often the worker should heartbeat to the
  dispatcher, in milliseconds. If not set, the runtime will select a
  reasonable default. A higher value will reduce the load on the dispatcher,
  while a lower value will reduce the time it takes to reclaim resources
  from finished jobs.
* <b>`dispatcher_timeout_ms`</b>: How long, in milliseconds, to retry requests to the
  dispatcher before giving up and reporting an error. Defaults to 1 hour.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dispatcher_address`
</td>
<td>

</td>
</tr><tr>
<td>
`worker_address`
</td>
<td>

</td>
</tr><tr>
<td>
`port`
</td>
<td>

</td>
</tr><tr>
<td>
`protocol`
</td>
<td>

</td>
</tr><tr>
<td>
`heartbeat_interval_ms`
</td>
<td>

</td>
</tr><tr>
<td>
`dispatcher_timeout_ms`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `dispatcher_address` <a id="dispatcher_address"></a>
* `dispatcher_timeout_ms` <a id="dispatcher_timeout_ms"></a>
* `heartbeat_interval_ms` <a id="heartbeat_interval_ms"></a>
* `port` <a id="port"></a>
* `protocol` <a id="protocol"></a>
* `worker_address` <a id="worker_address"></a>
