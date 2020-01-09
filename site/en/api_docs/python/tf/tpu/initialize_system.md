page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.initialize_system


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu.py#L90-L109">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Initializes a distributed TPU system for use with TensorFlow.

### Aliases:

* <a href="/api_docs/python/tf/tpu/initialize_system"><code>tf.compat.v1.tpu.initialize_system</code></a>
* <a href="/api_docs/python/tf/tpu/initialize_system"><code>tf.contrib.tpu.initialize_system</code></a>


``` python
tf.tpu.initialize_system(
    embedding_config=None,
    job=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`embedding_config`</b>: If not None, a `TPUEmbeddingConfiguration` proto
  describing the desired configuration of the hardware embedding lookup
  tables. If embedding_config is None, no hardware embeddings can be used.
* <b>`job`</b>: The job (the XXX in TensorFlow device specification /job:XXX) that
  contains the TPU devices that will be initialized. If job=None it is
  assumed there is only one job in the TensorFlow flock, and an error will
  be returned if this assumption does not hold.

#### Returns:

A serialized `TopologyProto` that describes the TPU system. Note:
  the topology must be evaluated using <a href="../../tf/InteractiveSession#run"><code>Session.run</code></a> before it can be used.
