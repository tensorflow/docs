page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.outfeed_enqueue


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_tpu_ops.py`



Enqueue a Tensor on the computation outfeed.

``` python
tf.contrib.tpu.outfeed_enqueue(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input`</b>: A `Tensor`. A tensor that will be inserted into the outfeed queue.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.
