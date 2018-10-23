

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.DynamicAttentionWrapperState

### `class tf.contrib.seq2seq.DynamicAttentionWrapperState`



Defined in [`tensorflow/contrib/seq2seq/python/ops/dynamic_attention_wrapper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/seq2seq/python/ops/dynamic_attention_wrapper.py).

`namedtuple` storing the state of a `DynamicAttentionWrapper`.

Contains:

  - `cell_state`: The state of the wrapped `RNNCell`.
  - `attention`: The attention emitted at the previous time step.

## Properties

<h3 id="attention"><code>attention</code></h3>

Alias for field number 1

<h3 id="cell_state"><code>cell_state</code></h3>

Alias for field number 0



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
__new__(
    _cls,
    cell_state,
    attention
)
```

Create new instance of DynamicAttentionWrapperState(cell_state, attention)



