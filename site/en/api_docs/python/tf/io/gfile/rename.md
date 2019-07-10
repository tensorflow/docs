page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.rename

Rename or move a file / directory.

### Aliases:

* `tf.compat.v1.io.gfile.rename`
* `tf.compat.v2.io.gfile.rename`
* `tf.io.gfile.rename`

``` python
tf.io.gfile.rename(
    src,
    dst,
    overwrite=False
)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`src`</b>: string, pathname for a file
* <b>`dst`</b>: string, pathname to which the file needs to be moved
* <b>`overwrite`</b>: boolean, if false it's an error for `dst` to be occupied by an
  existing file.


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.