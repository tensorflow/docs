page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.nn.static_state_saving_rnn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/rnn.py#L1447-L1538">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



RNN that accepts a state saver for time-truncated RNN calculation. (deprecated)

``` python
tf.compat.v1.nn.static_state_saving_rnn(
    cell,
    inputs,
    state_saver,
    state_name,
    sequence_length=None,
    scope=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use `keras.layers.RNN(cell, stateful=True)`, which is equivalent to this API

#### Args:


* <b>`cell`</b>: An instance of `RNNCell`.
* <b>`inputs`</b>: A length T list of inputs, each a `Tensor` of shape `[batch_size,
  input_size]`.
* <b>`state_saver`</b>: A state saver object with methods `state` and `save_state`.
* <b>`state_name`</b>: Python string or tuple of strings.  The name to use with the
  state_saver. If the cell returns tuples of states (i.e., `cell.state_size`
  is a tuple) then `state_name` should be a tuple of strings having the same
  length as `cell.state_size`.  Otherwise it should be a single string.
* <b>`sequence_length`</b>: (optional) An int32/int64 vector size [batch_size]. See the
  documentation for rnn() for more details about sequence_length.
* <b>`scope`</b>: VariableScope for the created subgraph; defaults to "rnn".


#### Returns:

A pair (outputs, state) where:
  outputs is a length T list of outputs (one for each input)
  states is the final state



#### Raises:


* <b>`TypeError`</b>: If `cell` is not an instance of RNNCell.
* <b>`ValueError`</b>: If `inputs` is `None` or an empty list, or if the arity and
 type of `state_name` does not match that of `cell.state_size`.
