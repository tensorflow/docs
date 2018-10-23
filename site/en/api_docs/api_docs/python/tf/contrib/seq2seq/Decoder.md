

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.seq2seq.Decoder

## Class `Decoder`





Defined in [`tensorflow/contrib/seq2seq/python/ops/decoder.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/seq2seq/python/ops/decoder.py).

See the guide: [Seq2seq Library (contrib) > Dynamic Decoding](../../../../../api_guides/python/contrib.seq2seq#Dynamic_Decoding)

An RNN Decoder abstract interface object.

Concepts used by this interface:
- `inputs`: (structure of) tensors and TensorArrays that is passed as input to
  the RNNCell composing the decoder, at each time step.
- `state`: (structure of) tensors and TensorArrays that is passed to the
  RNNCell instance as the state.
- `finished`: boolean tensor telling whether each sequence in the batch is
  finished.
- `outputs`: Instance of BasicDecoderOutput. Result of the decoding, at each
  time step.

## Properties

<h3 id="batch_size"><code>batch_size</code></h3>

The batch size of input values.

<h3 id="output_dtype"><code>output_dtype</code></h3>

A (possibly nested tuple of...) dtype[s].

<h3 id="output_size"><code>output_size</code></h3>

A (possibly nested tuple of...) integer[s] or `TensorShape` object[s].



## Methods

<h3 id="finalize"><code>finalize</code></h3>

``` python
finalize(
    outputs,
    final_state,
    sequence_lengths
)
```



<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize(name=None)
```

Called before any decoding iterations.

This methods must compute initial input values and initial state.

#### Args:

* <b>`name`</b>: Name scope for any created operations.


#### Returns:

  `(finished, initial_inputs, initial_state)`: initial values of
  'finished' flags, inputs and state.

<h3 id="step"><code>step</code></h3>

``` python
step(
    time,
    inputs,
    state,
    name=None
)
```

Called per step of decoding (but only once for dynamic decoding).

#### Args:

* <b>`time`</b>: Scalar `int32` tensor. Current step number.
* <b>`inputs`</b>: RNNCell input (possibly nested tuple of) tensor[s] for this time
    step.
* <b>`state`</b>: RNNCell state (possibly nested tuple of) tensor[s] from previous
    time step.
* <b>`name`</b>: Name scope for any created operations.


#### Returns:

  `(outputs, next_state, next_inputs, finished)`: `outputs` is an object
  containing the decoder output, `next_state` is a (structure of) state tensors
  and TensorArrays, `next_inputs` is the tensor that should be used as input for
  the next step, `finished` is a boolean tensor telling whether the sequence
  is complete, for each sequence in the batch.



