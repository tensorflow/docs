page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.outfeed_enqueue_tuple

Enqueue multiple Tensor values on the computation outfeed.

``` python
tf.contrib.tpu.outfeed_enqueue_tuple(
    inputs,
    name=None
)
```



Defined in generated file: `python/ops/gen_tpu_ops.py`.

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`inputs`</b>: A list of `Tensor` objects.
  A list of tensors that will be inserted into the outfeed queue as an
  XLA tuple.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.
