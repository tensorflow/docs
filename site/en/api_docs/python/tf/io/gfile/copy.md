page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.copy

``` python
tf.io.gfile.copy(
    src,
    dst,
    overwrite=False
)
```



Defined in [`tensorflow/python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/lib/io/file_io.py).

Copies data from src to dst.

#### Args:

* <b>`src`</b>: string, name of the file whose contents need to be copied
* <b>`dst`</b>: string, name of the file to which to copy to
* <b>`overwrite`</b>: boolean, if false its an error for newpath to be occupied by an
      existing file.


#### Raises:

* <b>`errors.OpError`</b>: If the operation fails.