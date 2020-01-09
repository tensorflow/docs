page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.write


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/summary_ops_v2.py#L589-L649">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Writes a generic summary to the default SummaryWriter if one exists.

### Aliases:

* `tf.compat.v2.summary.write`


``` python
tf.summary.write(
    tag,
    tensor,
    step=None,
    metadata=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This exists primarily to support the definition of type-specific summary ops
like scalar() and image(), and is not intended for direct use unless defining
a new type-specific summary op.

#### Args:


* <b>`tag`</b>: string tag used to identify the summary (e.g. in TensorBoard), usually
  generated with `tf.summary.summary_scope`
* <b>`tensor`</b>: the Tensor holding the summary data to write
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to <a href="../../tf/summary/experimental/get_step"><code>tf.summary.experimental.get_step()</code></a>, which must
  not be None.
* <b>`metadata`</b>: Optional SummaryMetadata, as a proto or serialized bytes
* <b>`name`</b>: Optional string name for this op.


#### Returns:

True on success, or false if no summary was written because no default
summary writer was available.



#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  <a href="../../tf/summary/experimental/get_step"><code>tf.summary.experimental.get_step()</code></a> is None.
