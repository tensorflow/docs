page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.crf.viterbi_decode

``` python
tf.contrib.crf.viterbi_decode(
    score,
    transition_params
)
```



Defined in [`tensorflow/contrib/crf/python/ops/crf.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/crf/python/ops/crf.py).

See the guide: [CRF (contrib)](../../../../../api_guides/python/contrib.crf)

Decode the highest scoring sequence of tags outside of TensorFlow.

This should only be used at test time.

#### Args:

* <b>`score`</b>: A [seq_len, num_tags] matrix of unary potentials.
* <b>`transition_params`</b>: A [num_tags, num_tags] matrix of binary potentials.


#### Returns:

* <b>`viterbi`</b>: A [seq_len] list of integers containing the highest scoring tag
      indices.
* <b>`viterbi_score`</b>: A float containing the score for the Viterbi sequence.