page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.GridLSTMCell

## Class `GridLSTMCell`

Grid Long short-term memory unit (LSTM) recurrent network cell.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)



Defined in [`contrib/rnn/python/ops/rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/rnn_cell.py).

<!-- Placeholder for "Used in" -->

The default is based on:
  Nal Kalchbrenner, Ivo Danihelka and Alex Graves
  "Grid Long Short-Term Memory," Proc. ICLR 2016.
  http://arxiv.org/abs/1507.01526

When peephole connections are used, the implementation is based on:
  Tara N. Sainath and Bo Li
  "Modeling Time-Frequency Patterns with LSTM vs. Convolutional Architectures
  for LVCSR Tasks." submitted to INTERSPEECH, 2016.

The code uses optional peephole connections, shared_weights and cell clipping.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    use_peepholes=False,
    share_time_frequency_weights=False,
    cell_clip=None,
    initializer=None,
    num_unit_shards=1,
    forget_bias=1.0,
    feature_size=None,
    frequency_skip=None,
    num_frequency_blocks=None,
    start_freqindex_list=None,
    end_freqindex_list=None,
    couple_input_forget_gates=False,
    state_is_tuple=True,
    reuse=None
)
```

Initialize the parameters for an LSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell
* <b>`use_peepholes`</b>: (optional) bool, default False. Set True to enable
  diagonal/peephole connections.
* <b>`share_time_frequency_weights`</b>: (optional) bool, default False. Set True to
  enable shared cell weights between time and frequency LSTMs.
* <b>`cell_clip`</b>: (optional) A float value, default None, if provided the cell
  state is clipped by this value prior to the cell output activation.
* <b>`initializer`</b>: (optional) The initializer to use for the weight and
  projection matrices, default None.
* <b>`num_unit_shards`</b>: (optional) int, default 1, How to split the weight
  matrix. If > 1, the weight matrix is stored across num_unit_shards.
* <b>`forget_bias`</b>: (optional) float, default 1.0, The initial bias of the
  forget gates, used to reduce the scale of forgetting at the beginning
  of the training.
* <b>`feature_size`</b>: (optional) int, default None, The size of the input feature
  the LSTM spans over.
* <b>`frequency_skip`</b>: (optional) int, default None, The amount the LSTM filter
  is shifted by in frequency.
* <b>`num_frequency_blocks`</b>: [required] A list of frequency blocks needed to
  cover the whole input feature splitting defined by start_freqindex_list
  and end_freqindex_list.
* <b>`start_freqindex_list`</b>: [optional], list of ints, default None,  The
  starting frequency index for each frequency block.
* <b>`end_freqindex_list`</b>: [optional], list of ints, default None. The ending
  frequency index for each frequency block.
* <b>`couple_input_forget_gates`</b>: (optional) bool, default False, Whether to
  couple the input and forget gates, i.e. f_gate = 1.0 - i_gate, to reduce
  model parameters and computation cost.
* <b>`state_is_tuple`</b>: If True, accepted and returned states are 2-tuples of
  the `c_state` and `m_state`.  By default (False), they are concatenated
  along the column axis.  This default behavior will soon be deprecated.
* <b>`reuse`</b>: (optional) Python boolean describing whether to reuse variables
  in an existing scope.  If not `True`, and the existing scope already has
  the given variables, an error is raised.

#### Raises:


* <b>`ValueError`</b>: if the num_frequency_blocks list is not specified



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="output_size"><code>output_size</code></h3>




<h3 id="scope_name"><code>scope_name</code></h3>




<h3 id="state_size"><code>state_size</code></h3>




<h3 id="state_tuple_type"><code>state_tuple_type</code></h3>






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




