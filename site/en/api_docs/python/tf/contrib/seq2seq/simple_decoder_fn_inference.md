


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.simple_decoder_fn_inference

### `tf.contrib.seq2seq.simple_decoder_fn_inference`

```
tf.contrib.seq2seq.simple_decoder_fn_inference(output_fn, encoder_state, embeddings, start_of_sequence_id, end_of_sequence_id, maximum_length, num_decoder_symbols, dtype=tf.int32, name=None)
```


Simple decoder function for a sequence-to-sequence model used in the
`dynamic_rnn_decoder`.

The `simple_decoder_fn_inference` is a simple inference function for a
sequence-to-sequence model. It should be used when `dynamic_rnn_decoder` is
in the inference mode.

The `simple_decoder_fn_inference` is called with a set of the user arguments
and returns the `decoder_fn`, which can be passed to the
`dynamic_rnn_decoder`, such that

```
dynamic_fn_inference = simple_decoder_fn_inference(...)
outputs_inference, state_inference = dynamic_rnn_decoder(
    decoder_fn=dynamic_fn_inference, ...)
```

Further usage can be found in the `kernel_tests/seq2seq_test.py`.

#### Args:

* <b>`output_fn`</b>: An output function to project your `cell_output` onto class
  logits.

  An example of an output function;

>       tf.variable_scope("decoder") as varscope
>         output_fn = lambda x: layers.linear(x, num_decoder_symbols,
>                                             scope=varscope)
>     
>         outputs_train, state_train = seq2seq.dynamic_rnn_decoder(...)
>         logits_train = output_fn(outputs_train)
>     
>         varscope.reuse_variables()
>         logits_inference, state_inference = seq2seq.dynamic_rnn_decoder(
>             output_fn=output_fn, ...)

  If `None` is supplied it will act as an identity function, which
  might be wanted when using the RNNCell `OutputProjectionWrapper`.

* <b>`encoder_state`</b>: The encoded state to initialize the `dynamic_rnn_decoder`.
* <b>`embeddings`</b>: The embeddings matrix used for the decoder sized
  `[num_decoder_symbols, embedding_size]`.
* <b>`start_of_sequence_id`</b>: The start of sequence ID in the decoder embeddings.
* <b>`end_of_sequence_id`</b>: The end of sequence ID in the decoder embeddings.
* <b>`maximum_length`</b>: The maximum allowed of time steps to decode.
* <b>`num_decoder_symbols`</b>: The number of classes to decode at each time step.
* <b>`dtype`</b>: (default: `dtypes.int32`) The default data type to use when
  handling integer objects.
* <b>`name`</b>: (default: `None`) NameScope for the decoder function;
    defaults to "simple_decoder_fn_inference"


#### Returns:

  A decoder function with the required interface of `dynamic_rnn_decoder`
  intended for inference.

Defined in [`tensorflow/contrib/seq2seq/python/ops/decoder_fn.py`](https://www.tensorflow.org/code/tensorflow/contrib/seq2seq/python/ops/decoder_fn.py).

