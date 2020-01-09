page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.write_file

### Aliases:

* `tf.io.write_file`
* `tf.write_file`

``` python
tf.io.write_file(
    filename,
    contents,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_io_ops.py`.

See the guide: [Inputs and Readers > Dealing with the filesystem](../../../../api_guides/python/io_ops#Dealing_with_the_filesystem)

Writes contents to the file at input filename. Creates file and recursively

creates directory if not existing.

#### Args:

* <b>`filename`</b>: A `Tensor` of type `string`.
    scalar. The name of the file to which we write the contents.
* <b>`contents`</b>: A `Tensor` of type `string`.
    scalar. The content to be written to the output file.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.