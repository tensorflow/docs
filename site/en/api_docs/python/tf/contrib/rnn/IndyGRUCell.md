page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.IndyGRUCell

## Class `IndyGRUCell`

Independently Gated Recurrent Unit cell.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->

Based on IndRNNs (https://arxiv.org/abs/1803.04831) and similar to GRUCell,
yet with the \\(U_r\\), \\(U_z\\), and \\(U\\) matrices in equations 5, 6, and
8 of http://arxiv.org/abs/1406.1078 respectively replaced by diagonal
matrices, i.e. a Hadamard product with a single vector:

<div>   $$r_j = \sigma\left([\mathbf W_r\mathbf x]_j +
    [\mathbf u_r\circ \mathbf h_{(t-1)}]_j\right)$$</div>
<div>   $$z_j = \sigma\left([\mathbf W_z\mathbf x]_j +
    [\mathbf u_z\circ \mathbf h_{(t-1)}]_j\right)$$</div>
<div>   $$\tilde{h}^{(t)}_j = \phi\left([\mathbf W \mathbf x]_j +
    [\mathbf u \circ \mathbf r \circ \mathbf h_{(t-1)}]_j\right)$$</div>

where \\(\circ\\) denotes the Hadamard operator. This means that each IndyGRU
node sees only its own state, as opposed to seeing all states in the same
layer.

#### Args:


* <b>`num_units`</b>: int, The number of units in the GRU cell.
* <b>`activation`</b>: Nonlinearity to use.  Default: `tanh`.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
 in an existing scope.  If not `True`, and the existing scope already has
 the given variables, an error is raised.
* <b>`kernel_initializer`</b>: (optional) The initializer to use for the weight
  matrices applied to the input.
* <b>`bias_initializer`</b>: (optional) The initializer to use for the bias.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will
  share weights, but to avoid mistakes we require reuse=True in such
  cases.
* <b>`dtype`</b>: Default dtype of the layer (default of `None` means use the type
  of the first input). Required when `build` is called before `call`.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    activation=None,
    reuse=None,
    kernel_initializer=None,
    bias_initializer=None,
    name=None,
    dtype=None
)
```






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




