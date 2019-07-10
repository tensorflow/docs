page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.meta_graph_transform.meta_graph_transform.meta_graph_transform

Apply the Graph Transform tool to a MetaGraphDef.

``` python
tf.contrib.meta_graph_transform.meta_graph_transform.meta_graph_transform(
    base_meta_graph_def,
    input_names,
    output_names,
    transforms,
    tags,
    checkpoint_path=None
)
```



Defined in [`contrib/meta_graph_transform/meta_graph_transform.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/meta_graph_transform/meta_graph_transform.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`base_meta_graph_def`</b>: A MetaGraphDef protocol buffer to transform.
* <b>`input_names`</b>: Names of input nodes.
* <b>`output_names`</b>: Names of output nodes.
* <b>`transforms`</b>: A list of strings naming the graph transforms to be applied in
  order.  These transform names are exactly those supported by the Graph
  Transform Tool, with the addition of the 'freeze_graph' and
  'sparsify_gather' transforms.
* <b>`tags`</b>: A list of tags with which to annotate the transformed MetaGraphDef.
* <b>`checkpoint_path`</b>: A path to a checkpoint to restore during freezing,
  if needed (default None).


#### Returns:

A new transformed MetaGraphDef protocol buffer.
