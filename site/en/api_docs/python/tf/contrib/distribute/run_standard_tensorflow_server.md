page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.run_standard_tensorflow_server


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_coordinator.py#L555-L625">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Starts a standard TensorFlow server.

``` python
tf.contrib.distribute.run_standard_tensorflow_server(session_config=None)
```



<!-- Placeholder for "Used in" -->

This method parses configurations from "TF_CONFIG" environment variable and
starts a TensorFlow server. The "TF_CONFIG" is typically a json string and
must have information of the cluster and the role of the server in the
cluster. One example is:

TF_CONFIG='{
    "cluster": {
        "worker": ["host1:2222", "host2:2222", "host3:2222"],
        "ps": ["host4:2222", "host5:2222"]
    },
    "task": {"type": "worker", "index": 1}
}'

This "TF_CONFIG" specifies there are 3 workers and 2 ps tasks in the cluster
and the current role is worker 1.

Valid task types are "chief", "worker", "ps" and "evaluator" and you can have
at most one "chief" and at most one "evaluator".

An optional key-value can be specified is "rpc_layer". The default value is
"grpc".

#### Args:


* <b>`session_config`</b>: an optional <a href="../../../tf/ConfigProto"><code>tf.compat.v1.ConfigProto</code></a> object. Users can
  pass in the session config object to configure server-local devices.


#### Returns:

a <a href="../../../tf/distribute/Server"><code>tf.distribute.Server</code></a> object which has already been started.



#### Raises:


* <b>`ValueError`</b>: if the "TF_CONFIG" environment is not complete.
