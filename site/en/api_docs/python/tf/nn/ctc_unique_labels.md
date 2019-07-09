page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.ctc_unique_labels

``` python
tf.nn.ctc_unique_labels(
    labels,
    name=None
)
```



Defined in [`tensorflow/python/ops/ctc_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/ctc_ops.py).

Get unique labels and indices for batched labels for tf.nn.ctc_loss.

For use with tf.nn.ctc_loss_v2 optional argument `unique`: This op can be
used to preprocess labels in input pipeline to for better speed/memory use
computing the ctc loss on TPU.

Example:
  ctc_unique_labels([[3, 4, 4, 3]]) ->
    unique labels padded with 0: [[3, 4, 0, 0]]
    indices of original labels in unique: [0, 1, 1, 0]

#### Args:

* <b>`labels`</b>: tensor of shape [batch_size, max_label_length] padded with 0.
* <b>`name`</b>: A name for this `Op`. Defaults to "ctc_unique_labels".


#### Returns:

tuple of
  - unique labels, tensor of shape `[batch_size, max_label_length]`
  - indices into unique labels, shape `[batch_size, max_label_length]`