page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.hardmax

Returns batched one-hot vectors.

``` python
tf.contrib.seq2seq.hardmax(
    logits,
    name=None
)
```



Defined in [`contrib/seq2seq/python/ops/attention_wrapper.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/seq2seq/python/ops/attention_wrapper.py).

<!-- Placeholder for "Used in" -->

The depth index containing the `1` is that of the maximum logit value.

#### Args:


* <b>`logits`</b>: A batch tensor of logit values.
* <b>`name`</b>: Name to use when creating ops.


#### Returns:

A batched one-hot tensor.
