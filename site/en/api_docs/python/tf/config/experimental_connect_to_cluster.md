page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental_connect_to_cluster


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/remote.py#L73-L154">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Connects to the given cluster.

### Aliases:

* `tf.compat.v1.config.experimental_connect_to_cluster`
* `tf.compat.v2.config.experimental_connect_to_cluster`


``` python
tf.config.experimental_connect_to_cluster(
    cluster_spec_or_resolver,
    job_name='localhost',
    task_index=0,
    protocol=None,
    make_master_device_default=True
)
```



<!-- Placeholder for "Used in" -->
Will make devices on the cluster available to use. Note that calling this more
than once will work, but will invalidate any tensor handles on the old remote
devices.
If the given local job name is not present in the cluster specification, it
will be automatically added, using an unused port on the localhost.
Args:
  cluster_spec_or_resolver: A `ClusterSpec` or `ClusterResolver` describing
    the cluster.
  job_name: The name of the local job.
  task_index: The local task index.
  protocol: The communication protocol, such as `"grpc"`. If unspecified, will
    use the default from `python/platform/remote_utils.py`.
  make_master_device_default: If True and a cluster resolver is passed, will
    automatically enter the master task device scope, which indicates the
    master becomes the default device to run ops. It won't do anything if
    a cluster spec is passed. Will throw an error if the caller is currently
    already in some device scope.
