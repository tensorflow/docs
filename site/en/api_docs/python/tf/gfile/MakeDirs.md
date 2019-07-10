page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.MakeDirs

Creates a directory and all parent/intermediate directories.

### Aliases:

* `tf.compat.v1.gfile.MakeDirs`
* `tf.gfile.MakeDirs`

``` python
tf.gfile.MakeDirs(dirname)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->

It succeeds if dirname already exists and is writable.

#### Args:


* <b>`dirname`</b>: string, name of the directory to be created


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.