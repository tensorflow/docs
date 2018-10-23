


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.load_file_system_library

### `tf.load_file_system_library`

```
tf.load_file_system_library(library_filename)
```


See the guide: [Building Graphs > Utility functions](../../../api_guides/python/framework#Utility_functions)

Loads a TensorFlow plugin, containing file system implementation.

Pass `library_filename` to a platform-specific mechanism for dynamically
loading a library. The rules for determining the exact location of the
library are platform-specific and are not documented here.

#### Args:

* <b>`library_filename`</b>: Path to the plugin.
    Relative or absolute filesystem path to a dynamic library file.


#### Returns:

  None.


#### Raises:

* <b>`RuntimeError`</b>: when unable to load the library.

Defined in [`tensorflow/python/framework/load_library.py`](https://www.tensorflow.org/code/tensorflow/python/framework/load_library.py).

