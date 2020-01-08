page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.import_event

``` python
tf.contrib.summary.import_event(
    tensor,
    name=None
)
```



Defined in [`tensorflow/python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/summary_ops_v2.py).

Writes a <a href="../../../tf/Event"><code>tf.Event</code></a> binary proto.

When using create_db_writer(), this can be used alongside
<a href="../../../tf/TFRecordReader"><code>tf.TFRecordReader</code></a> to load event logs into the database. Please
note that this is lower level than the other summary functions and
will ignore any conditions set by methods like
<a href="../../../tf/contrib/summary/should_record_summaries"><code>tf.contrib.summary.should_record_summaries</code></a>.

#### Args:

* <b>`tensor`</b>: A <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> of type `string` containing a serialized
    <a href="../../../tf/Event"><code>tf.Event</code></a> proto.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created <a href="../../../tf/Operation"><code>tf.Operation</code></a>.