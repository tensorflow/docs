page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.load_file_system_library


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/load_library.py#L89-L109">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads a TensorFlow plugin, containing file system implementation. (deprecated)

``` python
tf.compat.v1.load_file_system_library(library_filename)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/load_library"><code>tf.load_library</code></a> instead.

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
