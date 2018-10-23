

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.crf.crf_log_norm

``` python
tf.contrib.crf.crf_log_norm(
    inputs,
    sequence_lengths,
    transition_params
)
```



Defined in [`tensorflow/contrib/crf/python/ops/crf.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/crf/python/ops/crf.py).

See the guide: [CRF (contrib)](../../../../../api_guides/python/contrib.crf)

Computes the normalization for a CRF.

#### Args:

* <b>`inputs`</b>: A [batch_size, max_seq_len, num_tags] tensor of unary potentials
      to use as input to the CRF layer.
* <b>`sequence_lengths`</b>: A [batch_size] vector of true sequence lengths.
* <b>`transition_params`</b>: A [num_tags, num_tags] transition matrix.

#### Returns:

* <b>`log_norm`</b>: A [batch_size] vector of normalizers for a CRF.