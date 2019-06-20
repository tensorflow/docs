page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.outfeed_enqueue

``` python
tf.contrib.tpu.outfeed_enqueue(
    input,
    name=None
)
```



Defined in generated file: `tensorflow/contrib/tpu/ops/gen_tpu_ops.py`.

An op which emits a single Tensor value from an XLA computation.

#### Args:

* <b>`input`</b>: A `Tensor`. A tensor that will be inserted into the outfeed queue.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.