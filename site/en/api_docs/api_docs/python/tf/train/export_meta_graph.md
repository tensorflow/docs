

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.export_meta_graph

``` python
export_meta_graph(
    filename=None,
    meta_info_def=None,
    graph_def=None,
    saver_def=None,
    collection_list=None,
    as_text=False,
    graph=None,
    export_scope=None,
    clear_devices=False,
    clear_extraneous_savers=False,
    **kwargs
)
```



Defined in [`tensorflow/python/training/saver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/training/saver.py).

See the guides: [Exporting and Importing a MetaGraph](../../../../api_guides/python/meta_graph), [Variables > Exporting and Importing Meta Graphs](../../../../api_guides/python/state_ops#Exporting_and_Importing_Meta_Graphs)

Returns `MetaGraphDef` proto. Optionally writes it to filename.

This function exports the graph, saver, and collection objects into
`MetaGraphDef` protocol buffer with the intention of it being imported
at a later time or location to restart training, run inference, or be
a subgraph.

#### Args:

* <b>`filename`</b>: Optional filename including the path for writing the
    generated `MetaGraphDef` protocol buffer.
* <b>`meta_info_def`</b>: `MetaInfoDef` protocol buffer.
* <b>`graph_def`</b>: `GraphDef` protocol buffer.
* <b>`saver_def`</b>: `SaverDef` protocol buffer.
* <b>`collection_list`</b>: List of string keys to collect.
* <b>`as_text`</b>: If `True`, writes the `MetaGraphDef` as an ASCII proto.
* <b>`graph`</b>: The `Graph` to import into. If `None`, use the default graph.
* <b>`export_scope`</b>: Optional `string`. Name scope under which to extract
    the subgraph. The scope name will be striped from the node definitions
    for easy import later into new name scopes. If `None`, the whole graph
    is exported. graph_def and export_scope cannot both be specified.
* <b>`clear_devices`</b>: Whether or not to clear the device field for an `Operation`
    or `Tensor` during export.
* <b>`clear_extraneous_savers`</b>: Remove any Saver-related information from the
      graph (both Save/Restore ops and SaverDefs) that are not associated
      with the provided SaverDef.
* <b>`**kwargs`</b>: Optional keyed arguments.


#### Returns:

A `MetaGraphDef` proto.


#### Raises:

* <b>`ValueError`</b>: When the `GraphDef` is larger than 2GB.