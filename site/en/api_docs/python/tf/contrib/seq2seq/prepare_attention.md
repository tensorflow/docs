


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.prepare_attention

### `tf.contrib.seq2seq.prepare_attention`

```
tf.contrib.seq2seq.prepare_attention(attention_states, attention_option, num_units, reuse=False)
```


Prepare keys/values/functions for attention.

#### Args:

* <b>`attention_states`</b>: hidden states to attend over.
* <b>`attention_option`</b>: how to compute attention, either "luong" or "bahdanau".
* <b>`num_units`</b>: hidden state dimension.
* <b>`reuse`</b>: whether to reuse variable scope.


#### Returns:

* <b>`attention_keys`</b>: to be compared with target states.
* <b>`attention_values`</b>: to be used to construct context vectors.
* <b>`attention_score_fn`</b>: to compute similarity between key and target states.
* <b>`attention_construct_fn`</b>: to build attention states.

Defined in [`tensorflow/contrib/seq2seq/python/ops/attention_decoder_fn.py`](https://www.tensorflow.org/code/tensorflow/contrib/seq2seq/python/ops/attention_decoder_fn.py).

