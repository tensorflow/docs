description: Computes and returns the noise-contrastive estimation training loss.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.nce_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.nce_loss

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_impl.py#L2084-L2193">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes and returns the noise-contrastive estimation training loss.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.nce_loss(
    weights, biases, labels, inputs, num_sampled, num_classes, num_true=1,
    sampled_values=None, remove_accidental_hits=(False), partition_strategy='mod',
    name='nce_loss'
)
</code></pre>



<!-- Placeholder for "Used in" -->

A common use case is to use this method for training, and calculate the full
sigmoid loss for evaluation or inference. In this case, you must set
`partition_strategy="div"` for the two losses to be consistent, as in the
following example:

```python
if mode == "train":
  loss = tf.nn.nce_loss(
      weights=weights,
      biases=biases,
      labels=labels,
      inputs=inputs,
      ...,
      partition_strategy="div")
elif mode == "eval":
  logits = tf.matmul(inputs, tf.transpose(weights))
  logits = tf.nn.bias_add(logits, biases)
  labels_one_hot = tf.one_hot(labels, n_classes)
  loss = tf.nn.sigmoid_cross_entropy_with_logits(
      labels=labels_one_hot,
      logits=logits)
  loss = tf.reduce_sum(loss, axis=1)
```

Note: By default this uses a log-uniform (Zipfian) distribution for sampling,
so your labels must be sorted in order of decreasing frequency to achieve
good results.  For more details, see
<a href="../../../../tf/random/log_uniform_candidate_sampler.md"><code>tf.random.log_uniform_candidate_sampler</code></a>.

Note: In the case where `num_true` > 1, we assign to each target class
the target probability 1 / `num_true` so that the target probabilities
sum to 1 per-example.

Note: It would be useful to allow a variable number of target classes per
example.  We hope to provide this functionality in a future release.
For now, if you have a variable number of target classes, you can pad them
out to a constant number by either repeating them or by padding
with an otherwise unused class.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`weights`
</td>
<td>
A `Tensor` of shape `[num_classes, dim]`, or a list of `Tensor`
objects whose concatenation along dimension 0 has shape
[num_classes, dim].  The (possibly-partitioned) class embeddings.
</td>
</tr><tr>
<td>
`biases`
</td>
<td>
A `Tensor` of shape `[num_classes]`.  The class biases.
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
A `Tensor` of type `int64` and shape `[batch_size,
num_true]`. The target classes.
</td>
</tr><tr>
<td>
`inputs`
</td>
<td>
A `Tensor` of shape `[batch_size, dim]`.  The forward
activations of the input network.
</td>
</tr><tr>
<td>
`num_sampled`
</td>
<td>
An `int`.  The number of negative classes to randomly sample
per batch. This single sample of negative classes is evaluated for each
element in the batch.
</td>
</tr><tr>
<td>
`num_classes`
</td>
<td>
An `int`. The number of possible classes.
</td>
</tr><tr>
<td>
`num_true`
</td>
<td>
An `int`.  The number of target classes per training example.
</td>
</tr><tr>
<td>
`sampled_values`
</td>
<td>
a tuple of (`sampled_candidates`, `true_expected_count`,
`sampled_expected_count`) returned by a `*_candidate_sampler` function.
(if None, we default to `log_uniform_candidate_sampler`)
</td>
</tr><tr>
<td>
`remove_accidental_hits`
</td>
<td>
A `bool`.  Whether to remove "accidental hits"
where a sampled class equals one of the target classes.  If set to
`True`, this is a "Sampled Logistic" loss instead of NCE, and we are
learning to generate log-odds instead of log probabilities. See
our Candidate Sampling Algorithms Reference
([pdf](https://www.tensorflow.org/extras/candidate_sampling.pdf)).
Default is False.
</td>
</tr><tr>
<td>
`partition_strategy`
</td>
<td>
A string specifying the partitioning strategy, relevant
if `len(weights) > 1`. Currently `"div"` and `"mod"` are supported.
Default is `"mod"`. See `tf.nn.embedding_lookup` for more details.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `batch_size` 1-D tensor of per-example NCE losses.
</td>
</tr>

</table>



#### References:

Noise-contrastive estimation - A new estimation principle for unnormalized
statistical models:
  [Gutmann et al., 2010](http://proceedings.mlr.press/v9/gutmann10a)
  ([pdf](http://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf))
