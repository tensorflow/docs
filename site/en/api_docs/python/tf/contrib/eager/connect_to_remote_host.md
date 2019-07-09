page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.connect_to_remote_host

``` python
tf.contrib.eager.connect_to_remote_host(
    remote_host=None,
    job_name='worker'
)
```



Defined in [`tensorflow/contrib/eager/python/remote.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/eager/python/remote.py).

Connects to a single machine to enable remote execution on it.

Will make devices on the remote host available to use. Note that calling this
more than once will work, but will invalidate any tensor handles on the old
remote devices.

Using the default job_name of worker, you can schedule ops to run remotely as
follows:

```python
# Enable eager execution, and connect to the remote host.
tf.enable_eager_execution()
tf.contrib.eager.connect_to_remote_host("exampleaddr.com:9876")

with ops.device("job:worker/replica:0/task:1/device:CPU:0"):
  # The following tensors should be resident on the remote device, and the op
  # will also execute remotely.
  x1 = array_ops.ones([2, 2])
  x2 = array_ops.ones([2, 2])
  y = math_ops.matmul(x1, x2)
```

#### Args:

* <b>`remote_host`</b>: The addr of the remote server in host-port format.
* <b>`job_name`</b>: The job name under which the new server will be accessible.


#### Raises:

* <b>`ValueError`</b>: if remote_host is None.