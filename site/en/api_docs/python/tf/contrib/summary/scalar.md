page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.summary.scalar


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/summary_ops_v2.py#L757-L786">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Writes a scalar summary if possible.

``` python
tf.contrib.summary.scalar(
    name,
    tensor,
    family=None,
    step=None
)
```



<!-- Placeholder for "Used in" -->

Unlike <a href="../../../tf/contrib/summary/generic"><code>tf.contrib.summary.generic</code></a> this op may change the dtype
depending on the writer, for both practical and efficiency concerns.

#### Args:


* <b>`name`</b>: An arbitrary name for this summary.
* <b>`tensor`</b>: A <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> Must be one of the following types:
  `float32`, `float64`, `int32`, `int64`, `uint8`, `int16`,
  `int8`, `uint16`, `half`, `uint32`, `uint64`.
* <b>`family`</b>: Optional, the summary's family.
* <b>`step`</b>: The `int64` monotonic step variable, which defaults
  to <a href="../../../tf/train/get_global_step"><code>tf.compat.v1.train.get_global_step</code></a>.


#### Returns:

The created <a href="../../../tf/Operation"><code>tf.Operation</code></a> or a <a href="../../../tf/no_op"><code>tf.no_op</code></a> if summary writing has
not been enabled for this context.
