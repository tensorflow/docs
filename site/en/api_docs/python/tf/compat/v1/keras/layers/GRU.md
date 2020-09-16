description: Gated Recurrent Unit - Cho et al. 2014.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.layers.GRU" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
</div>

# tf.compat.v1.keras.layers.GRU

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L1914-L2194">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Gated Recurrent Unit - Cho et al. 2014.

Inherits From: [`RNN`](../../../../../tf/keras/layers/RNN.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.layers.GRU(
    units, activation='tanh', recurrent_activation='hard_sigmoid', use_bias=(True),
    kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal',
    bias_initializer='zeros', kernel_regularizer=None, recurrent_regularizer=None,
    bias_regularizer=None, activity_regularizer=None, kernel_constraint=None,
    recurrent_constraint=None, bias_constraint=None, dropout=0.0,
    recurrent_dropout=0.0, implementation=1, return_sequences=(False),
    return_state=(False), go_backwards=(False), stateful=(False), unroll=(False),
    reset_after=(False), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

There are two variants. The default one is based on 1406.1078v3 and
has reset gate applied to hidden state before matrix multiplication. The
other one is based on original 1406.1078v1 and has the order reversed.

The second variant is compatible with CuDNNGRU (GPU-only) and allows
inference on CPU. Thus it has separate biases for `kernel` and
`recurrent_kernel`. Use `'reset_after'=True` and
`recurrent_activation='sigmoid'`.

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
`recurrent_activation`
</td>
<td>
Activation function to use
for the recurrent step.
Default: hard sigmoid (`hard_sigmoid`).
If you pass `None`, no activation is applied
(ie. "linear" activation: `a(x) = x`).
</td>
</tr><tr>
<td>
`use_bias`
</td>
<td>
Boolean, whether the layer uses a bias vector.
</td>
</tr><tr>
<td>
`kernel_initializer`
</td>
<td>
Initializer for the `kernel` weights matrix,
used for the linear transformation of the inputs.
</td>
</tr><tr>
<td>
`recurrent_initializer`
</td>
<td>
Initializer for the `recurrent_kernel`
weights matrix, used for the linear transformation of the recurrent state.
</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>
Initializer for the bias vector.
</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>
Regularizer function applied to
the `kernel` weights matrix.
</td>
</tr><tr>
<td>
`recurrent_regularizer`
</td>
<td>
Regularizer function applied to
the `recurrent_kernel` weights matrix.
</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>
Regularizer function applied to the bias vector.
</td>
</tr><tr>
<td>
`activity_regularizer`
</td>
<td>
Regularizer function applied to
the output of the layer (its "activation")..
</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>
Constraint function applied to
the `kernel` weights matrix.
</td>
</tr><tr>
<td>
`recurrent_constraint`
</td>
<td>
Constraint function applied to
the `recurrent_kernel` weights matrix.
</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>
Constraint function applied to the bias vector.
</td>
</tr><tr>
<td>
`dropout`
</td>
<td>
Float between 0 and 1.
Fraction of the units to drop for
the linear transformation of the inputs.
</td>
</tr><tr>
<td>
`recurrent_dropout`
</td>
<td>
Float between 0 and 1.
Fraction of the units to drop for
the linear transformation of the recurrent state.
</td>
</tr><tr>
<td>
`implementation`
</td>
<td>
Implementation mode, either 1 or 2.
Mode 1 will structure its operations as a larger number of
smaller dot products and additions, whereas mode 2 will
batch them into fewer, larger operations. These modes will
have different performance profiles on different hardware and
for different applications.
</td>
</tr><tr>
<td>
`return_sequences`
</td>
<td>
Boolean. Whether to return the last output
in the output sequence, or the full sequence.
</td>
</tr><tr>
<td>
`return_state`
</td>
<td>
Boolean. Whether to return the last state
in addition to the output.
</td>
</tr><tr>
<td>
`go_backwards`
</td>
<td>
Boolean (default False).
If True, process the input sequence backwards and return the
reversed sequence.
</td>
</tr><tr>
<td>
`stateful`
</td>
<td>
Boolean (default False). If True, the last state
for each sample at index i in a batch will be used as initial
state for the sample of index i in the following batch.
</td>
</tr><tr>
<td>
`unroll`
</td>
<td>
Boolean (default False).
If True, the network will be unrolled,
else a symbolic loop will be used.
Unrolling can speed-up a RNN,
although it tends to be more memory-intensive.
Unrolling is only suitable for short sequences.
</td>
</tr><tr>
<td>
`time_major`
</td>
<td>
The shape format of the `inputs` and `outputs` tensors.
If True, the inputs and outputs will be in shape
`(timesteps, batch, ...)`, whereas in the False case, it will be
`(batch, timesteps, ...)`. Using `time_major = True` is a bit more
efficient because it avoids transposes at the beginning and end of the
RNN calculation. However, most TensorFlow data is batch-major, so by
default this function accepts input and emits output in batch-major
form.
</td>
</tr><tr>
<td>
`reset_after`
</td>
<td>
GRU convention (whether to apply reset gate after or
before matrix multiplication). False = "before" (default),
True = "after" (CuDNN compatible).
</td>
</tr>
</table>



#### Call arguments:


* <b>`inputs`</b>: A 3D tensor.
* <b>`mask`</b>: Binary tensor of shape `(samples, timesteps)` indicating whether
  a given timestep should be masked.
* <b>`training`</b>: Python boolean indicating whether the layer should behave in
  training mode or in inference mode. This argument is passed to the cell
  when calling it. This is only relevant if `dropout` or
  `recurrent_dropout` is used.
* <b>`initial_state`</b>: List of initial state tensors to be passed to the first
  call of the cell.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`activation`
</td>
<td>

</td>
</tr><tr>
<td>
`bias_constraint`
</td>
<td>

</td>
</tr><tr>
<td>
`bias_initializer`
</td>
<td>

</td>
</tr><tr>
<td>
`bias_regularizer`
</td>
<td>

</td>
</tr><tr>
<td>
`dropout`
</td>
<td>

</td>
</tr><tr>
<td>
`implementation`
</td>
<td>

</td>
</tr><tr>
<td>
`kernel_constraint`
</td>
<td>

</td>
</tr><tr>
<td>
`kernel_initializer`
</td>
<td>

</td>
</tr><tr>
<td>
`kernel_regularizer`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_activation`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_constraint`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_dropout`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_initializer`
</td>
<td>

</td>
</tr><tr>
<td>
`recurrent_regularizer`
</td>
<td>

</td>
</tr><tr>
<td>
`reset_after`
</td>
<td>

</td>
</tr><tr>
<td>
`states`
</td>
<td>

</td>
</tr><tr>
<td>
`units`
</td>
<td>

</td>
</tr><tr>
<td>
`use_bias`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L875-L943">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states(
    states=None
)
</code></pre>

Reset the recorded states for the stateful RNN layer.

Can only be used when RNN layer is constructed with `stateful` = `True`.
Args:
  states: Numpy arrays that contains the value for the initial state, which
    will be feed to cell at the first time step. When the value is None,
    zero filled numpy array will be created based on the cell state size.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AttributeError`
</td>
<td>
When the RNN layer is not stateful.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
When the batch size of the RNN layer is unknown.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
When the input numpy array is not compatible with the RNN
layer state, either size wise or dtype wise.
</td>
</tr>
</table>





