page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.initialize_system

Initializes a distributed TPU system for use with TensorFlow.

### Aliases:

* `tf.compat.v1.tpu.initialize_system`
* `tf.contrib.tpu.initialize_system`
* `tf.tpu.initialize_system`

``` python
tf.tpu.initialize_system(
    embedding_config=None,
    job=None
)
```



Defined in [`python/tpu/tpu.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/tpu/tpu.py).

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
