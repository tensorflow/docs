description: Computes CTC (Connectionist Temporal Classification) loss.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.ctc_loss_v2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.ctc_loss_v2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/ctc_ops.py#L738-L830">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes CTC (Connectionist Temporal Classification) loss.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.ctc_loss_v2(
    labels, logits, label_length, logit_length, logits_time_major=(True),
    unique=None, blank_index=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op implements the CTC loss as presented in (Graves et al., 2006).

#### Notes:



- Same as the "Classic CTC" in TensorFlow 1.x's tf.compat.v1.nn.ctc_loss
  setting of preprocess_collapse_repeated=False, ctc_merge_repeated=True
- Labels may be supplied as either a dense, zero-padded tensor with a
  vector of label sequence lengths OR as a SparseTensor.
- On TPU and GPU: Only dense padded labels are supported.
- On CPU: Caller may use SparseTensor or dense padded labels but calling with
  a SparseTensor will be significantly faster.
- Default blank label is 0 rather num_classes - 1, unless overridden by
  blank_index.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
tensor of shape [batch_size, max_label_seq_length] or SparseTensor
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
tensor of shape [frames, batch_size, num_labels], if
logits_time_major == False, shape is [batch_size, frames, num_labels].
</td>
</tr><tr>
<td>
`label_length`
</td>
<td>
tensor of shape [batch_size], None if labels is SparseTensor
Length of reference label sequence in labels.
</td>
</tr><tr>
<td>
`logit_length`
</td>
<td>
tensor of shape [batch_size] Length of input sequence in
logits.
</td>
</tr><tr>
<td>
`logits_time_major`
</td>
<td>
(optional) If True (default), logits is shaped [time,
batch, logits]. If False, shape is [batch, time, logits]
</td>
</tr><tr>
<td>
`unique`
</td>
<td>
(optional) Unique label indices as computed by
ctc_unique_labels(labels).  If supplied, enable a faster, memory efficient
implementation on TPU.
</td>
</tr><tr>
<td>
`blank_index`
</td>
<td>
(optional) Set the class index to use for the blank label.
Negative values will start from num_classes, ie, -1 will reproduce the
ctc_loss behavior of using num_classes - 1 for the blank symbol. There is
some memory/performance overhead to switching from the default of 0 as an
additional shifted copy of the logits may be created.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this `Op`. Defaults to "ctc_loss_dense".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`loss`
</td>
<td>
tensor of shape [batch_size], negative log probabilities.
</td>
</tr>
</table>



#### References:

Connectionist Temporal Classification - Labeling Unsegmented Sequence Data
with Recurrent Neural Networks:
  [Graves et al., 2006](https://dl.acm.org/citation.cfm?id=1143891)
  ([pdf](http://www.cs.toronto.edu/~graves/icml_2006.pdf))
