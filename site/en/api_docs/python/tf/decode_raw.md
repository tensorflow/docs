page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.decode_raw


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/parsing_ops.py#L1877-L1917">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Convert raw byte strings into tensors. (deprecated arguments)

### Aliases:

* <a href="/api_docs/python/tf/decode_raw"><code>tf.compat.v1.decode_raw</code></a>
* <a href="/api_docs/python/tf/decode_raw"><code>tf.compat.v1.io.decode_raw</code></a>
* <a href="/api_docs/python/tf/decode_raw"><code>tf.io.decode_raw</code></a>


``` python
tf.decode_raw(
    input_bytes=None,
    out_type=None,
    little_endian=True,
    name=None,
    bytes=None
)
```



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(bytes)`. They will be removed in a future version.
Instructions for updating:
bytes is deprecated, use input_bytes instead

#### Args:


* <b>`input_bytes`</b>:   Each element of the input Tensor is converted to an array of bytes.
* <b>`out_type`</b>:   `DType` of the output. Acceptable types are `half`, `float`, `double`,
  `int32`, `uint16`, `uint8`, `int16`, `int8`, `int64`.
* <b>`little_endian`</b>:   Whether the `input_bytes` data is in little-endian format. Data will be
  converted into host byte order if necessary.
* <b>`name`</b>: A name for the operation (optional).
* <b>`bytes`</b>: Deprecated parameter. Use `input_bytes` instead.


#### Returns:

A `Tensor` object storing the decoded bytes.
