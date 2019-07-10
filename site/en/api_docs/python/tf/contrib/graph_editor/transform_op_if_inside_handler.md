page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.transform_op_if_inside_handler

Transform an optional op only if it is inside the subgraph.

``` python
tf.contrib.graph_editor.transform_op_if_inside_handler(
    info,
    op,
    keep_if_possible=True
)
```



Defined in [`contrib/graph_editor/transform.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/transform.py).

<!-- Placeholder for "Used in" -->

This handler is typically use to handle original op: it is fine to keep them
if they are inside the subgraph, otherwise they are just ignored.

#### Args:


* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`op`</b>: the optional op to transform (or ignore).
* <b>`keep_if_possible`</b>: re-attach to the original op if possible, that is,
  if the source graph and the destination graph are the same.

#### Returns:

The transformed op or None.
