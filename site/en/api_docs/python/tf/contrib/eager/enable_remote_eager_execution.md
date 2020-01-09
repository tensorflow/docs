page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.enable_remote_eager_execution


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L5737-L5807">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Enables eager execution for the lifetime of this program.

``` python
tf.contrib.eager.enable_remote_eager_execution(
    config=None,
    device_policy=None,
    execution_mode=None,
    server_def=None
)
```



<!-- Placeholder for "Used in" -->

Most of the doc string for enable_eager_execution is relevant here as well.

#### Args:


* <b>`config`</b>: See enable_eager_execution doc string
* <b>`device_policy`</b>: See enable_eager_execution doc string
* <b>`execution_mode`</b>: See enable_eager_execution doc string
* <b>`server_def`</b>: (Optional.) A tensorflow::ServerDef proto. Enables execution on
  remote devices. GrpcServers need to be started by creating an identical
  server_def to this, and setting the appropriate task_indexes, so that the
  servers can communicate. It will then be possible to execute operations on
  remote devices.


#### Raises:

ValueError
