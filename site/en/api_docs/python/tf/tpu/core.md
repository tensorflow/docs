page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.core

Returns the device name for a core in a replicated TPU computation.

### Aliases:

* `tf.compat.v1.tpu.core`
* `tf.contrib.tpu.core`
* `tf.tpu.core`

``` python
tf.tpu.core(num)
```



Defined in [`python/tpu/tpu.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/tpu/tpu.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`num`</b>: the virtual core number within each replica to which operators should
be assigned.

#### Returns:

A device name, suitable for passing to <a href="../../tf/device"><code>tf.device()</code></a>.
