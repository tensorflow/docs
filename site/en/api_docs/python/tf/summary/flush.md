page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.flush


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/summary_ops_v2.py#L907-L932">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Forces summary writer to send any buffered data to storage.

### Aliases:

* `tf.compat.v2.summary.flush`


``` python
tf.summary.flush(
    writer=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation blocks until that finishes.

#### Args:


* <b>`writer`</b>: The <a href="../../tf/summary/SummaryWriter"><code>tf.summary.SummaryWriter</code></a> resource to flush.
  The thread default will be used if this parameter is None.
  Otherwise a <a href="../../tf/no_op"><code>tf.no_op</code></a> is returned.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created <a href="../../tf/Operation"><code>tf.Operation</code></a>.
