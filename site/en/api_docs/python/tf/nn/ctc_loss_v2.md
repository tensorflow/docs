page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.ctc_loss_v2

Computes CTC (Connectionist Temporal Classification) loss.

### Aliases:

* `tf.compat.v1.nn.ctc_loss_v2`
* `tf.compat.v2.nn.ctc_loss`
* `tf.nn.ctc_loss_v2`

``` python
tf.nn.ctc_loss_v2(
    labels,
    logits,
    label_length,
    logit_length,
    logits_time_major=True,
    unique=None,
    blank_index=None,
    name=None
)
```



Defined in [`python/ops/ctc_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/ctc_ops.py).

<!-- Placeholder for "Used in" -->

This op implements the CTC loss as presented in the article:

[A. Graves, S. Fernandez, F. Gomez, J. Schmidhuber.
Connectionist Temporal Classification: Labeling Unsegmented Sequence Data
with Recurrent Neural Networks. ICML 2006, Pittsburgh, USA,
pp. 369-376.](http://www.cs.toronto.edu/~graves/icml_2006.pdf)

#### Notes:

- Same as the "Classic CTC" in TensorFlow 1.x's tf.compat.v1.nn.ctc_loss
setting of
  preprocess_collapse_repeated=False, ctc_merge_repeated=True
- Labels may be supplied as either a dense, zero-padded tensor with a
  vector of label sequence lengths OR as a SparseTensor.
- On TPU and GPU:
    - Only dense padded labels are supported.
- On CPU:
    - Caller may use SparseTensor or dense padded labels but calling with
      a SparseTensor will be significantly faster.
- Default blank label is 0 rather num_classes - 1, unless overridden by
  blank_index.



#### Args:


* <b>`labels`</b>: tensor of shape [batch_size, max_label_seq_length] or SparseTensor
* <b>`logits`</b>: tensor of shape [frames, batch_size, num_labels], if
  logits_time_major == False, shape is [batch_size, frames, num_labels].
* <b>`label_length`</b>: tensor of shape [batch_size], None if labels is SparseTensor
  Length of reference label sequence in labels.
* <b>`logit_length`</b>: tensor of shape [batch_size] Length of input sequence in
  logits.
* <b>`logits_time_major`</b>: (optional) If True (default), logits is shaped [time,
  batch, logits]. If False, shape is [batch, time, logits]
* <b>`unique`</b>: (optional) Unique label indices as computed by
  ctc_unique_labels(labels).  If supplied, enable a faster, memory efficient
  implementation on TPU.
* <b>`blank_index`</b>: (optional) Set the class index to use for the blank label.
  Negative values will start from num_classes, ie, -1 will reproduce the
  ctc_loss behavior of using num_classes - 1 for the blank symbol. There is
  some memory/performance overhead to switching from the default of 0 as an
  additional shifted copy of the logits may be created.
* <b>`name`</b>: A name for this `Op`. Defaults to "ctc_loss_dense".


#### Returns:


* <b>`loss`</b>: tensor of shape [batch_size], negative log probabilities.