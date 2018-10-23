

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.LuongAttention

### `class tf.contrib.seq2seq.LuongAttention`



Defined in [`tensorflow/contrib/seq2seq/python/ops/dynamic_attention_wrapper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/seq2seq/python/ops/dynamic_attention_wrapper.py).

See the guide: [Seq2seq Library (contrib) > Attention](../../../../../api_guides/python/contrib.seq2seq#Attention)

Implements Luong-style (multiplicative) attention scoring.

This attention has two forms.  The first is standard Luong attention,
as described in:

Minh-Thang Luong, Hieu Pham, Christopher D. Manning.
"Effective Approaches to Attention-based Neural Machine Translation."
EMNLP 2015.  https://arxiv.org/abs/1508.04025

The second is the normalized form.  This form is inspired by the
normalization proposed for Bahdanau attention in

Colin Raffel, Thang Luong, Peter J. Liu, Ron J. Weiss, and Douglas Eck.
"Online and Linear-Time Attention by Enforcing Monotonic Alignments."
(Eq. 15).

To enable the second form, construct the object with parameter
`normalize=True`.

## Properties

<h3 id="keys"><code>keys</code></h3>



<h3 id="memory_layer"><code>memory_layer</code></h3>



<h3 id="query_layer"><code>query_layer</code></h3>



<h3 id="values"><code>values</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    num_units,
    memory,
    memory_sequence_length=None,
    normalize=False,
    attention_r_initializer=None,
    name='LuongAttention'
)
```

Construct the AttentionMechanism mechanism.

#### Args:

* <b>`num_units`</b>: The depth of the attention mechanism.
* <b>`memory`</b>: The memory to query; usually the output of an RNN encoder.  This
    tensor should be shaped `[batch_size, max_time, ...]`.
  memory_sequence_length (optional): Sequence lengths for the batch entries
    in memory.  If provided, the memory tensor rows are masked with zeros
    for values past the respective sequence lengths.
* <b>`normalize`</b>: Python boolean.  Whether to normalize the energy term.
* <b>`attention_r_initializer`</b>:  Initial value of the post-normalization bias
    when normalizing.  Default is `0`.
* <b>`name`</b>: Name to use when creating ops.

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(query)
```

Score the query based on the keys and values.

#### Args:

* <b>`query`</b>: Tensor of dtype matching `self.values` and shape
    `[batch_size, query_depth]`.


#### Returns:

* <b>`score`</b>: Tensor of dtype matching `self.values` and shape
    `[batch_size, max_time]` (`max_time` is memory's `max_time`).


#### Raises:

* <b>`ValueError`</b>: If `key` and `query` depths do not match.



