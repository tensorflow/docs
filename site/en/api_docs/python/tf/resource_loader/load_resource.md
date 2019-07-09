page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.resource_loader.load_resource

``` python
tf.resource_loader.load_resource(path)
```



Defined in [`tensorflow/python/platform/resource_loader.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/platform/resource_loader.py).

Load the resource at given path, where path is relative to tensorflow/.

#### Args:

* <b>`path`</b>: a string resource path relative to tensorflow/.


#### Returns:

The contents of that resource.


#### Raises:

* <b>`IOError`</b>: If the path is not found, or the resource can't be opened.