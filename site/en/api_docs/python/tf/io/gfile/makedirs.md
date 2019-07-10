page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.makedirs

``` python
tf.io.gfile.makedirs(path)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/lib/io/file_io.py).

Creates a directory and all parent/intermediate directories.

It succeeds if path already exists and is writable.

#### Args:

* <b>`path`</b>: string, name of the directory to be created


#### Raises:

* <b>`errors.OpError`</b>: If the operation fails.