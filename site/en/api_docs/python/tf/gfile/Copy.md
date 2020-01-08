page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Copy

``` python
tf.gfile.Copy(
    oldpath,
    newpath,
    overwrite=False
)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/lib/io/file_io.py).

Copies data from oldpath to newpath.

#### Args:

* <b>`oldpath`</b>: string, name of the file who's contents need to be copied
* <b>`newpath`</b>: string, name of the file to which to copy to
* <b>`overwrite`</b>: boolean, if false its an error for newpath to be occupied by an
      existing file.


#### Raises:

* <b>`errors.OpError`</b>: If the operation fails.