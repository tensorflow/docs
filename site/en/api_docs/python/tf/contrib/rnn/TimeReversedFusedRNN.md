page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.TimeReversedFusedRNN

## Class `TimeReversedFusedRNN`

This is an adaptor to time-reverse a FusedRNNCell.

Inherits From: [`FusedRNNCell`](../../../tf/contrib/rnn/FusedRNNCell)



Defined in [`contrib/rnn/python/ops/fused_rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py).

<!-- Placeholder for "Used in" -->

For example,

```python
cell = tf.compat.v1.nn.rnn_cell.BasicRNNCell(10)
fw_lstm = tf.contrib.rnn.FusedRNNCellAdaptor(cell, use_dynamic_rnn=True)
bw_lstm = tf.contrib.rnn.TimeReversedFusedRNN(fw_lstm)
fw_out, fw_state = fw_lstm(inputs)
bw_out, bw_state = bw_lstm(inputs)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(cell)
```






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






