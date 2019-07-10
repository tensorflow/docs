page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.FusedRNNCellAdaptor

## Class `FusedRNNCellAdaptor`

This is an adaptor for RNNCell classes to be used with `FusedRNNCell`.

Inherits From: [`FusedRNNCell`](../../../tf/contrib/rnn/FusedRNNCell)



Defined in [`contrib/rnn/python/ops/fused_rnn_cell.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/fused_rnn_cell.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

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






