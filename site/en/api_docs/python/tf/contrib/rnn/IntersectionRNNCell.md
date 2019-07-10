page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.IntersectionRNNCell

## Class `IntersectionRNNCell`

Intersection Recurrent Neural Network (+RNN) cell.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->

Architecture with coupled recurrent gate as well as coupled depth
gate, designed to improve information flow through stacked RNNs. As the
architecture uses depth gating, the dimensionality of the depth
output (y) also should not change through depth (input size == output size).
To achieve this, the first layer of a stacked Intersection RNN projects
the inputs to N (num units) dimensions. Therefore when initializing an
IntersectionRNNCell, one should set `num_in_proj = N` for the first layer
and use default settings for subsequent layers.

This implements the recurrent cell from the paper:

  https://arxiv.org/abs/1611.09913

Jasmine Collins, Jascha Sohl-Dickstein, and David Sussillo.
"Capacity and Trainability in Recurrent Neural Networks" Proc. ICLR 2017.

The Intersection RNN is built for use in deeply stacked
RNNs so it may not achieve best performance with depth 1.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    num_in_proj=None,
    initializer=None,
    forget_bias=1.0,
    y_activation=tf.nn.relu,
    reuse=None
)
```

Initialize the parameters for an +RNN cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the +RNN cell
* <b>`num_in_proj`</b>: (optional) int, The input dimensionality for the RNN.
  If creating the first layer of an +RNN, this should be set to
  `num_units`. Otherwise, this should be set to `None` (default).
  If `None`, dimensionality of `inputs` should be equal to `num_units`,
  otherwise ValueError is thrown.
* <b>`initializer`</b>: (optional) The initializer to use for the weight matrices.
* <b>`forget_bias`</b>: (optional) float, default 1.0, The initial bias of the
  forget gates, used to reduce the scale of forgetting at the beginning
  of the training.
* <b>`y_activation`</b>: (optional) Activation function of the states passed
  through depth. Default is 'tf.nn.relu`.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>




<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```

Return zero-filled state tensor(s).


#### Args:


* <b>`batch_size`</b>: int, float, or unit Tensor representing the batch size.
* <b>`dtype`</b>: the data type to use for the state.


#### Returns:

If `state_size` is an int or TensorShape, then the return value is a
`N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

If `state_size` is a nested list or tuple, then the return value is
a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size, s]` for each s in `state_size`.




