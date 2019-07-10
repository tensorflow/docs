page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.initialize_system

``` python
tf.contrib.tpu.initialize_system(
    embedding_config=None,
    job=None
)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/tpu/python/tpu/tpu.py).

Initializes a distributed TPU system for use with TensorFlow.

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
  the topology must be evaluated using `Session.run` before it can be used.