page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.exists

Determines whether a path exists or not.

### Aliases:

* `tf.compat.v1.io.gfile.exists`
* `tf.compat.v2.io.gfile.exists`
* `tf.io.gfile.exists`

``` python
tf.io.gfile.exists(path)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, a path


#### Returns:

True if the path exists, whether it's a file or a directory.
False if the path does not exist and there are no filesystem errors.



#### Raises:


* <b>`errors.OpError`</b>: Propagates any errors reported by the FileSystem API.