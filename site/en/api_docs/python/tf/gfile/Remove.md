page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Remove

Deletes the file located at 'filename'.

### Aliases:

* `tf.compat.v1.gfile.Remove`
* `tf.gfile.Remove`

``` python
tf.gfile.Remove(filename)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filename`</b>: string, a filename


#### Raises:


* <b>`errors.OpError`</b>: Propagates any errors reported by the FileSystem API.  E.g.,
NotFoundError if the file does not exist.