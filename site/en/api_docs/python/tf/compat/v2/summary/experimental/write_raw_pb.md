page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.experimental.write_raw_pb

Writes a summary using raw <a href="../../../../../tf/Summary"><code>tf.compat.v1.Summary</code></a> protocol buffers.

``` python
tf.compat.v2.summary.experimental.write_raw_pb(
    tensor,
    step=None,
    name=None
)
```



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->

Experimental: this exists to support the usage of V1-style manual summary
writing (via the construction of a <a href="../../../../../tf/Summary"><code>tf.compat.v1.Summary</code></a> protocol buffer)
with the V2 summary writing API.

#### Args:


* <b>`tensor`</b>: the string Tensor holding one or more serialized `Summary` protobufs
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to `tf.summary.experimental.get_step()`, which must
  not be None.
* <b>`name`</b>: Optional string name for this op.


#### Returns:

True on success, or false if no summary was written because no default
summary writer was available.



#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  `tf.summary.experimental.get_step()` is None.