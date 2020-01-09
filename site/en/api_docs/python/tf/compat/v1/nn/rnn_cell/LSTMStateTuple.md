page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.nn.rnn_cell.LSTMStateTuple


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/rnn_cell_impl.py#L616-L632">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LSTMStateTuple`

Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.



<!-- Placeholder for "Used in" -->

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
