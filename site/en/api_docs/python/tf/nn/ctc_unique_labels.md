page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.ctc_unique_labels

Get unique labels and indices for batched labels for <a href="../../tf/nn/ctc_loss"><code>tf.nn.ctc_loss</code></a>.

### Aliases:

* `tf.compat.v1.nn.ctc_unique_labels`
* `tf.compat.v2.nn.ctc_unique_labels`
* `tf.nn.ctc_unique_labels`

``` python
tf.nn.ctc_unique_labels(
    labels,
    name=None
)
```



Defined in [`python/ops/ctc_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/ctc_ops.py).

<!-- Placeholder for "Used in" -->

For use with <a href="../../tf/nn/ctc_loss"><code>tf.nn.ctc_loss</code></a> optional argument `unique`: This op can be
used to preprocess labels in input pipeline to for better speed/memory use
computing the ctc loss on TPU.

#### Example:

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
