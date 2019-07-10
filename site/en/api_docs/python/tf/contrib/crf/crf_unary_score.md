page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.crf.crf_unary_score

``` python
tf.contrib.crf.crf_unary_score(
    tag_indices,
    sequence_lengths,
    inputs
)
```



Defined in [`tensorflow/contrib/crf/python/ops/crf.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/crf/python/ops/crf.py).

Computes the unary scores of tag sequences.

#### Args:

* <b>`tag_indices`</b>: A [batch_size, max_seq_len] matrix of tag indices.
* <b>`sequence_lengths`</b>: A [batch_size] vector of true sequence lengths.
* <b>`inputs`</b>: A [batch_size, max_seq_len, num_tags] tensor of unary potentials.

#### Returns:

* <b>`unary_scores`</b>: A [batch_size] vector of unary scores.