

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.DynamicAttentionWrapper

### `class tf.contrib.seq2seq.DynamicAttentionWrapper`



Defined in [`tensorflow/contrib/seq2seq/python/ops/dynamic_attention_wrapper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/seq2seq/python/ops/dynamic_attention_wrapper.py).

See the guide: [Seq2seq Library (contrib) > Attention](../../../../../api_guides/python/contrib.seq2seq#Attention)

Wraps another `RNNCell` with attention.
  

## Properties

<h3 id="output_size"><code>output_size</code></h3>



<h3 id="state_size"><code>state_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    cell,
    attention_mechanism,
    attention_size,
    cell_input_fn=None,
    probability_fn=None,
    output_attention=True,
    name=None
)
```

Construct the `DynamicAttentionWrapper`.

#### Args:

* <b>`cell`</b>: An instance of `RNNCell`.
* <b>`attention_mechanism`</b>: An instance of `AttentionMechanism`.
* <b>`attention_size`</b>: Python integer, the depth of the attention (output)
    tensor.
* <b>`cell_input_fn`</b>: (optional) A `callable`.  The default is:
    `lambda inputs, attention: array_ops.concat([inputs, attention], -1)`.
* <b>`probability_fn`</b>: (optional) A `callable`.  Converts the score to
    probabilities.  The default is [`tf.nn.softmax`](../../../tf/nn/softmax). Other options include
    [`tf.contrib.seq2seq.hardmax`](../../../tf/contrib/seq2seq/hardmax) and [`tf.contrib.sparsemax.sparsemax`](../../../tf/contrib/sparsemax/sparsemax).
* <b>`output_attention`</b>: Python bool.  If `True` (default), the output at each
    time step is the attention value.  This is the behavior of Luong-style
    attention mechanisms.  If `False`, the output at each time step is
    the output of `cell`.  This is the beahvior of Bhadanau-style
    attention mechanisms.  In both cases, the `attention` tensor is
    propagated to the next time step via the state and is used there.
    This flag only controls whether the attention mechanism is propagated
    up to the next cell in an RNN stack or to the top RNN output.
* <b>`name`</b>: Name to use when creating ops.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    inputs,
    state,
    scope=None
)
```

Perform a step of attention-wrapped RNN.

- Step 1: Mix the `inputs` and previous step's `attention` output via
  `cell_input_fn`.
- Step 2: Call the wrapped `cell` with this input and its previous state.
- Step 3: Score the cell's output with `attention_mechanism`.
- Step 4: Calculate the alignments by passing the score through the
  `normalizer`.
- Step 5: Calculate the context vector as the inner product between the
  alignments and the attention_mechanism's values (memory).
- Step 6: Calculate the attention output by concatenating the cell output
  and context through the attention layer.

#### Args:

* <b>`inputs`</b>: (Possibly nested tuple of) Tensor, the input at this time step.
* <b>`state`</b>: An instance of `DynamicAttentionWrapperState` containing
    tensors from the previous time step.
* <b>`scope`</b>: Must be `None`.


#### Returns:

  A tuple `(attention, next_state)`, where:

  - `attention` is the attention passed to the layer above.
  - `next_state` is an instance of `DynamicAttentionWrapperState`
     containing the state calculated at this time step.


#### Raises:

* <b>`NotImplementedError`</b>: if `scope` is not `None`.

<h3 id="zero_state"><code>zero_state</code></h3>

``` python
zero_state(
    batch_size,
    dtype
)
```





