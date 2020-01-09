page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.flatten_with_tuple_paths


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/nest.py#L1307-L1327">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a list of `(tuple_path, leaf_element)` tuples.

``` python
tf.contrib.framework.nest.flatten_with_tuple_paths(
    structure,
    expand_composites=False
)
```



<!-- Placeholder for "Used in" -->

The order of pairs produced matches that of <a href="/api_docs/python/tf/nest/flatten"><code>nest.flatten</code></a>. This allows you
to flatten a nested structure while keeping information about where in the
structure each data element was located. See `nest.yield_flat_paths`
for more information about tuple paths.

#### Args:


* <b>`structure`</b>: the nested structure to flatten.
* <b>`expand_composites`</b>: If true, then composite tensors such as tf.SparseTensor
   and tf.RaggedTensor are expanded into their component tensors.


#### Returns:

A list of `(tuple_path, leaf_element)` tuples. Each `tuple_path` is a tuple
of indices and/or dictionary keys that uniquely specify the path to
`leaf_element` within `structure`.
