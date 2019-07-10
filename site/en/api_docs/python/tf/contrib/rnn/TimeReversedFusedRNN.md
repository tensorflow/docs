page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.TimeReversedFusedRNN

## Class `TimeReversedFusedRNN`

Inherits From: [`FusedRNNCell`](../../../tf/contrib/rnn/FusedRNNCell)



Defined in [`tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py).

This is an adaptor to time-reverse a FusedRNNCell.

For example,

```python
cell = tf.contrib.rnn.BasicRNNCell(10)
fw_lstm = tf.contrib.rnn.FusedRNNCellAdaptor(cell, use_dynamic_rnn=True)
bw_lstm = tf.contrib.rnn.TimeReversedFusedRNN(fw_lstm)
fw_out, fw_state = fw_lstm(inputs)
bw_out, bw_state = bw_lstm(inputs)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(cell)
```

Initialize self.  See help(type(self)) for accurate signature.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    initial_state=None,
    dtype=None,
    sequence_length=None,
    scope=None
)
```

Run this fused RNN on inputs, starting from the given state.

#### Args:

* <b>`inputs`</b>: `3-D` tensor with shape `[time_len x batch_size x input_size]`
    or a list of `time_len` tensors of shape `[batch_size x input_size]`.
* <b>`initial_state`</b>: either a tensor with shape `[batch_size x state_size]`
    or a tuple with shapes `[batch_size x s] for s in state_size`, if the
    cell takes tuples. If this is not provided, the cell is expected to
    create a zero initial state of type `dtype`.
* <b>`dtype`</b>: The data type for the initial state and expected output. Required
    if `initial_state` is not provided or RNN state has a heterogeneous
      dtype.
* <b>`sequence_length`</b>: Specifies the length of each sequence in inputs. An
    `int32` or `int64` vector (tensor) size `[batch_size]`, values in `[0,
    time_len)`.
    Defaults to `time_len` for each element.
* <b>`scope`</b>: `VariableScope` or `string` for the created subgraph; defaults to
    class name.


#### Returns:

A pair containing:

- Output: A `3-D` tensor of shape `[time_len x batch_size x output_size]`
  or a list of `time_len` tensors of shape `[batch_size x output_size]`,
  to match the type of the `inputs`.
- Final state: Either a single `2-D` tensor, or a tuple of tensors
  matching the arity and shapes of `initial_state`.



