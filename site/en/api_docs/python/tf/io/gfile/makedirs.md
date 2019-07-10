page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.makedirs

Creates a directory and all parent/intermediate directories.

### Aliases:

* `tf.compat.v1.io.gfile.makedirs`
* `tf.compat.v2.io.gfile.makedirs`
* `tf.io.gfile.makedirs`

``` python
tf.io.gfile.makedirs(path)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->

It succeeds if path already exists and is writable.

#### Args:


* <b>`path`</b>: string, name of the directory to be created


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.