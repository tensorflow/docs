page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.listdir

Returns a list of entries contained within a directory.

### Aliases:

* `tf.compat.v1.io.gfile.listdir`
* `tf.compat.v2.io.gfile.listdir`
* `tf.io.gfile.listdir`

``` python
tf.io.gfile.listdir(path)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->

The list is in arbitrary order. It does not contain the special entries "."
and "..".

#### Args:


* <b>`path`</b>: string, path to a directory


#### Returns:

[filename1, filename2, ... filenameN] as strings



#### Raises:

errors.NotFoundError if directory doesn't exist
