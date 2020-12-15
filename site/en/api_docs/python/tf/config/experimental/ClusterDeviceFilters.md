description: Represent a collection of device filters for the remote workers in cluster.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental.ClusterDeviceFilters" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="set_device_filters"/>
</div>

# tf.config.experimental.ClusterDeviceFilters

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/server_lib.py#L500-L578">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represent a collection of device filters for the remote workers in cluster.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.ClusterDeviceFilters`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental.ClusterDeviceFilters()
</code></pre>



<!-- Placeholder for "Used in" -->

NOTE: this is an experimental API and subject to changes.

Set device filters for selective jobs and tasks. For each remote worker, the
device filters are a list of strings. When any filters are present, the remote
worker will ignore all devices which do not match any of its filters. Each
filter can be partially specified, e.g. "/job:ps", "/job:worker/replica:3",
etc. Note that a device is always visible to the worker it is located on.

For example, to set the device filters for a parameter server cluster:

```python
cdf = tf.config.experimental.ClusterDeviceFilters()
for i in range(num_workers):
  cdf.set_device_filters('worker', i, ['/job:ps'])
for i in range(num_ps):
  cdf.set_device_filters('ps', i, ['/job:worker'])

tf.config.experimental_connect_to_cluster(cluster_def,
                                          cluster_device_filters=cdf)
```

The device filters can be partically specified. For remote tasks that do not
have device filters specified, all devices will be visible to them.

## Methods

<h3 id="set_device_filters"><code>set_device_filters</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/server_lib.py#L537-L543">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_device_filters(
    job_name, task_index, device_filters
)
</code></pre>

Set the device filters for given job name and task id.




