page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.flatten_with_joined_string_paths

Returns a list of (string path, data element) tuples.

``` python
tf.contrib.framework.nest.flatten_with_joined_string_paths(
    structure,
    separator='/',
    expand_composites=False
)
```



Defined in [`python/util/nest.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/util/nest.py).

<!-- Placeholder for "Used in" -->

The order of tuples produced matches that of `nest.flatten`. This allows you
to flatten a nested structure while keeping information about where in the
structure each data element was located. See `nest.yield_flat_paths`
for more information.

#### Args:


* <b>`structure`</b>: the nested structure to flatten.
* <b>`separator`</b>: string to separate levels of hierarchy in the results, defaults
  to '/'.
* <b>`expand_composites`</b>: If true, then composite tensors such as tf.SparseTensor
   and tf.RaggedTensor are expanded into their component tensors.


#### Returns:

A list of (string, data element) tuples.
