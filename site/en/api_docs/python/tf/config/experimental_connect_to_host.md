description: Connects to a single machine to enable remote execution on it.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental_connect_to_host" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental_connect_to_host

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/eager/remote.py#L41-L77">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Connects to a single machine to enable remote execution on it.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental_connect_to_host`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental_connect_to_host(
    remote_host=None, job_name='worker'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Will make devices on the remote host available to use. Note that calling this
more than once will work, but will invalidate any tensor handles on the old
remote devices.

Using the default job_name of worker, you can schedule ops to run remotely as
follows:
```python
# When eager execution is enabled, connect to the remote host.
tf.config.experimental_connect_to_host("exampleaddr.com:9876")

with ops.device("job:worker/replica:0/task:1/device:CPU:0"):
  # The following tensors should be resident on the remote device, and the op
  # will also execute remotely.
  x1 = array_ops.ones([2, 2])
  x2 = array_ops.ones([2, 2])
  y = math_ops.matmul(x1, x2)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`remote_host`
</td>
<td>
a single or a list the remote server addr in host-port format.
</td>
</tr><tr>
<td>
`job_name`
</td>
<td>
The job name under which the new server will be accessible.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if remote_host is None.
</td>
</tr>
</table>

