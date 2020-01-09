page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.AttentionWrapper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py#L2137-L2538">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `AttentionWrapper`

Wraps another `RNNCell` with attention.

Inherits From: [`RNNCell`](../../../tf/nn/rnn_cell/RNNCell)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py#L2140-L2335">View source</a>

``` python
__init__(
    cell,
    attention_mechanism,
    attention_layer_size=None,
    alignment_history=False,
    cell_input_fn=None,
    output_attention=True,
    initial_cell_state=None,
    name=None,
    attention_layer=None,
    attention_fn=None,
    dtype=None
)
```

Construct the `AttentionWrapper`.

**NOTE** If you are using the `BeamSearchDecoder` with a cell wrapped in
`AttentionWrapper`, then you must ensure that:

- The encoder output has been tiled to `beam_width` via
  <a href="../../../tf/contrib/seq2seq/tile_batch"><code>tf.contrib.seq2seq.tile_batch</code></a> (NOT <a href="../../../tf/tile"><code>tf.tile</code></a>).
- The `batch_size` argument passed to the `zero_state` method of this
  wrapper is equal to `true_batch_size * beam_width`.
- The initial state created with `zero_state` above contains a
  `cell_state` value containing properly tiled final state from the
  encoder.

#### An example:



```
tiled_encoder_outputs = tf.contrib.seq2seq.tile_batch(
    encoder_outputs, multiplier=beam_width)
tiled_encoder_final_state = tf.conrib.seq2seq.tile_batch(
    encoder_final_state, multiplier=beam_width)
tiled_sequence_length = tf.contrib.seq2seq.tile_batch(
    sequence_length, multiplier=beam_width)
attention_mechanism = MyFavoriteAttentionMechanism(
    num_units=attention_depth,
    memory=tiled_inputs,
    memory_sequence_length=tiled_sequence_length)
attention_cell = AttentionWrapper(cell, attention_mechanism, ...)
decoder_initial_state = attention_cell.zero_state(
    dtype, batch_size=true_batch_size * beam_width)
decoder_initial_state = decoder_initial_state.clone(
    cell_state=tiled_encoder_final_state)
```

#### Args:


* <b>`cell`</b>: An instance of `RNNCell`.
* <b>`attention_mechanism`</b>: A list of `AttentionMechanism` instances or a single
  instance.
* <b>`attention_layer_size`</b>: A list of Python integers or a single Python
  integer, the depth of the attention (output) layer(s). If None
  (default), use the context as attention at each time step. Otherwise,
  feed the context and cell output into the attention layer to generate
  attention at each time step. If attention_mechanism is a list,
  attention_layer_size must be a list of the same length. If
  attention_layer is set, this must be None. If attention_fn is set, it
  must guaranteed that the outputs of attention_fn also meet the above
  requirements.
* <b>`alignment_history`</b>: Python boolean, whether to store alignment history from
  all time steps in the final output state (currently stored as a time
  major `TensorArray` on which you must call `stack()`).
* <b>`cell_input_fn`</b>: (optional) A `callable`.  The default is:
  `lambda inputs, attention: array_ops.concat([inputs, attention], -1)`.
* <b>`output_attention`</b>: Python bool.  If `True` (default), the output at each
  time step is the attention value.  This is the behavior of Luong-style
  attention mechanisms.  If `False`, the output at each time step is the
  output of `cell`.  This is the behavior of Bhadanau-style attention
  mechanisms.  In both cases, the `attention` tensor is propagated to the
  next time step via the state and is used there. This flag only controls
  whether the attention mechanism is propagated up to the next cell in an
  RNN stack or to the top RNN output.
* <b>`initial_cell_state`</b>: The initial state value to use for the cell when the
  user calls `zero_state()`.  Note that if this value is provided now, and
  the user uses a `batch_size` argument of `zero_state` which does not
  match the batch size of `initial_cell_state`, proper behavior is not
  guaranteed.
* <b>`name`</b>: Name to use when creating ops.
* <b>`attention_layer`</b>: A list of <a href="../../../tf/layers/Layer"><code>tf.compat.v1.layers.Layer</code></a> instances or a
  single <a href="../../../tf/layers/Layer"><code>tf.compat.v1.layers.Layer</code></a> instance taking the context and cell
  output as inputs to generate attention at each time step. If None
  (default), use the context as attention at each time step. If
  attention_mechanism is a list, attention_layer must be a list of the
  same length. If attention_layers_size is set, this must be None.
* <b>`attention_fn`</b>: An optional callable function that allows users to provide
  their own customized attention function, which takes input
  (attention_mechanism, cell_output, attention_state, attention_layer) and
  outputs (attention, alignments, next_attention_state). If provided, the
  attention_layer_size should be the size of the outputs of attention_fn.
* <b>`dtype`</b>: The cell dtype


#### Raises:


* <b>`TypeError`</b>: `attention_layer_size` is not None and (`attention_mechanism`
  is a list but `attention_layer_size` is not; or vice versa).
* <b>`ValueError`</b>: if `attention_layer_size` is not None, `attention_mechanism`
  is a list, and its length does not match that of `attention_layer_size`;
  if `attention_layer_size` and `attention_layer` are set simultaneously.



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

The `state_size` property of `AttentionWrapper`.


#### Returns:

An `AttentionWrapperState` tuple containing shapes used by this object.




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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py#L2389-L2447">View source</a>

``` python
zero_state(
    batch_size,
    dtype
)
```

Return an initial (zero) state tuple for this `AttentionWrapper`.

**NOTE** Please see the initializer documentation for details of how
to call `zero_state` if using an `AttentionWrapper` with a
`BeamSearchDecoder`.

#### Args:


* <b>`batch_size`</b>: `0D` integer tensor: the batch size.
* <b>`dtype`</b>: The internal state data type.


#### Returns:

An `AttentionWrapperState` tuple containing zeroed out tensors and,
possibly, empty `TensorArray` objects.



#### Raises:


* <b>`ValueError`</b>: (or, possibly at runtime, InvalidArgument), if
  `batch_size` does not match the output size of the encoder passed
  to the wrapper object at initialization time.
