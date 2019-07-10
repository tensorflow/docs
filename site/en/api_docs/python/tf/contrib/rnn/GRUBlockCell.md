page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.GRUBlockCell

## Class `GRUBlockCell`

Block GRU cell implementation.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell)



Defined in [`contrib/rnn/python/ops/gru_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/gru_ops.py).

<!-- Placeholder for "Used in" -->

Deprecated: use GRUBlockCellV2 instead.

The implementation is based on:  http://arxiv.org/abs/1406.1078
Computes the GRU cell forward propagation for 1 time step.

This kernel op implements the following mathematical equations:

Biases are initialized with:

* `b_ru` - constant_initializer(1.0)
* `b_c` - constant_initializer(0.0)

```
x_h_prev = [x, h_prev]

[r_bar u_bar] = x_h_prev * w_ru + b_ru

r = sigmoid(r_bar)
u = sigmoid(u_bar)

h_prevr = h_prev \circ r

x_h_prevr = [x h_prevr]

c_bar = x_h_prevr * w_c + b_c
c = tanh(c_bar)

h = (1-u) \circ c + u \circ h_prev
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units=None,
    cell_size=None,
    reuse=None,
    name='gru_cell'
)
```

Initialize the Block GRU cell. (deprecated arguments)

Warning: SOME ARGUMENTS ARE DEPRECATED: `(cell_size)`. They will be removed in a future version.
Instructions for updating:
cell_size is deprecated, use num_units instead

#### Args:


* <b>`num_units`</b>: int, The number of units in the GRU cell.
* <b>`cell_size`</b>: int, The old (deprecated) name for `num_units`.
* <b>`reuse`</b>: (optional) boolean describing whether to reuse variables in an
  existing scope.  If not `True`, and the existing scope already has the
  given variables, an error is raised.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will
  share weights, but to avoid mistakes we require reuse=True in such
  cases.  By default this is "lstm_cell", for variable-name compatibility
  with <a href="../../../tf/nn/rnn_cell/GRUCell"><code>tf.compat.v1.nn.rnn_cell.GRUCell</code></a>.


#### Raises:


* <b>`ValueError`</b>: if both cell_size and num_units are not None;
  or both are None.



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




