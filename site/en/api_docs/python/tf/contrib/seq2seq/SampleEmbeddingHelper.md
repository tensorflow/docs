page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.SampleEmbeddingHelper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L631-L678">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SampleEmbeddingHelper`

A helper for use during inference.

Inherits From: [`GreedyEmbeddingHelper`](../../../tf/contrib/seq2seq/GreedyEmbeddingHelper)

<!-- Placeholder for "Used in" -->

Uses sampling (from a distribution) instead of argmax and passes the
result through an embedding layer to get the next input.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L638-L662">View source</a>

``` python
__init__(
    embedding,
    start_tokens,
    end_token,
    softmax_temperature=None,
    seed=None
)
```

Initializer.


#### Args:


* <b>`embedding`</b>: A callable that takes a vector tensor of `ids` (argmax ids),
  or the `params` argument for `embedding_lookup`. The returned tensor
  will be passed to the decoder input.
* <b>`start_tokens`</b>: `int32` vector shaped `[batch_size]`, the start tokens.
* <b>`end_token`</b>: `int32` scalar, the token that marks end of decoding.
* <b>`softmax_temperature`</b>: (Optional) `float32` scalar, value to divide the
  logits by before computing the softmax. Larger values (above 1.0) result
  in more random samples, while smaller values push the sampling
  distribution towards the argmax. Must be strictly greater than 0.
  Defaults to 1.0.
* <b>`seed`</b>: (Optional) The sampling seed.


#### Raises:


* <b>`ValueError`</b>: if `start_tokens` is not a 1D tensor or `end_token` is not a
  scalar.



## Properties

<h3 id="batch_size"><code>batch_size</code></h3>

Batch size of tensor returned by `sample`.

Returns a scalar int32 tensor.

<h3 id="sample_ids_dtype"><code>sample_ids_dtype</code></h3>

DType of tensor returned by `sample`.

Returns a DType.

<h3 id="sample_ids_shape"><code>sample_ids_shape</code></h3>

Shape of tensor returned by `sample`, excluding the batch dimension.

Returns a `TensorShape`.



## Methods

<h3 id="initialize"><code>initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L604-L606">View source</a>

``` python
initialize(name=None)
```

Returns `(initial_finished, initial_inputs)`.


<h3 id="next_inputs"><code>next_inputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L618-L628">View source</a>

``` python
next_inputs(
    time,
    outputs,
    state,
    sample_ids,
    name=None
)
```

next_inputs_fn for GreedyEmbeddingHelper.


<h3 id="sample"><code>sample</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L664-L678">View source</a>

``` python
sample(
    time,
    outputs,
    state,
    name=None
)
```

sample for SampleEmbeddingHelper.
