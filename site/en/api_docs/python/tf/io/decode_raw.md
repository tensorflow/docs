page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_raw


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/parsing_ops.py#L1835-L1874">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Convert raw byte strings into tensors.

### Aliases:

* `tf.compat.v2.io.decode_raw`


``` python
tf.io.decode_raw(
    input_bytes,
    out_type,
    little_endian=True,
    fixed_length=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input_bytes`</b>:   Each element of the input Tensor is converted to an array of bytes.
* <b>`out_type`</b>:   `DType` of the output. Acceptable types are `half`, `float`, `double`,
  `int32`, `uint16`, `uint8`, `int16`, `int8`, `int64`.
* <b>`little_endian`</b>:   Whether the `input_bytes` data is in little-endian format. Data will be
  converted into host byte order if necessary.
* <b>`fixed_length`</b>:   If set, the first `fixed_length` bytes of each element will be converted.
  Data will be zero-padded or truncated to the specified length.

  `fixed_length` must be a multiple of the size of `out_type`.
  `fixed_length` must be specified if the elements of `input_bytes` are of
  variable length.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` object storing the decoded bytes.
