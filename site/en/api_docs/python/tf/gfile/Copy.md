page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Copy

Copies data from `oldpath` to `newpath`.

### Aliases:

* `tf.compat.v1.gfile.Copy`
* `tf.gfile.Copy`

``` python
tf.gfile.Copy(
    oldpath,
    newpath,
    overwrite=False
)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`oldpath`</b>: string, name of the file who's contents need to be copied
* <b>`newpath`</b>: string, name of the file to which to copy to
* <b>`overwrite`</b>: boolean, if false it's an error for `newpath` to be occupied by
  an existing file.


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.