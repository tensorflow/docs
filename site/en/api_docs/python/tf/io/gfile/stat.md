page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.stat

``` python
tf.io.gfile.stat(path)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/lib/io/file_io.py).

Returns file statistics for a given path.

#### Args:

* <b>`path`</b>: string, path to a file


#### Returns:

FileStatistics struct that contains information about the path


#### Raises:

* <b>`errors.OpError`</b>: If the operation fails.