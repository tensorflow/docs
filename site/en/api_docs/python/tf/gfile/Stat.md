page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Stat

Returns file statistics for a given path.

### Aliases:

* `tf.compat.v1.gfile.Stat`
* `tf.gfile.Stat`

``` python
tf.gfile.Stat(filename)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`filename`</b>: string, path to a file


#### Returns:

FileStatistics struct that contains information about the path



#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.