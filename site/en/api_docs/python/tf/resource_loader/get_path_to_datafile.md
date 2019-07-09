page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.resource_loader.get_path_to_datafile

``` python
tf.resource_loader.get_path_to_datafile(path)
```



Defined in [`tensorflow/python/platform/resource_loader.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/platform/resource_loader.py).

Get the path to the specified file in the data dependencies.

The path is relative to tensorflow/

#### Args:

* <b>`path`</b>: a string resource path relative to tensorflow/


#### Returns:

The path to the specified file present in the data attribute of py_test
or py_binary.


#### Raises:

* <b>`IOError`</b>: If the path is not found, or the resource can't be opened.