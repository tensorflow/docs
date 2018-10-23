

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.summary.flush

``` python
tf.contrib.summary.flush(
    writer=None,
    name=None
)
```



Defined in [`tensorflow/contrib/summary/summary_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/summary/summary_ops.py).

Forces summary writer to send any buffered data to storage.

This operation blocks until that finishes.

#### Args:

* <b>`writer`</b>: The <a href="../../../tf/contrib/summary/SummaryWriter"><code>tf.contrib.summary.SummaryWriter</code></a> resource to flush.
    The thread default will be used if this parameter is None.
    Otherwise a <a href="../../../tf/no_op"><code>tf.no_op</code></a> is returned.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created <a href="../../../tf/Operation"><code>tf.Operation</code></a>.