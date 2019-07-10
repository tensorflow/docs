page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.LSTMBlockCell

## Class `LSTMBlockCell`

Basic LSTM recurrent network cell.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell)



Defined in [`contrib/rnn/python/ops/lstm_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/lstm_ops.py).

<!-- Placeholder for "Used in" -->

The implementation is based on: http://arxiv.org/abs/1409.2329.

We add `forget_bias` (default: 1) to the biases of the forget gate in order to
reduce the scale of forgetting in the beginning of the training.

Unlike `rnn_cell_impl.LSTMCell`, this is a monolithic op and should be much
faster.  The weight and bias matrices should be compatible as long as the
variable scope matches.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    forget_bias=1.0,
    cell_clip=None,
    use_peephole=False,
    dtype=None,
    reuse=None,
    name='lstm_cell'
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




