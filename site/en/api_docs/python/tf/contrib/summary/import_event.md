page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.import_event

Writes a <a href="../../../tf/Event"><code>tf.compat.v1.Event</code></a> binary proto.

``` python
tf.contrib.summary.import_event(
    tensor,
    name=None
)
```



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->

This can be used to import existing event logs into a new summary writer sink.
Please note that this is lower level than the other summary functions and
will ignore the `tf.summary.should_record_summaries` setting.

#### Args:


* <b>`tensor`</b>: A <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> of type `string` containing a serialized
  <a href="../../../tf/Event"><code>tf.compat.v1.Event</code></a> proto.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created <a href="../../../tf/Operation"><code>tf.Operation</code></a>.
