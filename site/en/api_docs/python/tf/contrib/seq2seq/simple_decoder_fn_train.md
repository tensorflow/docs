


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.simple_decoder_fn_train

### `tf.contrib.seq2seq.simple_decoder_fn_train`

```
tf.contrib.seq2seq.simple_decoder_fn_train(encoder_state, name=None)
```


Simple decoder function for a sequence-to-sequence model used in the
`dynamic_rnn_decoder`.

The `simple_decoder_fn_train` is a simple training function for a
sequence-to-sequence model. It should be used when `dynamic_rnn_decoder` is
in the training mode.

The `simple_decoder_fn_train` is called with a set of the user arguments and
returns the `decoder_fn`, which can be passed to the `dynamic_rnn_decoder`,
such that

```
dynamic_fn_train = simple_decoder_fn_train(encoder_state)
outputs_train, state_train = dynamic_rnn_decoder(
    decoder_fn=dynamic_fn_train, ...)
```

Further usage can be found in the `kernel_tests/seq2seq_test.py`.

#### Args:

* <b>`encoder_state`</b>: The encoded state to initialize the `dynamic_rnn_decoder`.
* <b>`name`</b>: (default: `None`) NameScope for the decoder function;
    defaults to "simple_decoder_fn_train"


#### Returns:

  A decoder function with the required interface of `dynamic_rnn_decoder`
  intended for training.

Defined in [`tensorflow/contrib/seq2seq/python/ops/decoder_fn.py`](https://www.tensorflow.org/code/tensorflow/contrib/seq2seq/python/ops/decoder_fn.py).

