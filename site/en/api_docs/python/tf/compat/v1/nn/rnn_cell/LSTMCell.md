description: Long short-term memory unit (LSTM) recurrent network cell.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.rnn_cell.LSTMCell" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="get_initial_state"/>
<meta itemprop="property" content="zero_state"/>
</div>

# tf.compat.v1.nn.rnn_cell.LSTMCell

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py#L809-L1089">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Long short-term memory unit (LSTM) recurrent network cell.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.rnn_cell.LSTMCell(
    num_units, use_peepholes=(False), cell_clip=None, initializer=None,
    num_proj=None, proj_clip=None, num_unit_shards=None, num_proj_shards=None,
    forget_bias=1.0, state_is_tuple=(True), activation=None, reuse=None, name=None,
    dtype=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The default non-peephole implementation is based on (Gers et al., 1999).
The peephole implementation is based on (Sak et al., 2014).

The class uses optional peep-hole connections, optional cell clipping, and
an optional projection layer.

Note that this cell is not optimized for performance. Please use
`tf.contrib.cudnn_rnn.CudnnLSTM` for better performance on GPU, or
`tf.contrib.rnn.LSTMBlockCell` and `tf.contrib.rnn.LSTMBlockFusedCell` for
better performance on CPU.
References:
  Long short-term memory recurrent neural network architectures for large
  scale acoustic modeling:
    [Sak et al., 2014]
    (https://www.isca-speech.org/archive/interspeech_2014/i14_0338.html)
    ([pdf]
    (https://www.isca-speech.org/archive/archive_papers/interspeech_2014/i14_0338.pdf))
  Learning to forget:
    [Gers et al., 1999]
    (http://digital-library.theiet.org/content/conferences/10.1049/cp_19991218)
    ([pdf](https://arxiv.org/pdf/1409.2329.pdf))
  Long Short-Term Memory:
    [Hochreiter et al., 1997]
    (https://www.mitpressjournals.org/doi/abs/10.1162/neco.1997.9.8.1735)
    ([pdf](http://ml.jku.at/publications/older/3504.pdf))

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_units`
</td>
<td>
int, The number of units in the LSTM cell.
</td>
</tr><tr>
<td>
`use_peepholes`
</td>
<td>
bool, set True to enable diagonal/peephole connections.
</td>
</tr><tr>
<td>
`cell_clip`
</td>
<td>
(optional) A float value, if provided the cell state is clipped
by this value prior to the cell output activation.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
(optional) The initializer to use for the weight and
projection matrices.
</td>
</tr><tr>
<td>
`num_proj`
</td>
<td>
(optional) int, The output dimensionality for the projection
matrices.  If None, no projection is performed.
</td>
</tr><tr>
<td>
`proj_clip`
</td>
<td>
(optional) A float value.  If `num_proj > 0` and `proj_clip` is
provided, then the projected values are clipped elementwise to within
`[-proj_clip, proj_clip]`.
</td>
</tr><tr>
<td>
`num_unit_shards`
</td>
<td>
Deprecated, will be removed by Jan. 2017. Use a
variable_scope partitioner instead.
</td>
</tr><tr>
<td>
`num_proj_shards`
</td>
<td>
Deprecated, will be removed by Jan. 2017. Use a
variable_scope partitioner instead.
</td>
</tr><tr>
<td>
`forget_bias`
</td>
<td>
Biases of the forget gate are initialized by default to 1 in
order to reduce the scale of forgetting at the beginning of the
training. Must set it manually to `0.0` when restoring from CudnnLSTM
trained checkpoints.
</td>
</tr><tr>
<td>
`state_is_tuple`
</td>
<td>
If True, accepted and returned states are 2-tuples of the
`c_state` and `m_state`.  If False, they are concatenated along the
column axis.  This latter behavior will soon be deprecated.
</td>
</tr><tr>
<td>
`activation`
</td>
<td>
Activation function of the inner states.  Default: `tanh`. It
could also be string that is within Keras activation function names.
</td>
</tr><tr>
<td>
`reuse`
</td>
<td>
(optional) Python boolean describing whether to reuse variables in
an existing scope.  If not `True`, and the existing scope already has
the given variables, an error is raised.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String, the name of the layer. Layers with the same name will share
weights, but to avoid mistakes we require reuse=True in such cases.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Default dtype of the layer (default of `None` means use the type of
the first input). Required when `build` is called before `call`.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Dict, keyword named properties for common layer attributes, like
`trainable` etc when constructing the cell from configs of get_config().
When restoring from CudnnLSTM-trained checkpoints, use
`CudnnCompatibleLSTMCell` instead.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.
</td>
</tr><tr>
<td>
`output_size`
</td>
<td>
Integer or TensorShape: size of outputs produced by this cell.
</td>
</tr><tr>
<td>
`scope_name`
</td>
<td>

</td>
</tr><tr>
<td>
`state_size`
</td>
<td>
size(s) of state(s) used by this cell.

It can be represented by an Integer, a TensorShape or a tuple of Integers
or TensorShapes.
</td>
</tr>
</table>



## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py#L281-L309">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_initial_state(
    inputs=None, batch_size=None, dtype=None
)
</code></pre>




<h3 id="zero_state"><code>zero_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py#L311-L340">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>zero_state(
    batch_size, dtype
)
</code></pre>

Return zero-filled state tensor(s).


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`batch_size`
</td>
<td>
int, float, or unit Tensor representing the batch size.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
the data type to use for the state.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
If `state_size` is an int or TensorShape, then the return value is a
`N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

If `state_size` is a nested list or tuple, then the return value is
a nested list or tuple (of the same structure) of `2-D` tensors with
the shapes `[batch_size, s]` for each s in `state_size`.
</td>
</tr>

</table>





