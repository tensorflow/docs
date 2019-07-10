page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.infeed_enqueue

An op which feeds a single Tensor value into the computation.

``` python
tf.contrib.tpu.infeed_enqueue(
    input,
    shape=[],
    layout=[],
    device_ordinal=-1,
    name=None
)
```



Defined in generated file: `python/ops/gen_tpu_ops.py`.

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input`</b>: A `Tensor`.
  A tensor that will be provided using the infeed mechanism.
* <b>`shape`</b>: An optional <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> or list of `ints`. Defaults to `[]`.
  The shape of the tensor.
* <b>`layout`</b>: An optional list of `ints`. Defaults to `[]`.
  A vector holding the requested layout in minor-to-major sequence.
  If a layout attribute is passed, but its values are all -1, the layout will
  be computed by the infeed operation.
* <b>`device_ordinal`</b>: An optional `int`. Defaults to `-1`.
  The TPU device to use. This should be -1 when the Op
  is running on a TPU device, and >= 0 when the Op is running on the CPU
  device.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.
