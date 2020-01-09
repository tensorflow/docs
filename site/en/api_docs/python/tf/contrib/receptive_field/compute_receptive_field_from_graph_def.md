page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.receptive_field.compute_receptive_field_from_graph_def


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/receptive_field/python/util/receptive_field.py#L153-L391">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes receptive field (RF) parameters from a Graph or GraphDef object.

``` python
tf.contrib.receptive_field.compute_receptive_field_from_graph_def(
    graph_def,
    input_node,
    output_node,
    stop_propagation=None,
    input_resolution=None
)
```



<!-- Placeholder for "Used in" -->

The algorithm stops the calculation of the receptive field whenever it
encounters an operation in the list `stop_propagation`. Stopping the
calculation early can be useful to calculate the receptive field of a
subgraph such as a single branch of the
[inception network](https://arxiv.org/abs/1512.00567).

#### Args:


* <b>`graph_def`</b>: Graph or GraphDef object.
* <b>`input_node`</b>: Name of the input node or Tensor object from graph.
* <b>`output_node`</b>: Name of the output node or Tensor object from graph.
* <b>`stop_propagation`</b>: List of operations or scope names for which to stop the
  propagation of the receptive field.
* <b>`input_resolution`</b>: 2D list. If the input resolution to the model is fixed and
  known, this may be set. This is helpful for cases where the RF parameters
  vary depending on the input resolution (this happens since SAME padding in
  tensorflow depends on input resolution in general). If this is None, it is
  assumed that the input resolution is unknown, so some RF parameters may be
  unknown (depending on the model architecture).


#### Returns:


* <b>`rf_size_x`</b>: Receptive field size of network in the horizontal direction, with
  respect to specified input and output.
* <b>`rf_size_y`</b>: Receptive field size of network in the vertical direction, with
  respect to specified input and output.
* <b>`effective_stride_x`</b>: Effective stride of network in the horizontal direction,
  with respect to specified input and output.
* <b>`effective_stride_y`</b>: Effective stride of network in the vertical direction,
  with respect to specified input and output.
* <b>`effective_padding_x`</b>: Effective padding of network in the horizontal
  direction, with respect to specified input and output.
* <b>`effective_padding_y`</b>: Effective padding of network in the vertical
  direction, with respect to specified input and output.


#### Raises:


* <b>`ValueError`</b>: If network is not aligned or if either input or output nodes
  cannot be found. For network criterion alignment, see
  photos/vision/features/delf/g3doc/rf_computation.md
