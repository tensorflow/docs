

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.DeleteRecursively

``` python
tf.gfile.DeleteRecursively(dirname)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/lib/io/file_io.py).

Deletes everything under dirname recursively.

#### Args:

* <b>`dirname`</b>: string, a path to a directory


#### Raises:

* <b>`errors.OpError`</b>: If the operation fails.