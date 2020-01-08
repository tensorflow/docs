page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.load_library

``` python
tf.load_library(library_location)
```



Defined in [`tensorflow/python/framework/load_library.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/framework/load_library.py).

Loads a TensorFlow plugin.

"library_location" can be a path to a specific shared object, or a folder.
If it is a folder, all sahred objects that are named "libtfkernel*" will be
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