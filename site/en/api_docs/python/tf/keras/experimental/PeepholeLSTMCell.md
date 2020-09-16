description: Equivalent to LSTMCell class but adds peephole connections.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.experimental.PeepholeLSTMCell" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="get_dropout_mask_for_cell"/>
<meta itemprop="property" content="get_initial_state"/>
<meta itemprop="property" content="get_recurrent_dropout_mask_for_cell"/>
<meta itemprop="property" content="reset_dropout_mask"/>
<meta itemprop="property" content="reset_recurrent_dropout_mask"/>
</div>

# tf.keras.experimental.PeepholeLSTMCell

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L2485-L2559">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Equivalent to LSTMCell class but adds peephole connections.

Inherits From: [`LSTMCell`](../../../tf/compat/v1/keras/layers/LSTMCell.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.experimental.PeepholeLSTMCell`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.experimental.PeepholeLSTMCell(
    units, activation='tanh', recurrent_activation='hard_sigmoid', use_bias=(True),
    kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal',
    bias_initializer='zeros', unit_forget_bias=(True), kernel_regularizer=None,
    recurrent_regularizer=None, bias_regularizer=None, kernel_constraint=None,
    recurrent_constraint=None, bias_constraint=None, dropout=0.0,
    recurrent_dropout=0.0, implementation=1, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Peephole connections allow the gates to utilize the previous internal state as
well as the previous hidden state (which is what LSTMCell is limited to).
This allows PeepholeLSTMCell to better learn precise timings over LSTMCell.

From [Gers et al.](http://www.jmlr.org/papers/volume3/gers02a/gers02a.pdf):

"We find that LSTM augmented by 'peephole connections' from its internal
cells to its multiplicative gates can learn the fine distinction between
sequences of spikes spaced either 50 or 49 time steps apart without the help
of any short training exemplars."

The peephole implementation is based on:

[Long short-term memory recurrent neural network architectures for
 large scale acoustic modeling.
](https://research.google.com/pubs/archive/43905.pdf)

#### Example:



```python
# Create 2 PeepholeLSTMCells
peephole_lstm_cells = [PeepholeLSTMCell(size) for size in [128, 256]]
# Create a layer composed sequentially of the peephole LSTM cells.
layer = RNN(peephole_lstm_cells)
input = keras.Input((timesteps, input_dim))
output = layer(input)
```

## Methods

<h3 id="get_dropout_mask_for_cell"><code>get_dropout_mask_for_cell</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L1137-L1156">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_dropout_mask_for_cell(
    inputs, training, count=1
)
</code></pre>

Get the dropout mask for RNN cell's input.

It will create mask based on context if there isn't any existing cached
mask. If a new mask is generated, it will update the cache in the cell.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`inputs`
</td>
<td>
The input tensor whose shape will be used to generate dropout
mask.
</td>
</tr><tr>
<td>
`training`
</td>
<td>
Boolean tensor, whether its in training mode, dropout will be
ignored in non-training mode.
</td>
</tr><tr>
<td>
`count`
</td>
<td>
Int, how many dropout mask will be generated. It is useful for cell
that has internal weights fused together.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
List of mask tensor, generated or cached mask based on context.
</td>
</tr>

</table>



<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L2479-L2481">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_initial_state(
    inputs=None, batch_size=None, dtype=None
)
</code></pre>




<h3 id="get_recurrent_dropout_mask_for_cell"><code>get_recurrent_dropout_mask_for_cell</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L1158-L1177">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_recurrent_dropout_mask_for_cell(
    inputs, training, count=1
)
</code></pre>

Get the recurrent dropout mask for RNN cell.

It will create mask based on context if there isn't any existing cached
mask. If a new mask is generated, it will update the cache in the cell.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`inputs`
</td>
<td>
The input tensor whose shape will be used to generate dropout
mask.
</td>
</tr><tr>
<td>
`training`
</td>
<td>
Boolean tensor, whether its in training mode, dropout will be
ignored in non-training mode.
</td>
</tr><tr>
<td>
`count`
</td>
<td>
Int, how many dropout mask will be generated. It is useful for cell
that has internal weights fused together.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
List of mask tensor, generated or cached mask based on context.
</td>
</tr>

</table>



<h3 id="reset_dropout_mask"><code>reset_dropout_mask</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L1101-L1110">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_dropout_mask()
</code></pre>

Reset the cached dropout masks if any.

This is important for the RNN layer to invoke this in it call() method so
that the cached mask is cleared before calling the cell.call(). The mask
should be cached across the timestep within the same batch, but shouldn't
be cached between batches. Otherwise it will introduce unreasonable bias
against certain index of data within the batch.

<h3 id="reset_recurrent_dropout_mask"><code>reset_recurrent_dropout_mask</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L1112-L1121">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_recurrent_dropout_mask()
</code></pre>

Reset the cached recurrent dropout masks if any.

This is important for the RNN layer to invoke this in it call() method so
that the cached mask is cleared before calling the cell.call(). The mask
should be cached across the timestep within the same batch, but shouldn't
be cached between batches. Otherwise it will introduce unreasonable bias
against certain index of data within the batch.



