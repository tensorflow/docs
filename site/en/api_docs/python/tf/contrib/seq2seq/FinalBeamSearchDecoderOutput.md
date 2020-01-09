page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.FinalBeamSearchDecoderOutput


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/beam_search_decoder.py#L65-L77">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `FinalBeamSearchDecoderOutput`

Final outputs returned by the beam search after all decoding is finished.



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`predicted_ids`</b>: The final prediction. A tensor of shape
  `[batch_size, T, beam_width]` (or `[T, batch_size, beam_width]` if
  `output_time_major` is True). Beams are ordered from best to worst.
* <b>`beam_search_decoder_output`</b>: An instance of `BeamSearchDecoderOutput` that
  describes the state of the beam search.

<h2 id="__new__"><code>__new__</code></h2>

``` python
__new__(
    _cls,
    predicted_ids,
    beam_search_decoder_output
)
```

Create new instance of FinalBeamDecoderOutput(predicted_ids, beam_search_decoder_output)




## Properties

<h3 id="predicted_ids"><code>predicted_ids</code></h3>




<h3 id="beam_search_decoder_output"><code>beam_search_decoder_output</code></h3>
