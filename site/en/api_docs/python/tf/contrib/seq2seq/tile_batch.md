page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.tile_batch


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/beam_search_decoder.py#L101-L126">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Tile the batch dimension of a (possibly nested structure of) tensor(s) t.

``` python
tf.contrib.seq2seq.tile_batch(
    t,
    multiplier,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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
