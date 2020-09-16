description: Cell class for SimpleRNN.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.SimpleRNNCell" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="get_dropout_mask_for_cell"/>
<meta itemprop="property" content="get_initial_state"/>
<meta itemprop="property" content="get_recurrent_dropout_mask_for_cell"/>
<meta itemprop="property" content="reset_dropout_mask"/>
<meta itemprop="property" content="reset_recurrent_dropout_mask"/>
</div>

# tf.keras.layers.SimpleRNNCell

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L1181-L1378">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Cell class for SimpleRNN.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.SimpleRNNCell`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.SimpleRNNCell(
    units, activation='tanh', use_bias=(True), kernel_initializer='glorot_uniform',
    recurrent_initializer='orthogonal', bias_initializer='zeros',
    kernel_regularizer=None, recurrent_regularizer=None, bias_regularizer=None,
    kernel_constraint=None, recurrent_constraint=None, bias_constraint=None,
    dropout=0.0, recurrent_dropout=0.0, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

See [the Keras RNN API guide](https://www.tensorflow.org/guide/keras/rnn)
for details about the usage of RNN API.

This class processes one step within the whole time sequence input, whereas
`tf.keras.layer.SimpleRNN` processes the whole sequence.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`units`
</td>
<td>
Positive integer, dimensionality of the output space.
</td>
</tr><tr>
<td>
`activation`
</td>
<td>
Activation function to use.
Default: hyperbolic tangent (`tanh`).
If you pass `None`, no activation is applied
(ie. "linear" activation: `a(x) = x`).
</td>
</tr><tr>
<td>
`use_bias`
</td>
<td>
Boolean, (default `True`), whether the layer uses a bias vector.
</td>
</tr><tr>
<td>
`kernel_initializer`
</td>
<td>
Initializer for the `kernel` weights matrix,
used for the linear transformation of the inputs. Default:
`glorot_uniform`.
</td>
</tr><tr>
<td>
`recurrent_initializer`
</td>
<td>
Initializer for the `recurrent_kernel`
weights matrix, used for the linear transformation of the recurrent state.
Default: `orthogonal`.
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
Initializer for the bias vector. Default: `zeros`.
</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>
Regularizer function applied to the `kernel` weights
matrix. Default: `None`.
</td>
</tr><tr>
<td>
`recurrent_regularizer`
</td>
<td>
Regularizer function applied to the
`recurrent_kernel` weights matrix. Default: `None`.
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Regularizer function applied to the bias vector. Default:
`None`.
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Constraint function applied to the `kernel` weights
matrix. Default: `None`.
</td>
</tr><tr>
<td>
`recurrent_constraint`
</td>
<td>
Constraint function applied to the `recurrent_kernel`
weights matrix. Default: `None`.
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
Constraint function applied to the bias vector. Default:
`None`.
</td>
</tr><tr>
<td>
`dropout`
</td>
<td>
Float between 0 and 1. Fraction of the units to drop for the linear
transformation of the inputs. Default: 0.
</td>
</tr><tr>
<td>
`recurrent_dropout`
</td>
<td>
Float between 0 and 1. Fraction of the units to drop for
the linear transformation of the recurrent state. Default: 0.
</td>
</tr>
</table>



#### Call arguments:


* <b>`inputs`</b>: A 2D tensor, with shape of `[batch, feature]`.
* <b>`states`</b>: A 2D tensor with shape of `[batch, units]`, which is the state from
  the previous time step. For timestep 0, the initial state provided by user
  will be feed to cell.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. Only relevant when `dropout` or
  `recurrent_dropout` is used.


#### Examples:



```python
inputs = np.random.random([32, 10, 8]).astype(np.float32)
rnn = tf.keras.layers.RNN(tf.keras.layers.SimpleRNNCell(4))

output = rnn(inputs)  # The output has shape `[32, 4]`.

rnn = tf.keras.layers.RNN(
    tf.keras.layers.SimpleRNNCell(4),
    return_sequences=True,
    return_state=True)

# whole_sequence_output has shape `[32, 10, 4]`.
# final_state has shape `[32, 4]`.
whole_sequence_output, final_state = rnn(inputs)
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L1342-L1343">View source</a>

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



