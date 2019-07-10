page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.IndyLSTMCell

## Class `IndyLSTMCell`

Basic IndyLSTM recurrent network cell.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->

Based on IndRNNs (https://arxiv.org/abs/1803.04831) and similar to
BasicLSTMCell, yet with the \\(U_f\\), \\(U_i\\), \\(U_o\\) and \\(U_c\\)
matrices in the regular LSTM equations replaced by diagonal matrices, i.e. a
Hadamard product with a single vector:

<div>   $$f_t = \sigma_g\left(W_f x_t + u_f \circ h_{t-1} + b_f\right)$$ </div>
<div>   $$i_t = \sigma_g\left(W_i x_t + u_i \circ h_{t-1} + b_i\right)$$ </div>
<div>   $$o_t = \sigma_g\left(W_o x_t + u_o \circ h_{t-1} + b_o\right)$$ </div>
<div>   $$c_t = f_t \circ c_{t-1} +
          i_t \circ \sigma_c\left(W_c x_t + u_c \circ h_{t-1} + b_c\right)$$</div>

where \\(\circ\\) denotes the Hadamard operator. This means that each IndyLSTM
node sees only its own state \\(h\\) and \\(c\\), as opposed to seeing all
states in the same layer.

We add forget_bias (default: 1) to the biases of the forget gate in order to
reduce the scale of forgetting in the beginning of the training.

It does not allow cell clipping, a projection layer, and does not
use peep-hole connections: it is the basic baseline.

For a detailed analysis of IndyLSTMs, see https://arxiv.org/abs/1903.08023.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    forget_bias=1.0,
    activation=None,
    reuse=None,
    kernel_initializer=None,
    bias_initializer=None,
    name=None,
    dtype=None
)
```

Initialize the IndyLSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell.
* <b>`forget_bias`</b>: float, The bias added to forget gates (see above).
  Must set to `0.0` manually when restoring from CudnnLSTM-trained
  checkpoints.
* <b>`activation`</b>: Activation function of the inner states.  Default: `tanh`.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.
* <b>`kernel_initializer`</b>: (optional) The initializer to use for the weight
  matrix applied to the inputs.
* <b>`bias_initializer`</b>: (optional) The initializer to use for the bias.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will
  share weights, but to avoid mistakes we require reuse=True in such
  cases.
* <b>`dtype`</b>: Default dtype of the layer (default of `None` means use the type
  of the first input). Required when `build` is called before `call`.



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




