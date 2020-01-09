page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental_connect_to_host


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/remote.py#L38-L70">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Connects to a single machine to enable remote execution on it.

### Aliases:

* `tf.compat.v1.config.experimental_connect_to_host`
* `tf.compat.v2.config.experimental_connect_to_host`


``` python
tf.config.experimental_connect_to_host(
    remote_host=None,
    job_name='worker'
)
```



<!-- Placeholder for "Used in" -->
Will make devices on the remote host available to use. Note that calling this
more than once will work, but will invalidate any tensor handles on the old
remote devices.
Using the default job_name of worker, you can schedule ops to run remotely as
follows:

```python
# Enable eager execution, and connect to the remote host.
tf.compat.v1.enable_eager_execution()
tf.contrib.eager.connect_to_remote_host("exampleaddr.com:9876")
with ops.device("job:worker/replica:0/task:1/device:CPU:0"):
  # The following tensors should be resident on the remote device, and the op
  # will also execute remotely.
  x1 = array_ops.ones([2, 2])
  x2 = array_ops.ones([2, 2])
  y = math_ops.matmul(x1, x2)
```
Args:
  remote_host: a single or a list the remote server addr in host-port format.
  job_name: The job name under which the new server will be accessible.
Raises:
  ValueError: if remote_host is None.
