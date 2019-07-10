page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.rnn_cell.BasicLSTMCell

## Class `BasicLSTMCell`

DEPRECATED: Please use <a href="../../../tf/nn/rnn_cell/LSTMCell"><code>tf.compat.v1.nn.rnn_cell.LSTMCell</code></a> instead.

Inherits From: [`LayerRNNCell`](../../../tf/contrib/rnn/LayerRNNCell)

### Aliases:

* Class `tf.compat.v1.nn.rnn_cell.BasicLSTMCell`
* Class `tf.contrib.rnn.BasicLSTMCell`
* Class `tf.nn.rnn_cell.BasicLSTMCell`



Defined in [`python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/rnn_cell_impl.py).

<!-- Placeholder for "Used in" -->

Basic LSTM recurrent network cell.

The implementation is based on: http://arxiv.org/abs/1409.2329.

We add forget_bias (default: 1) to the biases of the forget gate in order to
reduce the scale of forgetting in the beginning of the training.

It does not allow cell clipping, a projection layer, and does not
use peep-hole connections: it is the basic baseline.

For advanced models, please use the full <a href="../../../tf/nn/rnn_cell/LSTMCell"><code>tf.compat.v1.nn.rnn_cell.LSTMCell</code></a>
that follows.

Note that this cell is not optimized for performance. Please use
<a href="../../../tf/contrib/cudnn_rnn/CudnnLSTM"><code>tf.contrib.cudnn_rnn.CudnnLSTM</code></a> for better performance on GPU, or
<a href="../../../tf/contrib/rnn/LSTMBlockCell"><code>tf.contrib.rnn.LSTMBlockCell</code></a> and <a href="../../../tf/contrib/rnn/LSTMBlockFusedCell"><code>tf.contrib.rnn.LSTMBlockFusedCell</code></a> for
better performance on CPU.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    forget_bias=1.0,
    state_is_tuple=True,
    activation=None,
    reuse=None,
    name=None,
    dtype=None,
    **kwargs
)
```

Initialize the basic LSTM cell. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This class is equivalent as tf.keras.layers.LSTMCell, and will be replaced by that in Tensorflow 2.0.

#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell.
* <b>`forget_bias`</b>: float, The bias added to forget gates (see above). Must set
  to `0.0` manually when restoring from CudnnLSTM-trained checkpoints.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are 2-tuples of the
  `c_state` and `m_state`.  If False, they are concatenated along the
  column axis.  The latter behavior will soon be deprecated.
* <b>`activation`</b>: Activation function of the inner states.  Default: `tanh`. It
  could also be string that is within Keras activation function names.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables in
  an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will share
  weights, but to avoid mistakes we require reuse=True in such cases.
* <b>`dtype`</b>: Default dtype of the layer (default of `None` means use the type of
  the first input). Required when `build` is called before `call`.
* <b>`**kwargs`</b>: Dict, keyword named properties for common layer attributes, like
  `trainable` etc when constructing the cell from configs of get_config().
  When restoring from CudnnLSTM-trained checkpoints, must use
  `CudnnCompatibleLSTMCell` instead.



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




