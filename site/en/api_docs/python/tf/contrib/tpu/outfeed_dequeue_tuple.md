page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.outfeed_dequeue_tuple

``` python
tf.contrib.tpu.outfeed_dequeue_tuple(
    dtypes,
    shapes,
    device_ordinal=-1,
    name=None
)
```



Defined in generated file: `tensorflow/contrib/tpu/ops/gen_tpu_ops.py`.

Retrieve multiple values that will be emitted by the computation as an XLA

tuple.  This operations will block indefinitely until data is available.
Output `i` corresponds to XLA tuple element `i`.

#### Args:

* <b>`dtypes`</b>: A list of `tf.DTypes` that has length `>= 1`.
    The element types of each element in `outputs`.
* <b>`shapes`</b>: A list of shapes (each a <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> or list of `ints`).
    The shapes of each tensor in `outputs`.
* <b>`device_ordinal`</b>: An optional `int`. Defaults to `-1`.
    The TPU device to use. This should be -1 when the Op
    is running on a TPU device, and >= 0 when the Op is running on the CPU
    device.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `Tensor` objects of type `dtypes`.
A list of tensors that will be read from the outfeed.