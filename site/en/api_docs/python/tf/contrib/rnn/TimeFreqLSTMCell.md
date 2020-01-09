page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.TimeFreqLSTMCell


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/rnn/python/ops/rnn_cell.py#L325-L496">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TimeFreqLSTMCell`

Time-Frequency Long short-term memory unit (LSTM) recurrent network cell.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)

<!-- Placeholder for "Used in" -->

This implementation is based on:

  Tara N. Sainath and Bo Li
  "Modeling Time-Frequency Patterns with LSTM vs. Convolutional Architectures
  for LVCSR Tasks." submitted to INTERSPEECH, 2016.

It uses peep-hole connections and optional cell clipping.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/rnn/python/ops/rnn_cell.py#L337-L379">View source</a>

``` python
__init__(
    num_units,
    use_peepholes=False,
    cell_clip=None,
    initializer=None,
    num_unit_shards=1,
    forget_bias=1.0,
    feature_size=None,
    frequency_skip=1,
    reuse=None
)
```

Initialize the parameters for an LSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell
* <b>`use_peepholes`</b>: bool, set True to enable diagonal/peephole connections.
* <b>`cell_clip`</b>: (optional) A float value, if provided the cell state is clipped
  by this value prior to the cell output activation.
* <b>`initializer`</b>: (optional) The initializer to use for the weight and
  projection matrices.
* <b>`num_unit_shards`</b>: int, How to split the weight matrix.  If >1, the weight
  matrix is stored across num_unit_shards.
* <b>`forget_bias`</b>: float, Biases of the forget gate are initialized by default
  to 1 in order to reduce the scale of forgetting at the beginning
  of the training.
* <b>`feature_size`</b>: int, The size of the input feature the LSTM spans over.
* <b>`frequency_skip`</b>: int, The amount the LSTM filter is shifted by in
  frequency.
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
