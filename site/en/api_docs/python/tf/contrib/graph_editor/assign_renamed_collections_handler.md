page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.assign_renamed_collections_handler

Add the transformed elem to the (renamed) collections of elem.

``` python
tf.contrib.graph_editor.assign_renamed_collections_handler(
    info,
    elem,
    elem_
)
```



Defined in [`contrib/graph_editor/transform.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/transform.py).

<!-- Placeholder for "Used in" -->

A collection is renamed only if is not a known key, as described in
<a href="../../../tf/GraphKeys"><code>tf.compat.v1.GraphKeys</code></a>.

#### Args:


* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`elem`</b>: the original element (<a href="../../../tf/Tensor"><code>tf.Tensor</code></a> or <a href="../../../tf/Operation"><code>tf.Operation</code></a>)
* <b>`elem_`</b>: the transformed element