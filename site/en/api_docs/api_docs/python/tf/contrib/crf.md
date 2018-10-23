

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.crf



Defined in [`tensorflow/contrib/crf/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/crf/__init__.py).

Linear-chain CRF layer.

See the [CRF (contrib)](../../../../api_guides/python/contrib.crf) guide.


## Classes

[`class CrfForwardRnnCell`](../../tf/contrib/crf/CrfForwardRnnCell): Computes the alpha values in a linear-chain CRF.

## Functions

[`crf_binary_score(...)`](../../tf/contrib/crf/crf_binary_score): Computes the binary scores of tag sequences.

[`crf_log_likelihood(...)`](../../tf/contrib/crf/crf_log_likelihood): Computes the log-likelihood of tag sequences in a CRF.

[`crf_log_norm(...)`](../../tf/contrib/crf/crf_log_norm): Computes the normalization for a CRF.

[`crf_sequence_score(...)`](../../tf/contrib/crf/crf_sequence_score): Computes the unnormalized score for a tag sequence.

[`crf_unary_score(...)`](../../tf/contrib/crf/crf_unary_score): Computes the unary scores of tag sequences.

[`viterbi_decode(...)`](../../tf/contrib/crf/viterbi_decode): Decode the highest scoring sequence of tags outside of TensorFlow.

