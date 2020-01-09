page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.write_file


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/write_file">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_io_ops.py`



Writes contents to the file at input filename. Creates file and recursively

### Aliases:

* <a href="/api_docs/python/tf/io/write_file"><code>tf.compat.v1.io.write_file</code></a>
* <a href="/api_docs/python/tf/io/write_file"><code>tf.compat.v1.write_file</code></a>
* <a href="/api_docs/python/tf/io/write_file"><code>tf.compat.v2.io.write_file</code></a>
* <a href="/api_docs/python/tf/io/write_file"><code>tf.write_file</code></a>


``` python
tf.io.write_file(
    filename,
    contents,
    name=None
)
```



<!-- Placeholder for "Used in" -->

creates directory if not existing.

#### Args:


* <b>`filename`</b>: A `Tensor` of type `string`.
  scalar. The name of the file to which we write the contents.
* <b>`contents`</b>: A `Tensor` of type `string`.
  scalar. The content to be written to the output file.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.
