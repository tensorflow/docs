page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.experimental.nn.TFLiteLSTMCell

## Class `TFLiteLSTMCell`

Long short-term memory unit (LSTM) recurrent network cell.

Inherits From: [`LayerRNNCell`](../../../../tf/contrib/rnn/LayerRNNCell)

### Aliases:

* Class `tf.compat.v1.lite.experimental.nn.TFLiteLSTMCell`
* Class `tf.lite.experimental.nn.TFLiteLSTMCell`



Defined in [`lite/experimental/examples/lstm/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/lite/experimental/examples/lstm/rnn_cell.py).

<!-- Placeholder for "Used in" -->

This is used only for TfLite, it provides hints and it also makes the
variables in the desired for the tflite ops  (transposed and seaparated).

The default non-peephole implementation is based on:

  https://pdfs.semanticscholar.org/1154/0131eae85b2e11d53df7f1360eeb6476e7f4.pdf

Felix Gers, Jurgen Schmidhuber, and Fred Cummins.
"Learning to forget: Continual prediction with LSTM." IET, 850-855, 1999.

The peephole implementation is based on:

  https://research.google.com/pubs/archive/43905.pdf

Hasim Sak, Andrew Senior, and Francoise Beaufays.
"Long short-term memory recurrent neural network architectures for
 large scale acoustic modeling." INTERSPEECH, 2014.

The class uses optional peep-hole connections, optional cell clipping, and
an optional projection layer.

Note that this cell is not optimized for performance. Please use
<a href="../../../../tf/contrib/cudnn_rnn/CudnnLSTM"><code>tf.contrib.cudnn_rnn.CudnnLSTM</code></a> for better performance on GPU, or
<a href="../../../../tf/contrib/rnn/LSTMBlockCell"><code>tf.contrib.rnn.LSTMBlockCell</code></a> and <a href="../../../../tf/contrib/rnn/LSTMBlockFusedCell"><code>tf.contrib.rnn.LSTMBlockFusedCell</code></a> for
better performance on CPU.

<h2 id="__init__"><code>__init__</code></h2>

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
    reuse=None,
    name=None,
    dtype=None
)
```

Initialize the parameters for an LSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell.
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
* <b>`num_unit_shards`</b>: Deprecated, will be removed by Jan. 2017. Use a
  variable_scope partitioner instead.
* <b>`num_proj_shards`</b>: Deprecated, will be removed by Jan. 2017. Use a
  variable_scope partitioner instead.
* <b>`forget_bias`</b>: Biases of the forget gate are initialized by default to 1 in
  order to reduce the scale of forgetting at the beginning of the
  training. Must set it manually to `0.0` when restoring from CudnnLSTM
  trained checkpoints.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are 2-tuples of the
  `c_state` and `m_state`.  If False, they are concatenated along the
  column axis.  This latter behavior will soon be deprecated.
* <b>`activation`</b>: Activation function of the inner states.  Default: `tanh`.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables in
  an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will share
  weights, but to avoid mistakes we require reuse=True in such cases.
* <b>`dtype`</b>: Default dtype of the layer (default of `None` means use the type of
  the first input). Required when `build` is called before `call`.  When
  restoring from CudnnLSTM-trained checkpoints, use
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




