page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_compressed


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/decode_compressed">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_parsing_ops.py`



Decompress strings.

### Aliases:

* <a href="/api_docs/python/tf/io/decode_compressed"><code>tf.compat.v1.decode_compressed</code></a>
* <a href="/api_docs/python/tf/io/decode_compressed"><code>tf.compat.v1.io.decode_compressed</code></a>
* <a href="/api_docs/python/tf/io/decode_compressed"><code>tf.compat.v2.io.decode_compressed</code></a>
* <a href="/api_docs/python/tf/io/decode_compressed"><code>tf.decode_compressed</code></a>


``` python
tf.io.decode_compressed(
    bytes,
    compression_type='',
    name=None
)
```



<!-- Placeholder for "Used in" -->

This op decompresses each element of the `bytes` input `Tensor`, which
is assumed to be compressed using the given `compression_type`.

The `output` is a string `Tensor` of the same shape as `bytes`,
each element containing the decompressed data from the corresponding
element in `bytes`.

#### Args:


* <b>`bytes`</b>: A `Tensor` of type `string`.
  A Tensor of string which is compressed.
* <b>`compression_type`</b>: An optional `string`. Defaults to `""`.
  A scalar containing either (i) the empty string (no
  compression), (ii) "ZLIB", or (iii) "GZIP".
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
