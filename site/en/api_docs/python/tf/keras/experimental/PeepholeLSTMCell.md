page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.experimental.PeepholeLSTMCell


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/recurrent.py#L2318-L2392">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `PeepholeLSTMCell`

Equivalent to LSTMCell class but adds peephole connections.

Inherits From: [`LSTMCell`](../../../tf/compat/v1/keras/layers/LSTMCell)

### Aliases:

* Class `tf.compat.v1.keras.experimental.PeepholeLSTMCell`
* Class `tf.compat.v2.keras.experimental.PeepholeLSTMCell`


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

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/recurrent.py#L2100-L2148">View source</a>

``` python
__init__(
    units,
    activation='tanh',
    recurrent_activation='hard_sigmoid',
    use_bias=True,
    kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal',
    bias_initializer='zeros',
    unit_forget_bias=True,
    kernel_regularizer=None,
    recurrent_regularizer=None,
    bias_regularizer=None,
    kernel_constraint=None,
    recurrent_constraint=None,
    bias_constraint=None,
    dropout=0.0,
    recurrent_dropout=0.0,
    implementation=1,
    **kwargs
)
```






## Methods

<h3 id="get_dropout_mask_for_cell"><code>get_dropout_mask_for_cell</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/recurrent.py#L1033-L1067">View source</a>

``` python
get_dropout_mask_for_cell(
    inputs,
    training,
    count=1
)
```

Get the dropout mask for RNN cell's input.

It will create mask based on context if there isn't any existing cached
mask. If a new mask is generated, it will update the cache in the cell.

#### Args:


* <b>`inputs`</b>: the input tensor whose shape will be used to generate dropout
  mask.
* <b>`training`</b>: boolean tensor, whether its in training mode, dropout will be
  ignored in non-training mode.
* <b>`count`</b>: int, how many dropout mask will be generated. It is useful for cell
  that has internal weights fused together.

#### Returns:

List of mask tensor, generated or cached mask based on context.


<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/recurrent.py#L2312-L2314">View source</a>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="get_recurrent_dropout_mask_for_cell"><code>get_recurrent_dropout_mask_for_cell</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/recurrent.py#L1069-L1105">View source</a>

``` python
get_recurrent_dropout_mask_for_cell(
    inputs,
    training,
    count=1
)
```

Get the recurrent dropout mask for RNN cell.

It will create mask based on context if there isn't any existing cached
mask. If a new mask is generated, it will update the cache in the cell.

#### Args:


* <b>`inputs`</b>: the input tensor whose shape will be used to generate dropout
  mask.
* <b>`training`</b>: boolean tensor, whether its in training mode, dropout will be
  ignored in non-training mode.
* <b>`count`</b>: int, how many dropout mask will be generated. It is useful for cell
  that has internal weights fused together.

#### Returns:

List of mask tensor, generated or cached mask based on context.


<h3 id="reset_dropout_mask"><code>reset_dropout_mask</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/recurrent.py#L1009-L1019">View source</a>

``` python
reset_dropout_mask()
```

Reset the cached dropout masks if any.

This is important for the RNN layer to invoke this in it call() method so
that the cached mask is cleared before calling the cell.call(). The mask
should be cached across the timestep within the same batch, but shouldn't
be cached between batches. Otherwise it will introduce unreasonable bias
against certain index of data within the batch.

<h3 id="reset_recurrent_dropout_mask"><code>reset_recurrent_dropout_mask</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/layers/recurrent.py#L1021-L1031">View source</a>

``` python
reset_recurrent_dropout_mask()
```

Reset the cached recurrent dropout masks if any.

This is important for the RNN layer to invoke this in it call() method so
that the cached mask is cleared before calling the cell.call(). The mask
should be cached across the timestep within the same batch, but shouldn't
be cached between batches. Otherwise it will introduce unreasonable bias
against certain index of data within the batch.
