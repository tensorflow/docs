page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.graph_def_from_checkpoint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/strip_pruning_vars_lib.py#L113-L142">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts checkpoint data to GraphDef.

``` python
tf.contrib.model_pruning.graph_def_from_checkpoint(
    checkpoint_dir,
    output_node_names
)
```



<!-- Placeholder for "Used in" -->

Reads the latest checkpoint data and produces a GraphDef in which the
variables have been converted to constants.

#### Args:


* <b>`checkpoint_dir`</b>: Path to the checkpoints.
* <b>`output_node_names`</b>: List of name strings for the result nodes of the graph.


#### Returns:

A GraphDef from the latest checkpoint



#### Raises:


* <b>`ValueError`</b>: if no checkpoint is found
