page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.flatten_with_joined_string_paths


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/nest.py#L1280-L1304">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a list of (string path, data element) tuples.

``` python
tf.contrib.framework.nest.flatten_with_joined_string_paths(
    structure,
    separator='/',
    expand_composites=False
)
```



<!-- Placeholder for "Used in" -->

The order of tuples produced matches that of <a href="/api_docs/python/tf/nest/flatten"><code>nest.flatten</code></a>. This allows you
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
