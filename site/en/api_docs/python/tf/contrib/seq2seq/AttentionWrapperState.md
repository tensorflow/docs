

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.AttentionWrapperState

## Class `AttentionWrapperState`





Defined in [`tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py).

`namedtuple` storing the state of a `AttentionWrapper`.

Contains:

  - `cell_state`: The state of the wrapped `RNNCell` at the previous time
    step.
  - `attention`: The attention emitted at the previous time step.
  - `time`: int32 scalar containing the current time step.
  - `alignments`: A single or tuple of `Tensor`(s) containing the alignments
     emitted at the previous time step for each attention mechanism.
  - `alignment_history`: (if enabled) a single or tuple of `TensorArray`(s)
     containing alignment matrices from all time steps for each attention
     mechanism. Call `stack()` on each to convert to a `Tensor`.
  - `attention_state`: A single or tuple of nested objects
     containing attention mechanism state for each attention mechanism.
     The objects may contain Tensors or TensorArrays.

## Properties

<h3 id="alignment_history"><code>alignment_history</code></h3>

Alias for field number 4

<h3 id="alignments"><code>alignments</code></h3>

Alias for field number 3

<h3 id="attention"><code>attention</code></h3>

Alias for field number 1

<h3 id="attention_state"><code>attention_state</code></h3>

Alias for field number 5

<h3 id="cell_state"><code>cell_state</code></h3>

Alias for field number 0

<h3 id="time"><code>time</code></h3>

Alias for field number 2



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
__new__(
    _cls,
    cell_state,
    attention,
    time,
    alignments,
    alignment_history,
    attention_state
)
```

Create new instance of AttentionWrapperState(cell_state, attention, time, alignments, alignment_history, attention_state)

<h3 id="clone"><code>clone</code></h3>

``` python
clone(**kwargs)
```

Clone this object, overriding components provided by kwargs.

The new state fields' shape must match original state fields' shape. This
will be validated, and original fields' shape will be propagated to new
fields.

Example:

```python
initial_state = attention_wrapper.zero_state(dtype=..., batch_size=...)
initial_state = initial_state.clone(cell_state=encoder_state)
```

#### Args:

* <b>`**kwargs`</b>: Any properties of the state object to replace in the returned
    `AttentionWrapperState`.


#### Returns:

A new `AttentionWrapperState` whose properties are the same as
this one, except any overridden properties as provided in `kwargs`.



