page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.nn.RNNCellDropoutWrapper

## Class `RNNCellDropoutWrapper`

Operator adding dropout to inputs and outputs of the given cell.





Defined in [`python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/rnn_cell_impl.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    *args,
    **kwargs
)
```

Create a cell with added input, state, and/or output dropout.

If `variational_recurrent` is set to `True` (**NOT** the default behavior),
then the same dropout mask is applied at every step, as described in:
[A Theoretically Grounded Application of Dropout in Recurrent
Neural Networks. Y. Gal, Z. Ghahramani](https://arxiv.org/abs/1512.05287).

Otherwise a different dropout mask is applied at every time step.

Note, by default (unless a custom `dropout_state_filter` is provided),
the memory state (`c` component of any `LSTMStateTuple`) passing through
a `DropoutWrapper` is never modified.  This behavior is described in the
above article.

#### Args:


* <b>`cell`</b>: an RNNCell, a projection to output_size is added to it.
* <b>`input_keep_prob`</b>: unit Tensor or float between 0 and 1, input keep
  probability; if it is constant and 1, no input dropout will be added.
* <b>`output_keep_prob`</b>: unit Tensor or float between 0 and 1, output keep
  probability; if it is constant and 1, no output dropout will be added.
* <b>`state_keep_prob`</b>: unit Tensor or float between 0 and 1, output keep
  probability; if it is constant and 1, no output dropout will be added.
  State dropout is performed on the outgoing states of the cell. **Note**
  the state components to which dropout is applied when `state_keep_prob`
  is in `(0, 1)` are also determined by the argument
  `dropout_state_filter_visitor` (e.g. by default dropout is never applied
  to the `c` component of an `LSTMStateTuple`).
* <b>`variational_recurrent`</b>: Python bool.  If `True`, then the same dropout
  pattern is applied across all time steps per run call. If this parameter
  is set, `input_size` **must** be provided.
* <b>`input_size`</b>: (optional) (possibly nested tuple of) `TensorShape` objects
  containing the depth(s) of the input tensors expected to be passed in to
  the `DropoutWrapper`.  Required and used **iff** `variational_recurrent
  = True` and `input_keep_prob < 1`.
* <b>`dtype`</b>: (optional) The `dtype` of the input, state, and output tensors.
  Required and used **iff** `variational_recurrent = True`.
* <b>`seed`</b>: (optional) integer, the randomness seed.
* <b>`dropout_state_filter_visitor`</b>: (optional), default: (see below).  Function
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


#### Raises:


* <b>`TypeError`</b>: if `cell` is not an `RNNCell`, or `keep_state_fn` is provided
  but not `callable`.
* <b>`ValueError`</b>: if any of the keep_probs are not between 0 and 1.



## Properties

<h3 id="output_size"><code>output_size</code></h3>




<h3 id="state_size"><code>state_size</code></h3>




<h3 id="wrapped_cell"><code>wrapped_cell</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```




<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```






