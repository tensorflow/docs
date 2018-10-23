

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.Decoder

### `class tf.contrib.seq2seq.Decoder`



Defined in [`tensorflow/contrib/seq2seq/python/ops/decoder.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/seq2seq/python/ops/decoder.py).

See the guide: [Seq2seq Library (contrib) > Dynamic Decoding](../../../../../api_guides/python/contrib.seq2seq#Dynamic_Decoding)

An RNN Decoder abstract interface object.

## Properties

<h3 id="batch_size"><code>batch_size</code></h3>

The batch size of the inputs returned by `sample`.

<h3 id="output_dtype"><code>output_dtype</code></h3>

A (possibly nested tuple of...) dtype[s].

<h3 id="output_size"><code>output_size</code></h3>

A (possibly nested tuple of...) integer[s] or `TensorShape` object[s].



## Methods

<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize(name=None)
```

Called before any decoding iterations.

#### Args:

* <b>`name`</b>: Name scope for any created operations.


#### Returns:

  `(finished, first_inputs, initial_state)`.

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

* <b>`time`</b>: Scalar `int32` tensor.
* <b>`inputs`</b>: Input (possibly nested tuple of) tensor[s] for this time step.
* <b>`state`</b>: State (possibly nested tuple of) tensor[s] from previous time step.
* <b>`name`</b>: Name scope for any created operations.


#### Returns:

  `(outputs, next_state, next_inputs, finished)`.



