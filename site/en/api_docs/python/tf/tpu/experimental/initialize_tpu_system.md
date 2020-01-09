page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.experimental.initialize_tpu_system


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/tpu/tpu_strategy_util.py#L39-L118">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Initialize the TPU devices.

### Aliases:

* `tf.compat.v1.tpu.experimental.initialize_tpu_system`
* `tf.compat.v2.tpu.experimental.initialize_tpu_system`


``` python
tf.tpu.experimental.initialize_tpu_system(cluster_resolver=None)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`cluster_resolver`</b>: A tf.distribute.cluster_resolver.TPUClusterResolver,
    which provides information about the TPU cluster.

#### Returns:

The tf.tpu.Topology object for the topology of the TPU cluster.



#### Raises:


* <b>`RuntimeError`</b>: If no TPU devices found for eager execution.
