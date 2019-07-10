page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.gfile.Walk

Recursive directory tree generator for directories.

### Aliases:

* `tf.compat.v1.gfile.Walk`
* `tf.gfile.Walk`

``` python
tf.gfile.Walk(
    top,
    in_order=True
)
```



Defined in [`python/lib/io/file_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/lib/io/file_io.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`top`</b>: string, a Directory name
* <b>`in_order`</b>: bool, Traverse in order if True, post order if False.  Errors that
  happen while listing directories are ignored.


#### Yields:

Each yield is a 3-tuple:  the pathname of a directory, followed by lists of
all its subdirectories and leaf files.
(dirname, [subdirname, subdirname, ...], [filename, filename, ...])
as strings
