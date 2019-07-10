page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.infeed_enqueue

``` python
tf.contrib.tpu.infeed_enqueue(
    input,
    shape=[],
    device_ordinal=-1,
    name=None
)
```



Defined in generated file: `tensorflow/contrib/tpu/ops/gen_tpu_ops.py`.

An op which feeds a single Tensor value into the computation.

#### Args:

* <b>`input`</b>: A `Tensor`.
    A tensor that will be provided using the infeed mechanism.
* <b>`shape`</b>: An optional <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> or list of `ints`. Defaults to `[]`.
    The shape of the tensor.
* <b>`device_ordinal`</b>: An optional `int`. Defaults to `-1`.
    The TPU device to use. This should be -1 when the Op
    is running on a TPU device, and >= 0 when the Op is running on the CPU
    device.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.