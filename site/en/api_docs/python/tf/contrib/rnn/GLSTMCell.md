page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.GLSTMCell


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/rnn/python/ops/rnn_cell.py#L2248-L2465">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GLSTMCell`

Group LSTM cell (G-LSTM).

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)

<!-- Placeholder for "Used in" -->

The implementation is based on:

  https://arxiv.org/abs/1703.10722

O. Kuchaiev and B. Ginsburg
"Factorization Tricks for LSTM Networks", ICLR 2017 workshop.

In brief, a G-LSTM cell consists of one LSTM sub-cell per group, where each
sub-cell operates on an evenly-sized sub-vector of the input and produces an
evenly-sized sub-vector of the output.  For example, a G-LSTM cell with 128
units and 4 groups consists of 4 LSTMs sub-cells with 32 units each.  If that
G-LSTM cell is fed a 200-dim input, then each sub-cell receives a 50-dim part
of the input and produces a 32-dim part of the output.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/rnn/python/ops/rnn_cell.py#L2266-L2326">View source</a>

``` python
__init__(
    num_units,
    initializer=None,
    num_proj=None,
    number_of_groups=1,
    forget_bias=1.0,
    activation=tf.math.tanh,
    reuse=None
)
```

Initialize the parameters of G-LSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the G-LSTM cell
* <b>`initializer`</b>: (optional) The initializer to use for the weight and
  projection matrices.
* <b>`num_proj`</b>: (optional) int, The output dimensionality for the projection
  matrices.  If None, no projection is performed.
* <b>`number_of_groups`</b>: (optional) int, number of groups to use.
  If `number_of_groups` is 1, then it should be equivalent to LSTM cell
* <b>`forget_bias`</b>: Biases of the forget gate are initialized by default to 1
  in order to reduce the scale of forgetting at the beginning of
  the training.
* <b>`activation`</b>: Activation function of the inner states.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already
  has the given variables, an error is raised.


#### Raises:


* <b>`ValueError`</b>: If `num_units` or `num_proj` is not divisible by
  `number_of_groups`.



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>

Integer or TensorShape: size of outputs produced by this cell.


<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>

size(s) of state(s) used by this cell.

It can be represented by an Integer, a TensorShape or a tuple of Integers
or TensorShapes.



## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/rnn_cell_impl.py#L281-L309">View source</a>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="zero_state"><code>zero_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/rnn_cell_impl.py#L311-L340">View source</a>

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
