page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.matching_files


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/matching_files">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_io_ops.py`



Returns the set of files matching one or more glob patterns.

### Aliases:

* <a href="/api_docs/python/tf/io/matching_files"><code>tf.compat.v1.io.matching_files</code></a>
* <a href="/api_docs/python/tf/io/matching_files"><code>tf.compat.v1.matching_files</code></a>
* <a href="/api_docs/python/tf/io/matching_files"><code>tf.compat.v2.io.matching_files</code></a>
* <a href="/api_docs/python/tf/io/matching_files"><code>tf.matching_files</code></a>


``` python
tf.io.matching_files(
    pattern,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Note that this routine only supports wildcard characters in the
basename portion of the pattern, not in the directory portion.
Note also that the order of filenames returned is deterministic.

#### Args:


* <b>`pattern`</b>: A `Tensor` of type `string`.
  Shell wildcard pattern(s). Scalar or vector of type string.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
