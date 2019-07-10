page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.write

Writes a generic summary to the default SummaryWriter if one exists.

``` python
tf.compat.v2.summary.write(
    tag,
    tensor,
    step=None,
    metadata=None,
    name=None
)
```



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->

This exists primarily to support the definition of type-specific summary ops
like scalar() and image(), and is not intended for direct use unless defining
a new type-specific summary op.

#### Args:


* <b>`tag`</b>: string tag used to identify the summary (e.g. in TensorBoard), usually
  generated with `tf.summary.summary_scope`
* <b>`tensor`</b>: the Tensor holding the summary data to write
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to `tf.summary.experimental.get_step()`, which must
  not be None.
* <b>`metadata`</b>: Optional SummaryMetadata, as a proto or serialized bytes
* <b>`name`</b>: Optional string name for this op.


#### Returns:

True on success, or false if no summary was written because no default
summary writer was available.



#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  `tf.summary.experimental.get_step()` is None.