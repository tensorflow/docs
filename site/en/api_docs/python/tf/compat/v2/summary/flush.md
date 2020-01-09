page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.summary.flush


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L907-L932">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Forces summary writer to send any buffered data to storage.

### Aliases:

* <a href="/api_docs/python/tf/compat/v2/summary/flush"><code>tf.contrib.summary.flush</code></a>


``` python
tf.compat.v2.summary.flush(
    writer=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation blocks until that finishes.

#### Args:


* <b>`writer`</b>: The `tf.summary.SummaryWriter` resource to flush.
  The thread default will be used if this parameter is None.
  Otherwise a <a href="../../../../tf/no_op"><code>tf.no_op</code></a> is returned.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created <a href="../../../../tf/Operation"><code>tf.Operation</code></a>.
