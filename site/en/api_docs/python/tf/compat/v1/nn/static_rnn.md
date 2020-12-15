description: Creates a recurrent neural network specified by RNNCell cell. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.static_rnn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.static_rnn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/rnn.py#L1241-L1417">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a recurrent neural network specified by RNNCell `cell`. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.static_rnn(
    cell, inputs, initial_state=None, dtype=None, sequence_length=None, scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use `keras.layers.RNN(cell, unroll=True)`, which is equivalent to this API

The simplest form of RNN network generated is:

```python
  state = cell.zero_state(...)
  outputs = []
  for input_ in inputs:
    output, state = cell(input_, state)
    outputs.append(output)
  return (outputs, state)
```
However, a few other options are available:

An initial state can be provided.
If the sequence_length vector is provided, dynamic calculation is performed.
This method of calculation does not compute the RNN steps past the maximum
sequence length of the minibatch (thus saving computational time),
and properly propagates the state at an example's sequence length
to the final state output.

The dynamic calculation performed is, at time `t` for batch row `b`,

```python
  (output, state)(b, t) =
    (t >= sequence_length(b))
      ? (zeros(cell.output_size), states(b, sequence_length(b) - 1))
      : cell(input(b, t), state(b, t - 1))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cell`
</td>
<td>
An instance of RNNCell.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A length T list of inputs, each a `Tensor` of shape `[batch_size,
input_size]`, or a nested tuple of such elements.
</td>
</tr><tr>
<td>
`initial_state`
</td>
<td>
(optional) An initial state for the RNN. If `cell.state_size`
is an integer, this must be a `Tensor` of appropriate type and shape
`[batch_size, cell.state_size]`. If `cell.state_size` is a tuple, this
should be a tuple of tensors having shapes `[batch_size, s] for s in
cell.state_size`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(optional) The data type for the initial state and expected output.
Required if initial_state is not provided or RNN state has a heterogeneous
dtype.
</td>
</tr><tr>
<td>
`sequence_length`
</td>
<td>
Specifies the length of each sequence in inputs. An int32
or int64 vector (tensor) size `[batch_size]`, values in `[0, T)`.
</td>
</tr><tr>
<td>
`scope`
</td>
<td>
VariableScope for the created subgraph; defaults to "rnn".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A pair (outputs, state) where:

- outputs is a length T list of outputs (one for each input), or a nested
tuple of such elements.
- state is the final state
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `cell` is not an instance of RNNCell.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `inputs` is `None` or an empty list, or if the input depth
(column size) cannot be inferred from inputs via shape inference.
</td>
</tr>
</table>

