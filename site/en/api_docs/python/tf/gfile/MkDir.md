page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.MkDir

Creates a directory with the name 'dirname'.

### Aliases:

* `tf.compat.v1.gfile.MkDir`
* `tf.gfile.MkDir`

``` python
tf.gfile.MkDir(dirname)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`dirname`</b>: string, name of the directory to be created
Notes: The parent directories need to exist. Use recursive_create_dir instead
  if there is the possibility that the parent dirs don't exist.

#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.