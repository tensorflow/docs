page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Remove

``` python
tf.gfile.Remove(filename)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/lib/io/file_io.py).

Deletes the file located at 'filename'.

#### Args:

* <b>`filename`</b>: string, a filename


#### Raises:

* <b>`errors.OpError`</b>: Propagates any errors reported by the FileSystem API.  E.g.,
  NotFoundError if the file does not exist.