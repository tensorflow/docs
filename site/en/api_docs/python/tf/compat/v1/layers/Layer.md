page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.layers.Layer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/layers/base.py#L158-L579">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Layer`

Base layer class.

Inherits From: [`Layer`](../../../../tf/keras/layers/Layer)

<!-- Placeholder for "Used in" -->

It is considered legacy, and we recommend the use of <a href="../../../../tf/keras/layers/Layer"><code>tf.keras.layers.Layer</code></a>
instead.

#### Arguments:


* <b>`trainable`</b>: Boolean, whether the layer's variables should be trainable.
* <b>`name`</b>: String name of the layer.
* <b>`dtype`</b>: Default dtype of the layer's weights (default of `None` means use the
  type of the first input).

Read-only properties:
  name: The name of the layer (string).
  dtype: Default dtype of the layer's weights (default of `None` means use the
    type of the first input).
  trainable_variables: List of trainable variables.
  non_trainable_variables: List of non-trainable variables.
  variables: List of all variables of this layer, trainable and
    non-trainable.
  updates: List of update ops of this layer.
  losses: List of losses added by this layer.
  trainable_weights: List of variables to be included in backprop.
  non_trainable_weights: List of variables that should not be
    included in backprop.
  weights: The concatenation of the lists trainable_weights and
    non_trainable_weights (in this order).

#### Mutable properties:


* <b>`trainable`</b>: Whether the layer should be trained (boolean).
* <b>`input_spec`</b>: Optional (list of) `InputSpec` object(s) specifying the
  constraints on inputs that can be accepted by the layer.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/layers/base.py#L192-L235">View source</a>

``` python
__init__(
    trainable=True,
    name=None,
    dtype=None,
    **kwargs
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="scope_name"><code>scope_name</code></h3>
