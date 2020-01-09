page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.nn.rank_sampled_softmax_loss

``` python
tf.contrib.nn.rank_sampled_softmax_loss(
    weights,
    biases,
    labels,
    inputs,
    num_sampled,
    num_resampled,
    num_classes,
    num_true,
    sampled_values,
    resampling_temperature,
    remove_accidental_hits,
    partition_strategy,
    name=None
)
```



Defined in [`tensorflow/contrib/nn/python/ops/sampling_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/nn/python/ops/sampling_ops.py).

Computes softmax loss using rank-based adaptive resampling.

This has been shown to improve rank loss after training compared to
<a href="../../../tf/nn/sampled_softmax_loss"><code>tf.nn.sampled_softmax_loss</code></a>. For a description of the algorithm and some
experimental results, please see: [TAPAS: Two-pass Approximate Adaptive
Sampling for Softmax](https://arxiv.org/abs/1707.03073).

Sampling follows two phases:
* In the first phase, `num_sampled` classes are selected using
  <a href="../../../tf/nn/learned_unigram_candidate_sampler"><code>tf.nn.learned_unigram_candidate_sampler</code></a> or supplied `sampled_values`.
  The logits are calculated on those sampled classes. This phases is
  similar to <a href="../../../tf/nn/sampled_softmax_loss"><code>tf.nn.sampled_softmax_loss</code></a>.
* In the second phase, the `num_resampled` classes with highest predicted
  probability are kept. Probabilities are
  `LogSumExp(logits / resampling_temperature)`, where the sum is over
  `inputs`.

The `resampling_temperature` parameter controls the "adaptiveness" of the
resampling. At lower temperatures, resampling is more adaptive because it
picks more candidates close to the predicted classes. A common strategy is
to decrease the temperature as training proceeds.

See <a href="../../../tf/nn/sampled_softmax_loss"><code>tf.nn.sampled_softmax_loss</code></a> for more documentation on sampling and
for typical default values for some of the parameters.

This operation is for training only. It is generally an underestimate of
the full softmax loss.

A common use case is to use this method for training, and calculate the full
softmax loss for evaluation or inference. In this case, you must set
`partition_strategy="div"` for the two losses to be consistent, as in the
following example:

```python
if mode == "train":
  loss = rank_sampled_softmax_loss(
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
  loss = tf.nn.softmax_cross_entropy_with_logits(
      labels=labels_one_hot,
      logits=logits)
```

#### Args:

* <b>`weights`</b>: A `Tensor` or `PartitionedVariable` of shape `[num_classes, dim]`,
      or a list of `Tensor` objects whose concatenation along dimension 0
      has shape [num_classes, dim]. The (possibly-sharded) class embeddings.
* <b>`biases`</b>: A `Tensor` or `PartitionedVariable` of shape `[num_classes]`.
      The (possibly-sharded) class biases.
* <b>`labels`</b>: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes. Note that this format differs from
      the `labels` argument of `nn.softmax_cross_entropy_with_logits`.
* <b>`inputs`</b>: A `Tensor` of shape `[batch_size, dim]`. The forward
      activations of the input network.
* <b>`num_sampled`</b>: An `int`. The number of classes to randomly sample per batch.
* <b>`num_resampled`</b>: An `int`. The number of classes to select from the
      `num_sampled` classes using the adaptive resampling algorithm. Must be
      less than `num_sampled`.
* <b>`num_classes`</b>: An `int`. The number of possible classes.
* <b>`num_true`</b>: An `int`.  The number of target classes per training example.
* <b>`sampled_values`</b>: A tuple of (`sampled_candidates`, `true_expected_count`,
      `sampled_expected_count`) returned by a `*_candidate_sampler` function.
      If None, default to `nn.learned_unigram_candidate_sampler`.
* <b>`resampling_temperature`</b>: A scalar `Tensor` with the temperature parameter
      for the adaptive resampling algorithm.
* <b>`remove_accidental_hits`</b>: A `bool`. Whether to remove "accidental hits"
      where a sampled class equals one of the target classes.
* <b>`partition_strategy`</b>: A string specifying the partitioning strategy, relevant
      if `len(weights) > 1`. Currently `"div"` and `"mod"` are supported.
      See <a href="../../../tf/nn/embedding_lookup"><code>tf.nn.embedding_lookup</code></a> for more details.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `batch_size` 1-D tensor of per-example sampled softmax losses.


#### Raises:

* <b>`ValueError`</b>: If `num_sampled <= num_resampled`.