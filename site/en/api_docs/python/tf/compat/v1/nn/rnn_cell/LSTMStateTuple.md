description: Tuple used by LSTM Cells for state_size, zero_state, and output state.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.rnn_cell.LSTMStateTuple" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="c"/>
<meta itemprop="property" content="h"/>
</div>

# tf.compat.v1.nn.rnn_cell.LSTMStateTuple

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py#L621-L637">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.rnn_cell.LSTMStateTuple(
    c, h
)
</code></pre>



<!-- Placeholder for "Used in" -->

Stores two elements: `(c, h)`, in that order. Where `c` is the hidden state
and `h` is the output.

Only used when `state_is_tuple=True`.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`c`
</td>
<td>

</td>
</tr><tr>
<td>
`h`
</td>
<td>

</td>
</tr><tr>
<td>
`dtype`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `c` <a id="c"></a>
* `h` <a id="h"></a>
