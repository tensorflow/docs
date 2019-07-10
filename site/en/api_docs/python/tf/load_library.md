page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.load_library

Loads a TensorFlow plugin.

### Aliases:

* `tf.compat.v1.load_library`
* `tf.compat.v2.load_library`
* `tf.load_library`

``` python
tf.load_library(library_location)
```



Defined in [`python/framework/load_library.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/load_library.py).

<!-- Placeholder for "Used in" -->

"library_location" can be a path to a specific shared object, or a folder.
If it is a folder, all shared objects that are named "libtfkernel*" will be
loaded. When the library is loaded, kernels registered in the library via the
`REGISTER_*` macros are made available in the TensorFlow process.

#### Args:


* <b>`library_location`</b>: Path to the plugin or the folder of plugins.
  Relative or absolute filesystem path to a dynamic library file or folder.


#### Returns:

None



#### Raises:


* <b>`OSError`</b>: When the file to be loaded is not found.
* <b>`RuntimeError`</b>: when unable to load the library.