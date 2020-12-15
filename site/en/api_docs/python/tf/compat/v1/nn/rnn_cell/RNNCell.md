description: Abstract object representing an RNN cell.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.rnn_cell.RNNCell" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="get_initial_state"/>
<meta itemprop="property" content="zero_state"/>
</div>

# tf.compat.v1.nn.rnn_cell.RNNCell

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py#L186-L347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Abstract object representing an RNN cell.

Inherits From: [`Layer`](../../../../../tf/compat/v1/layers/Layer.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.rnn_cell.RNNCell(
    trainable=(True), name=None, dtype=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Every `RNNCell` must have the properties below and implement `call` with
the signature `(output, next_state) = call(input, state)`.  The optional
third input argument, `scope`, is allowed for backwards compatibility
purposes; but should be left off for new subclasses.

This definition of cell differs from the definition used in the literature.
In the literature, 'cell' refers to an object with a single scalar output.
This definition refers to a horizontal array of such units.

An RNN cell, in the most abstract setting, is anything that has
a state and performs some operation that takes a matrix of inputs.
This operation results in an output matrix with `self.output_size` columns.
If `self.state_size` is an integer, this operation also results in a new
state matrix with `self.state_size` columns.  If `self.state_size` is a
(possibly nested tuple of) TensorShape object(s), then it should return a
matching structure of Tensors having shape `[batch_size].concatenate(s)`
for each `s` in `self.batch_size`.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py#L284-L312">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_initial_state(
    inputs=None, batch_size=None, dtype=None
)
</code></pre>




<h3 id="zero_state"><code>zero_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py#L314-L343">View source</a>

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





