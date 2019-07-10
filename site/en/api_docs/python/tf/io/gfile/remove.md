page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.remove

``` python
tf.io.gfile.remove(path)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/lib/io/file_io.py).

Deletes the path located at 'path'.

#### Args:

* <b>`path`</b>: string, a path


#### Raises:

* <b>`errors.OpError`</b>: Propagates any errors reported by the FileSystem API.  E.g.,
  NotFoundError if the path does not exist.