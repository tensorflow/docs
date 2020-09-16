description: Operator adding dropout to inputs and outputs of the given cell.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.RNNCellDropoutWrapper" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="get_initial_state"/>
<meta itemprop="property" content="zero_state"/>
</div>

# tf.nn.RNNCellDropoutWrapper

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py#L93-L104">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Operator adding dropout to inputs and outputs of the given cell.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.RNNCellDropoutWrapper(
    *args, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cell`
</td>
<td>
an RNNCell, a projection to output_size is added to it.
</td>
</tr><tr>
<td>
`input_keep_prob`
</td>
<td>
unit Tensor or float between 0 and 1, input keep
probability; if it is constant and 1, no input dropout will be added.
</td>
</tr><tr>
<td>
`output_keep_prob`
</td>
<td>
unit Tensor or float between 0 and 1, output keep
probability; if it is constant and 1, no output dropout will be added.
</td>
</tr><tr>
<td>
`state_keep_prob`
</td>
<td>
unit Tensor or float between 0 and 1, output keep
probability; if it is constant and 1, no output dropout will be added.
State dropout is performed on the outgoing states of the cell. **Note**
the state components to which dropout is applied when `state_keep_prob`
is in `(0, 1)` are also determined by the argument
`dropout_state_filter_visitor` (e.g. by default dropout is never applied
to the `c` component of an `LSTMStateTuple`).
</td>
</tr><tr>
<td>
`variational_recurrent`
</td>
<td>
Python bool.  If `True`, then the same dropout
pattern is applied across all time steps per run call. If this parameter
is set, `input_size` **must** be provided.
</td>
</tr><tr>
<td>
`input_size`
</td>
<td>
(optional) (possibly nested tuple of) `TensorShape` objects
containing the depth(s) of the input tensors expected to be passed in to
the `DropoutWrapper`.  Required and used **iff** `variational_recurrent
= True` and `input_keep_prob < 1`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(optional) The `dtype` of the input, state, and output tensors.
Required and used **iff** `variational_recurrent = True`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
(optional) integer, the randomness seed.
</td>
</tr><tr>
<td>
`dropout_state_filter_visitor`
</td>
<td>
(optional), default: (see below).  Function
that takes any hierarchical level of the state and returns a scalar or
depth=1 structure of Python booleans describing which terms in the state
should be dropped out.  In addition, if the function returns `True`,
dropout is applied across this sublevel.  If the function returns
`False`, dropout is not applied across this entire sublevel.
Default behavior: perform dropout on all terms except the memory (`c`)
state of `LSTMCellState` objects, and don't try to apply dropout to
`TensorArray` objects: ```
def dropout_state_filter_visitor(s):
if isinstance(s, LSTMCellState): # Never perform dropout on the c
state. return LSTMCellState(c=False, h=True)
elif isinstance(s, TensorArray): return False return True ```
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
dict of keyword arguments for base layer.
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
if `cell` is not an `RNNCell`, or `keep_state_fn` is provided
but not `callable`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if any of the keep_probs are not between 0 and 1.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`output_size`
</td>
<td>

</td>
</tr><tr>
<td>
`state_size`
</td>
<td>

</td>
</tr><tr>
<td>
`wrapped_cell`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/recurrent.py#L1068-L1069">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_initial_state(
    inputs=None, batch_size=None, dtype=None
)
</code></pre>




<h3 id="zero_state"><code>zero_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/rnn_cell_wrapper_impl.py#L201-L203">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>zero_state(
    batch_size, dtype
)
</code></pre>






