page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.ctc_beam_search_decoder_v2

``` python
tf.nn.ctc_beam_search_decoder_v2(
    inputs,
    sequence_length,
    beam_width=100,
    top_paths=1
)
```



Defined in [`tensorflow/python/ops/ctc_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/ctc_ops.py).

Performs beam search decoding on the logits given in input.

**Note** The `ctc_greedy_decoder` is a special case of the
`ctc_beam_search_decoder` with `top_paths=1` and `beam_width=1` (but
that decoder is faster for this special case).

#### Args:

* <b>`inputs`</b>: 3-D `float` `Tensor`, size
    `[max_time, batch_size, num_classes]`.  The logits.
* <b>`sequence_length`</b>: 1-D `int32` vector containing sequence lengths,
    having size `[batch_size]`.
* <b>`beam_width`</b>: An int scalar >= 0 (beam search beam width).
* <b>`top_paths`</b>: An int scalar >= 0, <= beam_width (controls output size).


#### Returns:

A tuple `(decoded, log_probabilities)` where

* <b>`decoded`</b>: A list of length top_paths, where `decoded[j]`
    is a `SparseTensor` containing the decoded outputs:

    `decoded[j].indices`: Indices matrix `[total_decoded_outputs[j], 2]`;
      The rows store: `[batch, time]`.

    `decoded[j].values`: Values vector, size `[total_decoded_outputs[j]]`.
      The vector stores the decoded classes for beam `j`.

    `decoded[j].dense_shape`: Shape vector, size `(2)`.
      The shape values are: `[batch_size, max_decoded_length[j]]`.

* <b>`log_probability`</b>: A `float` matrix `[batch_size, top_paths]` containing
      sequence log-probabilities.