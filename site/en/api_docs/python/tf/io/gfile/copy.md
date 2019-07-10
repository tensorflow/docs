page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.gfile.copy

Copies data from `src` to `dst`.

### Aliases:

* `tf.compat.v1.io.gfile.copy`
* `tf.compat.v2.io.gfile.copy`
* `tf.io.gfile.copy`

``` python
tf.io.gfile.copy(
    src,
    dst,
    overwrite=False
)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`src`</b>: string, name of the file whose contents need to be copied
* <b>`dst`</b>: string, name of the file to which to copy to
* <b>`overwrite`</b>: boolean, if false it's an error for `dst` to be occupied by an
  existing file.


#### Raises:


* <b>`errors.OpError`</b>: If the operation fails.