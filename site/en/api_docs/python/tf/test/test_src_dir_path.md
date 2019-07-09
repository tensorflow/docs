page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.test_src_dir_path

``` python
tf.test.test_src_dir_path(relative_path)
```



Defined in [`tensorflow/python/platform/test.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/platform/test.py).

Creates an absolute test srcdir path given a relative path.

#### Args:

* <b>`relative_path`</b>: a path relative to tensorflow root.
    e.g. "core/platform".


#### Returns:

An absolute path to the linked in runfiles.