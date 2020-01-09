page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.summary.experimental.write_raw_pb


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/summary_ops_v2.py#L652-L701">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Writes a summary using raw <a href="../../../tf/compat/v1/Summary"><code>tf.compat.v1.Summary</code></a> protocol buffers.

### Aliases:

* `tf.compat.v2.summary.experimental.write_raw_pb`


``` python
tf.summary.experimental.write_raw_pb(
    tensor,
    step=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Experimental: this exists to support the usage of V1-style manual summary
writing (via the construction of a <a href="../../../tf/compat/v1/Summary"><code>tf.compat.v1.Summary</code></a> protocol buffer)
with the V2 summary writing API.

#### Args:


* <b>`tensor`</b>: the string Tensor holding one or more serialized `Summary` protobufs
* <b>`step`</b>: Explicit `int64`-castable monotonic step value for this summary. If
  omitted, this defaults to <a href="../../../tf/summary/experimental/get_step"><code>tf.summary.experimental.get_step()</code></a>, which must
  not be None.
* <b>`name`</b>: Optional string name for this op.


#### Returns:

True on success, or false if no summary was written because no default
summary writer was available.



#### Raises:


* <b>`ValueError`</b>: if a default writer exists, but no step was provided and
  <a href="../../../tf/summary/experimental/get_step"><code>tf.summary.experimental.get_step()</code></a> is None.
