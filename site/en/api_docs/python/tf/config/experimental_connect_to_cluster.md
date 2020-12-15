description: Connects to the given cluster.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental_connect_to_cluster" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental_connect_to_cluster

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/eager/remote.py#L80-L219">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Connects to the given cluster.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental_connect_to_cluster`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental_connect_to_cluster(
    cluster_spec_or_resolver, job_name='localhost', task_index=0, protocol=None,
    make_master_device_default=(True), cluster_device_filters=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Will make devices on the cluster available to use. Note that calling this more
than once will work, but will invalidate any tensor handles on the old remote
devices.

If the given local job name is not present in the cluster specification, it
will be automatically added, using an unused port on the localhost.

Device filters can be specified to isolate groups of remote tasks to avoid
undesired accesses between workers. Workers accessing resources or launching
ops / functions on filtered remote devices will result in errors (unknown
devices). For any remote task, if no device filter is present, all cluster
devices will be visible; if any device filter is specified, it can only
see devices matching at least one filter. Devices on the task itself are
always visible. Device filters can be particially specified.

For example, for a cluster set up for parameter server training, the following
device filters might be specified:

```python
cdf = tf.config.experimental.ClusterDeviceFilters()
# For any worker, only the devices on PS nodes and itself are visible
for i in range(num_workers):
  cdf.set_device_filters('worker', i, ['/job:ps'])
# Similarly for any ps, only the devices on workers and itself are visible
for i in range(num_ps):
  cdf.set_device_filters('ps', i, ['/job:worker'])

tf.config.experimental_connect_to_cluster(cluster_def,
                                          cluster_device_filters=cdf)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cluster_spec_or_resolver`
</td>
<td>
A `ClusterSpec` or `ClusterResolver` describing
the cluster.
</td>
</tr><tr>
<td>
`job_name`
</td>
<td>
The name of the local job.
</td>
</tr><tr>
<td>
`task_index`
</td>
<td>
The local task index.
</td>
</tr><tr>
<td>
`protocol`
</td>
<td>
The communication protocol, such as `"grpc"`. If unspecified, will
use the default from `python/platform/remote_utils.py`.
</td>
</tr><tr>
<td>
`make_master_device_default`
</td>
<td>
If True and a cluster resolver is passed, will
automatically enter the master task device scope, which indicates the
master becomes the default device to run ops. It won't do anything if
a cluster spec is passed. Will throw an error if the caller is currently
already in some device scope.
</td>
</tr><tr>
<td>
`cluster_device_filters`
</td>
<td>
an instance of
`tf.train.experimental/ClusterDeviceFilters` that specify device filters
to the remote tasks in cluster.
</td>
</tr>
</table>

