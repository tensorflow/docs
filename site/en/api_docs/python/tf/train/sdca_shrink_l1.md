page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.sdca_shrink_l1


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_sdca_ops.py`



Applies L1 regularization shrink step on the parameters.

### Aliases:

* <a href="/api_docs/python/tf/train/sdca_shrink_l1"><code>tf.compat.v1.train.sdca_shrink_l1</code></a>


``` python
tf.train.sdca_shrink_l1(
    weights,
    l1,
    l2,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`weights`</b>: A list of `Tensor` objects with type mutable `float32`.
  a list of vectors where each value is the weight associated with a
  feature group.
* <b>`l1`</b>: A `float`. Symmetric l1 regularization strength.
* <b>`l2`</b>: A `float`.
  Symmetric l2 regularization strength. Should be a positive float.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.
