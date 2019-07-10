page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.mkdir

Creates a directory with the name given by 'path'.

### Aliases:

* `tf.compat.v1.io.gfile.mkdir`
* `tf.compat.v2.io.gfile.mkdir`
* `tf.io.gfile.mkdir`

``` python
tf.io.gfile.mkdir(path)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`path`</b>: string, name of the directory to be created
Notes: The parent directories need to exist. Use recursive_create_dir instead
  if there is the possibility that the parent dirs don't exist.

#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.