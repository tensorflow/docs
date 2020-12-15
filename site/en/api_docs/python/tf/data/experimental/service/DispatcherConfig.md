description: Configuration class for tf.data service dispatchers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.service.DispatcherConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="fault_tolerant_mode"/>
<meta itemprop="property" content="job_gc_check_interval_ms"/>
<meta itemprop="property" content="job_gc_timeout_ms"/>
<meta itemprop="property" content="port"/>
<meta itemprop="property" content="protocol"/>
<meta itemprop="property" content="work_dir"/>
</div>

# tf.data.experimental.service.DispatcherConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/experimental/service/server_lib.py#L31-L78">
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
<p>`tf.compat.v1.data.experimental.service.DispatcherConfig`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.service.DispatcherConfig(
    port=0, protocol='grpc', work_dir=None, fault_tolerant_mode=(False),
    job_gc_check_interval_ms=None, job_gc_timeout_ms=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Fields:


* <b>`port`</b>: Specifies the port to bind to. A value of 0 indicates that the server
  may bind to any available port.
* <b>`protocol`</b>: The protocol to use for communicating with the tf.data service.
  Defaults to `"grpc"`.
* <b>`work_dir`</b>: A directory to store dispatcher state in. This
  argument is required for the dispatcher to be able to recover from
  restarts.
* <b>`fault_tolerant_mode`</b>: Whether the dispatcher should write its state to a
  journal so that it can recover from restarts. Dispatcher state, including
  registered datasets and created jobs, is synchronously written to the
  journal before responding to RPCs. If `True`, `work_dir` must also be
  specified.
* <b>`job_gc_check_interval_ms`</b>: How often the dispatcher should scan through to
  delete old and unused jobs, in milliseconds. If not set, the runtime will
  select a reasonable default. A higher value will reduce load on the
  dispatcher, while a lower value will reduce the time it takes for the
  dispatcher to garbage collect expired jobs.
* <b>`job_gc_timeout_ms`</b>: How long a job needs to be unused before it becomes a
  candidate for garbage collection, in milliseconds. If not set, the runtime
  will select a reasonable default. A higher value will cause jobs to stay
  around longer with no consumers. This is useful if there is a large gap in
  time between when consumers read from the job. A lower value will reduce
  the time it takes to reclaim the resources from expired jobs.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
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
`work_dir`
</td>
<td>

</td>
</tr><tr>
<td>
`fault_tolerant_mode`
</td>
<td>

</td>
</tr><tr>
<td>
`job_gc_check_interval_ms`
</td>
<td>

</td>
</tr><tr>
<td>
`job_gc_timeout_ms`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `fault_tolerant_mode` <a id="fault_tolerant_mode"></a>
* `job_gc_check_interval_ms` <a id="job_gc_check_interval_ms"></a>
* `job_gc_timeout_ms` <a id="job_gc_timeout_ms"></a>
* `port` <a id="port"></a>
* `protocol` <a id="protocol"></a>
* `work_dir` <a id="work_dir"></a>
