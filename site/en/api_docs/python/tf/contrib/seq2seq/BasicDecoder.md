page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.BasicDecoder


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/basic_decoder.py#L44-L147">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `BasicDecoder`

Basic sampling decoder.

Inherits From: [`Decoder`](../../../tf/contrib/seq2seq/Decoder)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/basic_decoder.py#L47-L72">View source</a>

``` python
__init__(
    cell,
    helper,
    initial_state,
    output_layer=None
)
```

Initialize BasicDecoder.


#### Args:


* <b>`cell`</b>: An `RNNCell` instance.
* <b>`helper`</b>: A `Helper` instance.
* <b>`initial_state`</b>: A (possibly nested tuple of...) tensors and TensorArrays.
  The initial state of the RNNCell.
* <b>`output_layer`</b>: (Optional) An instance of <a href="../../../tf/layers/Layer"><code>tf.compat.v1.layers.Layer</code></a>, i.e.,
  <a href="../../../tf/layers/Dense"><code>tf.compat.v1.layers.Dense</code></a>. Optional layer to apply to the RNN output
  prior to storing the result or sampling.


#### Raises:


* <b>`TypeError`</b>: if `cell`, `helper` or `output_layer` have an incorrect type.



## Properties

<h3 id="batch_size"><code>batch_size</code></h3>

The batch size of input values.


<h3 id="output_dtype"><code>output_dtype</code></h3>

A (possibly nested tuple of...) dtype[s].


<h3 id="output_size"><code>output_size</code></h3>

A (possibly nested tuple of...) integer[s] or `TensorShape` object[s].


<h3 id="tracks_own_finished"><code>tracks_own_finished</code></h3>

Describes whether the Decoder keeps track of finished states.

Most decoders will emit a true/false `finished` value independently
at each time step.  In this case, the `dynamic_decode` function keeps track
of which batch entries are already finished, and performs a logical OR to
insert new batches to the finished set.

Some decoders, however, shuffle batches / beams between time steps and
`dynamic_decode` will mix up the finished state across these entries because
it does not track the reshuffle across time steps.  In this case, it is
up to the decoder to declare that it will keep track of its own finished
state by setting this property to `True`.

#### Returns:

Python bool.




## Methods

<h3 id="finalize"><code>finalize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/decoder.py#L115-L130">View source</a>

``` python
finalize(
    outputs,
    final_state,
    sequence_lengths
)
```

Called after decoding iterations complete.


#### Args:


* <b>`outputs`</b>: RNNCell outputs (possibly nested tuple of) tensor[s] for all time
  steps.
* <b>`final_state`</b>: RNNCell final state (possibly nested tuple of) tensor[s] for
  last time step.
* <b>`sequence_lengths`</b>: 1-D `int32` tensor containing lengths of each sequence.


#### Returns:

`(final_outputs, final_state)`: `final_outputs` is an object containing
the final decoder output, `final_state` is a (structure of) state tensors
and TensorArrays.


<h3 id="initialize"><code>initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/basic_decoder.py#L112-L121">View source</a>

``` python
initialize(name=None)
```

Initialize the decoder.


#### Args:


* <b>`name`</b>: Name scope for any created operations.


#### Returns:

`(finished, first_inputs, initial_state)`.


<h3 id="step"><code>step</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/basic_decoder.py#L123-L147">View source</a>

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
