page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.infeed_enqueue_tuple

Feeds multiple Tensor values into the computation as an XLA tuple.

``` python
tf.contrib.tpu.infeed_enqueue_tuple(
    inputs,
    shapes,
    layouts=[],
    device_ordinal=-1,
    name=None
)
```



Defined in generated file: `python/ops/gen_tpu_ops.py`.

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`inputs`</b>: A list of `Tensor` objects.
  A list of tensors that will be provided using the infeed mechanism.
* <b>`shapes`</b>: A list of shapes (each a <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> or list of `ints`).
  The shapes of each tensor in `inputs`.
* <b>`layouts`</b>: An optional list of `ints`. Defaults to `[]`.
  A vector holding the requested layout in minor-to-major sequence for
  all the tuple shapes, in the order the shapes appear in the "shapes" input.
  The layout elements for a sub-shape can be set to -1, in which case the
  corresponding layout will be computed by the infeed operation.
* <b>`device_ordinal`</b>: An optional `int`. Defaults to `-1`.
  The TPU device to use. This should be -1 when the Op
  is running on a TPU device, and >= 0 when the Op is running on the CPU
  device.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.
