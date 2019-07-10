page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.rnn.LSTMBlockFusedCell

## Class `LSTMBlockFusedCell`

FusedRNNCell implementation of LSTM.

Inherits From: [`LSTMBlockWrapper`](../../../tf/contrib/rnn/LSTMBlockWrapper)



Defined in [`contrib/rnn/python/ops/lstm_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/rnn/python/ops/lstm_ops.py).

<!-- Placeholder for "Used in" -->

This is an extremely efficient LSTM implementation, that uses a single TF op
for the entire LSTM. It should be both faster and more memory-efficient than
LSTMBlockCell defined above.

The implementation is based on: http://arxiv.org/abs/1409.2329.

We add forget_bias (default: 1) to the biases of the forget gate in order to
reduce the scale of forgetting in the beginning of the training.

The variable naming is consistent with `rnn_cell_impl.LSTMCell`.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_units,
    forget_bias=1.0,
    cell_clip=None,
    use_peephole=False,
    reuse=None,
    dtype=None,
    name='lstm_fused_cell'
)
```

Initialize the LSTM cell.


#### Args:


* <b>`num_units`</b>: int, The number of units in the LSTM cell.
* <b>`forget_bias`</b>: float, The bias added to forget gates (see above).
* <b>`cell_clip`</b>: clip the cell to this value. Defaults is no cell clipping.
* <b>`use_peephole`</b>: Whether to use peephole connections or not.
* <b>`reuse`</b>: (optional) boolean describing whether to reuse variables in an
  existing scope.  If not `True`, and the existing scope already has the
  given variables, an error is raised.
* <b>`dtype`</b>: the dtype of variables of this layer.
* <b>`name`</b>: String, the name of the layer. Layers with the same name will
  share weights, but to avoid mistakes we require reuse=True in such
  cases.  By default this is "lstm_cell", for variable-name compatibility
  with <a href="../../../tf/nn/rnn_cell/LSTMCell"><code>tf.compat.v1.nn.rnn_cell.LSTMCell</code></a>.



## Properties

<h3 id="graph"><code>graph</code></h3>

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Stop using this property because tf.layers layers no longer track their graph.

<h3 id="num_units"><code>num_units</code></h3>

Number of units in this cell (output dimension).


<h3 id="scope_name"><code>scope_name</code></h3>






