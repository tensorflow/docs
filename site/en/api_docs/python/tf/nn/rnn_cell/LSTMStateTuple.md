page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.rnn_cell.LSTMStateTuple

## Class `LSTMStateTuple`

Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.



### Aliases:

* Class `tf.compat.v1.nn.rnn_cell.LSTMStateTuple`
* Class `tf.contrib.rnn.LSTMStateTuple`
* Class `tf.nn.rnn_cell.LSTMStateTuple`



Defined in [`python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/rnn_cell_impl.py).

<!-- Placeholder for "Used in" -->

Stores two elements: `(c, h)`, in that order. Where `c` is the hidden state
and `h` is the output.

Only used when `state_is_tuple=True`.

## Properties

<h3 id="c"><code>c</code></h3>




<h3 id="h"><code>h</code></h3>




<h3 id="dtype"><code>dtype</code></h3>






