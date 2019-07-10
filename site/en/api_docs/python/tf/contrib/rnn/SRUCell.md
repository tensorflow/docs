page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.SRUCell

## Class `SRUCell`

SRU, Simple Recurrent Unit.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->

   Implementation based on
   Training RNNs as Fast as CNNs (cf. https://arxiv.org/abs/1709.02755).

   This variation of RNN cell is characterized by the simplified data
   dependence
   between hidden states of two consecutive time steps. Traditionally, hidden
   states from a cell at time step t-1 needs to be multiplied with a matrix
   W_hh before being fed into the ensuing cell at time step t.
   This flavor of RNN replaces the matrix multiplication between h_{t-1}
   and W_hh with a pointwise multiplication, resulting in performance
   gain.

#### Args:


* <b>`num_units`</b>: int, The number of units in the SRU cell.
* <b>`activation`</b>: Nonlinearity to use.  Default: `tanh`.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.
* <b>`name`</b>: (optional) String, the name of the layer. Layers with the same name
  will share weights, but to avoid mistakes we require reuse=True in such
  cases.
* <b>`**kwargs`</b>: Additional keyword arguments.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    activation=None,
    reuse=None,
    name=None,
    **kwargs
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




