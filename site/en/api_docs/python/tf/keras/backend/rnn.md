description: Iterates over the time dimension of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.rnn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.rnn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L3873-L4264">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Iterates over the time dimension of a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.rnn`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.rnn(
    step_function, inputs, initial_states, go_backwards=(False), mask=None,
    constants=None, unroll=(False), input_length=None, time_major=(False),
    zero_output_for_mask=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`step_function`
</td>
<td>
RNN step function.
Args;
input; Tensor with shape `(samples, ...)` (no time dimension),
representing input for the batch of samples at a certain
time step.
states; List of tensors.
Returns;
output; Tensor with shape `(samples, output_dim)`
(no time dimension).
new_states; List of tensors, same length and shapes
as 'states'. The first state in the list must be the
output tensor at the previous timestep.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
Tensor of temporal data of shape `(samples, time, ...)`
(at least 3D), or nested tensors, and each of which has shape
`(samples, time, ...)`.
</td>
</tr><tr>
<td>
`initial_states`
</td>
<td>
Tensor with shape `(samples, state_size)`
(no time dimension), containing the initial values for the states used
in the step function. In the case that state_size is in a nested
shape, the shape of initial_states will also follow the nested
structure.
</td>
</tr><tr>
<td>
`go_backwards`
</td>
<td>
Boolean. If True, do the iteration over the time
dimension in reverse order and return the reversed sequence.
</td>
</tr><tr>
<td>
`mask`
</td>
<td>
Binary tensor with shape `(samples, time, 1)`,
with a zero for every element that is masked.
</td>
</tr><tr>
<td>
`constants`
</td>
<td>
List of constant values passed at each step.
</td>
</tr><tr>
<td>
`unroll`
</td>
<td>
Whether to unroll the RNN or to use a symbolic `while_loop`.
</td>
</tr><tr>
<td>
`input_length`
</td>
<td>
An integer or a 1-D Tensor, depending on whether
the time dimension is fixed-length or not. In case of variable length
input, it is used for masking in case there's no mask specified.
</td>
</tr><tr>
<td>
`time_major`
</td>
<td>
Boolean. If true, the inputs and outputs will be in shape
`(timesteps, batch, ...)`, whereas in the False case, it will be
`(batch, timesteps, ...)`. Using `time_major = True` is a bit more
efficient because it avoids transposes at the beginning and end of the
RNN calculation. However, most TensorFlow data is batch-major, so by
default this function accepts input and emits output in batch-major
form.
</td>
</tr><tr>
<td>
`zero_output_for_mask`
</td>
<td>
Boolean. If True, the output for masked timestep
will be zeros, whereas in the False case, output from previous
timestep is returned.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple, `(last_output, outputs, new_states)`.
last_output: the latest output of the rnn, of shape `(samples, ...)`
outputs: tensor with shape `(samples, time, ...)` where each
entry `outputs[s, t]` is the output of the step function
at time `t` for sample `s`.
new_states: list of tensors, latest states returned by
the step function, of shape `(samples, ...)`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if input dimension is less than 3.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `unroll` is `True` but input timestep is not a fixed
number.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `mask` is provided (not `None`) but states is not provided
(`len(states)` == 0).
</td>
</tr>
</table>

