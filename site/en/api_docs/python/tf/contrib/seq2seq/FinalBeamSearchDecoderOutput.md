page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.FinalBeamSearchDecoderOutput

## Class `FinalBeamSearchDecoderOutput`

Final outputs returned by the beam search after all decoding is finished.





Defined in [`contrib/seq2seq/python/ops/beam_search_decoder.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/seq2seq/python/ops/beam_search_decoder.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`predicted_ids`</b>: The final prediction. A tensor of shape
  `[batch_size, T, beam_width]` (or `[T, batch_size, beam_width]` if
  `output_time_major` is True). Beams are ordered from best to worst.
* <b>`beam_search_decoder_output`</b>: An instance of `BeamSearchDecoderOutput` that
  describes the state of the beam search.

## Properties

<h3 id="predicted_ids"><code>predicted_ids</code></h3>




<h3 id="beam_search_decoder_output"><code>beam_search_decoder_output</code></h3>






