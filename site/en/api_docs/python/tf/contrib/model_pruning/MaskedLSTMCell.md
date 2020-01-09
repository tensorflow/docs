page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.MaskedLSTMCell


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/layers/rnn_cells.py#L172-L348">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MaskedLSTMCell`

LSTMCell with pruning.

Inherits From: [`LSTMCell`](../../../tf/nn/rnn_cell/LSTMCell)

<!-- Placeholder for "Used in" -->

Overrides the call method of tensorflow LSTMCell and injects the weight masks.
Masks are applied to only the weight matrix of the LSTM and not the
projection matrix.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/model_pruning/python/layers/rnn_cells.py#L180-L238">View source</a>

``` python
__init__(
    num_units,
    use_peepholes=False,
    cell_clip=None,
    initializer=None,
    num_proj=None,
    proj_clip=None,
    num_unit_shards=None,
    num_proj_shards=None,
    forget_bias=1.0,
    state_is_tuple=True,
    activation=None,
    reuse=None
)
```

Initialize the parameters for an LSTM cell with masks for pruning.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell
* <b>`use_peepholes`</b>: bool, set True to enable diagonal/peephole connections.
* <b>`cell_clip`</b>: (optional) A float value, if provided the cell state is clipped
  by this value prior to the cell output activation.
* <b>`initializer`</b>: (optional) The initializer to use for the weight and
  projection matrices.
* <b>`num_proj`</b>: (optional) int, The output dimensionality for the projection
  matrices.  If None, no projection is performed.
* <b>`proj_clip`</b>: (optional) A float value.  If `num_proj > 0` and `proj_clip` is
  provided, then the projected values are clipped elementwise to within
  `[-proj_clip, proj_clip]`.
* <b>`num_unit_shards`</b>: Deprecated, will be removed by Jan. 2017.
  Use a variable_scope partitioner instead.
* <b>`num_proj_shards`</b>: Deprecated, will be removed by Jan. 2017.
  Use a variable_scope partitioner instead.
* <b>`forget_bias`</b>: Biases of the forget gate are initialized by default to 1
  in order to reduce the scale of forgetting at the beginning of
  the training. Must set it manually to `0.0` when restoring from
  CudnnLSTM trained checkpoints.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are 2-tuples of
  the `c_state` and `m_state`.  If False, they are concatenated
  along the column axis.  This latter behavior will soon be deprecated.
* <b>`activation`</b>: Activation function of the inner states.  Default: `tanh`.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.

When restoring from CudnnLSTM-trained checkpoints, must use
CudnnCompatibleLSTMCell instead.



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
