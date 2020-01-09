page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.LSTMBlockWrapper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/rnn/python/ops/lstm_ops.py#L402-L537">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LSTMBlockWrapper`

This is a helper class that provides housekeeping for LSTM cells.

Inherits From: [`Layer`](../../../tf/layers/Layer)

<!-- Placeholder for "Used in" -->

This may be useful for alternative LSTM and similar type of cells.
The subclasses must implement `_call_cell` method and `num_units` property.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/layers/base.py#L192-L235">View source</a>

``` python
__init__(
    trainable=True,
    name=None,
    dtype=None,
    **kwargs
)
```






## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="num_units"><code>num_units</code></h3>

Number of units in this cell (output dimension).


<h3 id="scope_name"><code>scope_name</code></h3>
