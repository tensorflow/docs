page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.enable_remote_eager_execution

``` python
tf.contrib.eager.enable_remote_eager_execution(
    config=None,
    device_policy=None,
    execution_mode=None,
    server_def=None
)
```



Defined in [`tensorflow/python/framework/ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/framework/ops.py).

Enables eager execution for the lifetime of this program.

Most of the doc string for enable_eager_execution is relevant here as well.
#### Args:

* <b>`config`</b>: See enable_eager_execution doc string
* <b>`device_policy`</b>: See enable_eager_execution doc string
* <b>`execution_mode`</b>: See enable_eager_execution doc string
* <b>`server_def`</b>: (Optional.) A tensorflow::ServerDef proto.
    Enables execution on remote devices. GrpcServers need to be started by
    creating an identical server_def to this, and setting the appropriate
    task_indexes, so that the servers can communicate. It will then be
    possible to execute operations on remote devices.


#### Raises:

ValueError