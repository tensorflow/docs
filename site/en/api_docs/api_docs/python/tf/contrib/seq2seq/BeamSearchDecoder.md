

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.seq2seq.BeamSearchDecoder

## Class `BeamSearchDecoder`

Inherits From: [`Decoder`](../../../tf/contrib/seq2seq/Decoder)



Defined in [`tensorflow/contrib/seq2seq/python/ops/beam_search_decoder.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/seq2seq/python/ops/beam_search_decoder.py).

BeamSearch sampling decoder.

## Properties

<h3 id="batch_size"><code>batch_size</code></h3>



<h3 id="output_dtype"><code>output_dtype</code></h3>



<h3 id="output_size"><code>output_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    cell,
    embedding,
    start_tokens,
    end_token,
    initial_state,
    beam_width,
    output_layer=None,
    length_penalty_weight=0.0
)
```

Initialize BeamSearchDecoder.

#### Args:

* <b>`cell`</b>: An `RNNCell` instance.
* <b>`embedding`</b>: A callable that takes a vector tensor of `ids` (argmax ids),
    or the `params` argument for `embedding_lookup`.
* <b>`start_tokens`</b>: `int32` vector shaped `[batch_size]`, the start tokens.
* <b>`end_token`</b>: `int32` scalar, the token that marks end of decoding.
* <b>`initial_state`</b>: A (possibly nested tuple of...) tensors and TensorArrays.
* <b>`beam_width`</b>:  Python integer, the number of beams.
* <b>`output_layer`</b>: (Optional) An instance of `tf.layers.Layer`, i.e.,
    `tf.layers.Dense`.  Optional layer to apply to the RNN output prior
    to storing the result or sampling.
* <b>`length_penalty_weight`</b>: Float weight to penalize length. Disabled with 0.0.


#### Raises:

* <b>`TypeError`</b>: if `cell` is not an instance of `RNNCell`,
    or `output_layer` is not an instance of `tf.layers.Layer`.
* <b>`ValueError`</b>: If `start_tokens` is not a vector or
    `end_token` is not a scalar.

<h3 id="finalize"><code>finalize</code></h3>

``` python
finalize(
    outputs,
    final_state,
    sequence_lengths
)
```

Finalize and return the predicted_ids.

#### Args:

* <b>`outputs`</b>: An instance of BeamSearchDecoderOutput.
* <b>`final_state`</b>: An instance of BeamSearchDecoderState. Passed through to the
    output.
* <b>`sequence_lengths`</b>: An `int32` tensor shaped `[batch_size, beam_width]`.
    The sequence lengths determined for each beam during decode.


#### Returns:

* <b>`outputs`</b>: An instance of FinalBeamSearchDecoderOutput where the
    predicted_ids are the result of calling _gather_tree.
* <b>`final_state`</b>: The same input instance of BeamSearchDecoderState.

<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize(name=None)
```

Initialize the decoder.

#### Args:

* <b>`name`</b>: Name scope for any created operations.


#### Returns:

  `(finished, start_inputs, initial_state)`.

<h3 id="step"><code>step</code></h3>

``` python
step(
    time,
    inputs,
    state,
    name=None
)
```

Perform a decoding step.

#### Args:

* <b>`time`</b>: scalar `int32` tensor.
* <b>`inputs`</b>: A (structure of) input tensors.
* <b>`state`</b>: A (structure of) state tensors and TensorArrays.
* <b>`name`</b>: Name scope for any created operations.


#### Returns:

  `(outputs, next_state, next_inputs, finished)`.



