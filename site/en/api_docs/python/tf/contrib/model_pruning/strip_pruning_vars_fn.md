page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.strip_pruning_vars_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/strip_pruning_vars_lib.py#L74-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Removes mask variable from the graph.

``` python
tf.contrib.model_pruning.strip_pruning_vars_fn(
    input_graph_def,
    output_node_names
)
```



<!-- Placeholder for "Used in" -->

Replaces the masked_weight tensor with element-wise multiplication of mask
and the corresponding weight variable.

#### Args:


* <b>`input_graph_def`</b>: A GraphDef in which the variables have been converted to
  constants. This is typically the output of
  tf.graph_util.convert_variables_to_constant()
* <b>`output_node_names`</b>: List of name strings for the result nodes of the graph


#### Returns:

A GraphDef in which pruning-related variables have been removed
