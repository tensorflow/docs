page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental_connect_to_cluster


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/experimental_connect_to_cluster">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/remote.py#L76-L125">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Connects to the given cluster.

### Aliases:

* <a href="/api_docs/python/tf/config/experimental_connect_to_cluster"><code>tf.compat.v1.config.experimental_connect_to_cluster</code></a>
* <a href="/api_docs/python/tf/config/experimental_connect_to_cluster"><code>tf.compat.v2.config.experimental_connect_to_cluster</code></a>


``` python
tf.config.experimental_connect_to_cluster(
    cluster_spec_or_resolver,
    job_name='localhost',
    task_index=0,
    protocol=None
)
```



<!-- Placeholder for "Used in" -->

Will make devices on the cluster available to use. Note that calling this more
than once will work, but will invalidate any tensor handles on the old remote
devices.

If the given local job name is not present in the cluster specification, it
will be automatically added, using an unused port on the localhost.

#### Args:


* <b>`cluster_spec_or_resolver`</b>: A `ClusterSpec` or `ClusterResolver` describing
  the cluster.
* <b>`job_name`</b>: The name of the local job.
* <b>`task_index`</b>: The local task index.
* <b>`protocol`</b>: The communication protocol, such as `"grpc"`. If unspecified, will
  use the default from `python/platform/remote_utils.py`.
