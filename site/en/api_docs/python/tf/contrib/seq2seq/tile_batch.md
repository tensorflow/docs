page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.tile_batch

``` python
tf.contrib.seq2seq.tile_batch(
    t,
    multiplier,
    name=None
)
```



Defined in [`tensorflow/contrib/seq2seq/python/ops/beam_search_decoder.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/seq2seq/python/ops/beam_search_decoder.py).

Tile the batch dimension of a (possibly nested structure of) tensor(s) t.

For each tensor t in a (possibly nested structure) of tensors,
this function takes a tensor t shaped `[batch_size, s0, s1, ...]` composed of
minibatch entries `t[0], ..., t[batch_size - 1]` and tiles it to have a shape
`[batch_size * multiplier, s0, s1, ...]` composed of minibatch entries
`t[0], t[0], ..., t[1], t[1], ...` where each minibatch entry is repeated
`multiplier` times.

#### Args:

* <b>`t`</b>: `Tensor` shaped `[batch_size, ...]`.
* <b>`multiplier`</b>: Python int.
* <b>`name`</b>: Name scope for any created operations.


#### Returns:

A (possibly nested structure of) `Tensor` shaped
`[batch_size * multiplier, ...]`.


#### Raises:

* <b>`ValueError`</b>: if tensor(s) `t` do not have a statically known rank or
  the rank is < 1.