

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.FusedRNNCellAdaptor

## Class `FusedRNNCellAdaptor`

Inherits From: [`FusedRNNCell`](../../../tf/contrib/rnn/FusedRNNCell)



Defined in [`tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py).

See the guide: [RNN and Cells (contrib) > Core RNN Cell wrappers (RNNCells that wrap other RNNCells)](../../../../../api_guides/python/contrib.rnn#Core_RNN_Cell_wrappers_RNNCells_that_wrap_other_RNNCells_)

This is an adaptor for RNNCell classes to be used with `FusedRNNCell`.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    cell,
    use_dynamic_rnn=False
)
```

Initialize the adaptor.

#### Args:

* <b>`cell`</b>: an instance of a subclass of a `rnn_cell.RNNCell`.
* <b>`use_dynamic_rnn`</b>: whether to use dynamic (or static) RNN.

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





