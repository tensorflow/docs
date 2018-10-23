

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.seq2seq.hardmax

``` python
tf.contrib.seq2seq.hardmax(
    logits,
    name=None
)
```



Defined in [`tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py).

Returns batched one-hot vectors.

The depth index containing the `1` is that of the maximum logit value.

#### Args:

* <b>`logits`</b>: A batch tensor of logit values.
* <b>`name`</b>: Name to use when creating ops.

#### Returns:

A batched one-hot tensor.