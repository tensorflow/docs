page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.experimental.initialize_tpu_system


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/tpu/experimental/initialize_tpu_system">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu_strategy_util.py#L39-L118">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Initialize the TPU devices.

### Aliases:

* <a href="/api_docs/python/tf/tpu/experimental/initialize_tpu_system"><code>tf.compat.v1.tpu.experimental.initialize_tpu_system</code></a>
* <a href="/api_docs/python/tf/tpu/experimental/initialize_tpu_system"><code>tf.compat.v2.tpu.experimental.initialize_tpu_system</code></a>
* <a href="/api_docs/python/tf/tpu/experimental/initialize_tpu_system"><code>tf.contrib.distribute.initialize_tpu_system</code></a>


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
