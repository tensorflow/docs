page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.crf.crf_unary_score


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/crf/python/ops/crf.py#L265-L298">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the unary scores of tag sequences.

``` python
tf.contrib.crf.crf_unary_score(
    tag_indices,
    sequence_lengths,
    inputs
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`tag_indices`</b>: A [batch_size, max_seq_len] matrix of tag indices.
* <b>`sequence_lengths`</b>: A [batch_size] vector of true sequence lengths.
* <b>`inputs`</b>: A [batch_size, max_seq_len, num_tags] tensor of unary potentials.

#### Returns:


* <b>`unary_scores`</b>: A [batch_size] vector of unary scores.
