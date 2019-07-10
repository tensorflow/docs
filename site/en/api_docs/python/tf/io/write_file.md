page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.write_file

Writes contents to the file at input filename. Creates file and recursively

### Aliases:

* `tf.compat.v1.io.write_file`
* `tf.compat.v1.write_file`
* `tf.compat.v2.io.write_file`
* `tf.io.write_file`
* `tf.write_file`

``` python
tf.io.write_file(
    filename,
    contents,
    name=None
)
```



Defined in generated file: `python/ops/gen_io_ops.py`.

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
