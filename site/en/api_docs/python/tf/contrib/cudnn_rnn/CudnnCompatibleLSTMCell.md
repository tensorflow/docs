page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cudnn_rnn.CudnnCompatibleLSTMCell


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/cudnn_rnn/python/ops/cudnn_rnn_ops.py#L62-L78">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CudnnCompatibleLSTMCell`

Cudnn Compatible LSTMCell.

Inherits From: [`LSTMBlockCell`](../../../tf/contrib/rnn/LSTMBlockCell)

<!-- Placeholder for "Used in" -->

A simple wrapper around <a href="../../../tf/contrib/rnn/LSTMBlockCell"><code>tf.contrib.rnn.LSTMBlockCell</code></a> to use along with
<a href="../../../tf/contrib/cudnn_rnn/CudnnLSTM"><code>tf.contrib.cudnn_rnn.CudnnLSTM</code></a>. The latter's params can be used by
this cell seamlessly.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/cudnn_rnn/python/ops/cudnn_rnn_ops.py#L70-L78">View source</a>

``` python
__init__(
    num_units,
    reuse=None
)
```

Initialize the basic LSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell.
* <b>`forget_bias`</b>: float, The bias added to forget gates (see above).
* <b>`cell_clip`</b>: An optional `float`. Defaults to `-1` (no clipping).
* <b>`use_peephole`</b>: Whether to use peephole connections or not.
* <b>`dtype`</b>: the variable dtype of this layer. Default to tf.float32.
* <b>`reuse`</b>: (optional) boolean describing whether to reuse variables in an
  existing scope.  If not `True`, and the existing scope already has the
  given variables, an error is raised.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will
  share weights, but to avoid mistakes we require reuse=True in such
  cases.  By default this is "lstm_cell", for variable-name compatibility
  with <a href="../../../tf/nn/rnn_cell/LSTMCell"><code>tf.compat.v1.nn.rnn_cell.LSTMCell</code></a>.

When restoring from CudnnLSTM-trained checkpoints, must use
CudnnCompatibleLSTMBlockCell instead.



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
