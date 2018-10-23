

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.graph_util.remove_training_nodes

### `tf.graph_util.remove_training_nodes`

``` python
remove_training_nodes(input_graph)
```



Defined in [`tensorflow/python/framework/graph_util_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/framework/graph_util_impl.py).

Prunes out nodes that aren't needed for inference.

There are nodes like Identity and CheckNumerics that are only useful
during training, and can be removed in graphs that will be used for
nothing but inference. Here we identify and remove them, returning an
equivalent graph. To be specific, CheckNumerics nodes are always removed, and
Identity nodes that aren't involved in control edges are spliced out so that
their input and outputs are directly connected.

#### Args:

* <b>`input_graph`</b>: Model to analyze and prune.


#### Returns:

  A list of nodes with the unnecessary ones removed.