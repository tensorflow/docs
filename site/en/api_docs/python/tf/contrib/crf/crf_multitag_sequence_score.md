page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.crf.crf_multitag_sequence_score

Computes the unnormalized score of all tag sequences matching tag_bitmap.

``` python
tf.contrib.crf.crf_multitag_sequence_score(
    inputs,
    tag_bitmap,
    sequence_lengths,
    transition_params
)
```



Defined in [`contrib/crf/python/ops/crf.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/crf/python/ops/crf.py).

<!-- Placeholder for "Used in" -->

tag_bitmap enables more than one tag to be considered correct at each time
step. This is useful when an observed output at a given time step is
consistent with more than one tag, and thus the log likelihood of that
observation must take into account all possible consistent tags.

Using one-hot vectors in tag_bitmap gives results identical to
crf_sequence_score.

#### Args:


* <b>`inputs`</b>: A [batch_size, max_seq_len, num_tags] tensor of unary potentials
    to use as input to the CRF layer.
* <b>`tag_bitmap`</b>: A [batch_size, max_seq_len, num_tags] boolean tensor
    representing all active tags at each index for which to calculate the
    unnormalized score.
* <b>`sequence_lengths`</b>: A [batch_size] vector of true sequence lengths.
* <b>`transition_params`</b>: A [num_tags, num_tags] transition matrix.

#### Returns:


* <b>`sequence_scores`</b>: A [batch_size] vector of unnormalized sequence scores.