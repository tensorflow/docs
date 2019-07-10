page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.flush

Forces summary writer to send any buffered data to storage.

### Aliases:

* `tf.compat.v2.summary.flush`
* `tf.contrib.summary.flush`

``` python
tf.compat.v2.summary.flush(
    writer=None,
    name=None
)
```



Defined in [`python/ops/summary_ops_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/summary_ops_v2.py).

<!-- Placeholder for "Used in" -->

This operation blocks until that finishes.

#### Args:


* <b>`writer`</b>: The `tf.summary.SummaryWriter` resource to flush.
  The thread default will be used if this parameter is None.
  Otherwise a <a href="../../../../tf/no_op"><code>tf.no_op</code></a> is returned.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created <a href="../../../../tf/Operation"><code>tf.Operation</code></a>.
