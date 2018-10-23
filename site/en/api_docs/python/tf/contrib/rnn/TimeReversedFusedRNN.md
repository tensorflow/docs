

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.rnn.TimeReversedFusedRNN

## Class `TimeReversedFusedRNN`

Inherits From: [`FusedRNNCell`](../../../tf/contrib/rnn/FusedRNNCell)



Defined in [`tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

This is an adaptor to time-reverse a FusedRNNCell.

For example,

```python
cell = tf.contrib.rnn.BasicRNNCell(10)
fw_lstm = tf.contrib.rnn.FusedRNNCellAdaptor(cell, use_dynamic_rnn=True)
bw_lstm = tf.contrib.rnn.TimeReversedFusedRNN(fw_lstm)
fw_out, fw_state = fw_lstm(inputs)
bw_out, bw_state = bw_lstm(inputs)
```

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(cell)
```



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





