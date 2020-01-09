page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.load_op_library


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/load_library.py#L38-L86">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads a TensorFlow plugin, containing custom ops and kernels.

### Aliases:

* `tf.compat.v1.load_op_library`
* `tf.compat.v2.load_op_library`


``` python
tf.load_op_library(library_filename)
```



<!-- Placeholder for "Used in" -->

Pass "library_filename" to a platform-specific mechanism for dynamically
loading a library. The rules for determining the exact location of the
library are platform-specific and are not documented here. When the
library is loaded, ops and kernels registered in the library via the
`REGISTER_*` macros are made available in the TensorFlow process. Note
that ops with the same name as an existing op are rejected and not
registered with the process.

#### Args:


* <b>`library_filename`</b>: Path to the plugin.
  Relative or absolute filesystem path to a dynamic library file.


#### Returns:

A python module containing the Python wrappers for Ops defined in
the plugin.



#### Raises:


* <b>`RuntimeError`</b>: when unable to load the library or get the python wrappers.
