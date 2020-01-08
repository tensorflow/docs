page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.rnn_cell.LSTMStateTuple

## Class `LSTMStateTuple`



### Aliases:

* Class `tf.contrib.rnn.LSTMStateTuple`
* Class `tf.nn.rnn_cell.LSTMStateTuple`



Defined in [`tensorflow/python/ops/rnn_cell_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/rnn_cell_impl.py).

Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.

Stores two elements: `(c, h)`, in that order. Where `c` is the hidden state
and `h` is the output.

Only used when `state_is_tuple=True`.

<h2 id="__new__"><code>__new__</code></h2>

``` python
__new__(
    _cls,
    c,
    h
)
```

Create new instance of LSTMStateTuple(c, h)



## Properties

<h3 id="c"><code>c</code></h3>



<h3 id="h"><code>h</code></h3>



<h3 id="dtype"><code>dtype</code></h3>





