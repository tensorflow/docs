page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.remove

Deletes the path located at 'path'.

### Aliases:

* `tf.compat.v1.io.gfile.remove`
* `tf.compat.v2.io.gfile.remove`
* `tf.io.gfile.remove`

``` python
tf.io.gfile.remove(path)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, a path


#### Raises:


* <b>`errors.OpError`</b>: Propagates any errors reported by the FileSystem API.  E.g.,
NotFoundError if the path does not exist.