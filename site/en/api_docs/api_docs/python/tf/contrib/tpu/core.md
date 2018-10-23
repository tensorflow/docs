

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.core

``` python
core(num)
```



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/tpu/python/tpu/tpu.py).

Returns the device name for a core in a replicated TPU computation.

#### Args:

* <b>`num`</b>: the virtual core number within each replica to which operators should
  be assigned.

#### Returns:

A device name, suitable for passing to tf.device().