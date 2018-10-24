

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.BahdanauMonotonicAttention

## Class `BahdanauMonotonicAttention`





Defined in [`tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py).

Monotonic attention mechanism with Bahadanau-style energy function.

This type of attention enforces a monotonic constraint on the attention
distributions; that is once the model attends to a given point in the memory
it can't attend to any prior points at subsequence output timesteps.  It
achieves this by using the _monotonic_probability_fn instead of softmax to
construct its attention distributions.  Since the attention scores are passed
through a sigmoid, a learnable scalar bias parameter is applied after the
score function and before the sigmoid.  Otherwise, it is equivalent to
BahdanauAttention.  This approach is proposed in

Colin Raffel, Minh-Thang Luong, Peter J. Liu, Ron J. Weiss, Douglas Eck,
"Online and Linear-Time Attention by Enforcing Monotonic Alignments."
ICML 2017.  https://arxiv.org/abs/1704.00784

## Properties

<h3 id="alignments_size"><code>alignments_size</code></h3>



<h3 id="batch_size"><code>batch_size</code></h3>



<h3 id="keys"><code>keys</code></h3>



<h3 id="memory_layer"><code>memory_layer</code></h3>



<h3 id="query_layer"><code>query_layer</code></h3>



<h3 id="state_size"><code>state_size</code></h3>



<h3 id="values"><code>values</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    num_units,
    memory,
    memory_sequence_length=None,
    normalize=False,
    score_mask_value=None,
    sigmoid_noise=0.0,
    sigmoid_noise_seed=None,
    score_bias_init=0.0,
    mode='parallel',
    dtype=None,
    name='BahdanauMonotonicAttention'
)
```

Construct the Attention mechanism.

#### Args:

* <b>`num_units`</b>: The depth of the query mechanism.
* <b>`memory`</b>: The memory to query; usually the output of an RNN encoder.  This
    tensor should be shaped `[batch_size, max_time, ...]`.
  memory_sequence_length (optional): Sequence lengths for the batch entries
    in memory.  If provided, the memory tensor rows are masked with zeros
    for values past the respective sequence lengths.
* <b>`normalize`</b>: Python boolean.  Whether to normalize the energy term.
* <b>`score_mask_value`</b>: (optional): The mask value for score before passing into
    `probability_fn`. The default is -inf. Only used if
    `memory_sequence_length` is not None.
* <b>`sigmoid_noise`</b>: Standard deviation of pre-sigmoid noise.  See the docstring
    for `_monotonic_probability_fn` for more information.
* <b>`sigmoid_noise_seed`</b>: (optional) Random seed for pre-sigmoid noise.
* <b>`score_bias_init`</b>: Initial value for score bias scalar.  It's recommended to
    initialize this to a negative value when the length of the memory is
    large.
* <b>`mode`</b>: How to compute the attention distribution.  Must be one of
    'recursive', 'parallel', or 'hard'.  See the docstring for
    <a href="../../../tf/contrib/seq2seq/monotonic_attention"><code>tf.contrib.seq2seq.monotonic_attention</code></a> for more information.
* <b>`dtype`</b>: The data type for the query and memory layers of the attention
    mechanism.
* <b>`name`</b>: Name to use when creating ops.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    query,
    state
)
```

Score the query based on the keys and values.

#### Args:

* <b>`query`</b>: Tensor of dtype matching `self.values` and shape
    `[batch_size, query_depth]`.
* <b>`state`</b>: Tensor of dtype matching `self.values` and shape
    `[batch_size, alignments_size]`
    (`alignments_size` is memory's `max_time`).


#### Returns:

* <b>`alignments`</b>: Tensor of dtype matching `self.values` and shape
    `[batch_size, alignments_size]` (`alignments_size` is memory's
    `max_time`).

<h3 id="initial_alignments"><code>initial_alignments</code></h3>

``` python
initial_alignments(
    batch_size,
    dtype
)
```

Creates the initial alignment values for the monotonic attentions.

Initializes to dirac distributions, i.e. [1, 0, 0, ...memory length..., 0]
for all entries in the batch.

#### Args:

* <b>`batch_size`</b>: `int32` scalar, the batch_size.
* <b>`dtype`</b>: The `dtype`.


#### Returns:

A `dtype` tensor shaped `[batch_size, alignments_size]`
(`alignments_size` is the values' `max_time`).

<h3 id="initial_state"><code>initial_state</code></h3>

``` python
initial_state(
    batch_size,
    dtype
)
```

Creates the initial state values for the `AttentionWrapper` class.

This is important for AttentionMechanisms that use the previous alignment
to calculate the alignment at the next time step (e.g. monotonic attention).

The default behavior is to return the same output as initial_alignments.

#### Args:

* <b>`batch_size`</b>: `int32` scalar, the batch_size.
* <b>`dtype`</b>: The `dtype`.


#### Returns:

A structure of all-zero tensors with shapes as described by `state_size`.



