


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.attention_decoder_fn_train

### `tf.contrib.seq2seq.attention_decoder_fn_train`

```
tf.contrib.seq2seq.attention_decoder_fn_train(encoder_state, attention_keys, attention_values, attention_score_fn, attention_construct_fn, name=None)
```


Attentional decoder function for `dynamic_rnn_decoder` during training.

The `attention_decoder_fn_train` is a training function for an
attention-based sequence-to-sequence model. It should be used when
`dynamic_rnn_decoder` is in the training mode.

The `attention_decoder_fn_train` is called with a set of the user arguments
and returns the `decoder_fn`, which can be passed to the
`dynamic_rnn_decoder`, such that

```
dynamic_fn_train = attention_decoder_fn_train(encoder_state)
outputs_train, state_train = dynamic_rnn_decoder(
    decoder_fn=dynamic_fn_train, ...)
```

Further usage can be found in the `kernel_tests/seq2seq_test.py`.

#### Args:

* <b>`encoder_state`</b>: The encoded state to initialize the `dynamic_rnn_decoder`.
* <b>`attention_keys`</b>: to be compared with target states.
* <b>`attention_values`</b>: to be used to construct context vectors.
* <b>`attention_score_fn`</b>: to compute similarity between key and target states.
* <b>`attention_construct_fn`</b>: to build attention states.
* <b>`name`</b>: (default: `None`) NameScope for the decoder function;
    defaults to "simple_decoder_fn_train"


#### Returns:

  A decoder function with the required interface of `dynamic_rnn_decoder`
  intended for training.

Defined in [`tensorflow/contrib/seq2seq/python/ops/attention_decoder_fn.py`](https://www.tensorflow.org/code/tensorflow/contrib/seq2seq/python/ops/attention_decoder_fn.py).

