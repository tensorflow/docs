page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.nn.sampled_sparse_softmax_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/nn/python/ops/sampling_ops.py#L247-L342">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes and returns the sampled sparse softmax training loss.

``` python
tf.contrib.nn.sampled_sparse_softmax_loss(
    weights,
    biases,
    labels,
    inputs,
    num_sampled,
    num_classes,
    sampled_values=None,
    remove_accidental_hits=True,
    partition_strategy='mod',
    name='sampled_sparse_softmax_loss'
)
```



<!-- Placeholder for "Used in" -->

This is a faster way to train a softmax classifier over a huge number of
classes.

This operation is for training only.  It is generally an underestimate of
the full softmax loss.

A common use case is to use this method for training, and calculate the full
softmax loss for evaluation or inference. In this case, you must set
`partition_strategy="div"` for the two losses to be consistent, as in the
following example:

```python
if mode == "train":
  loss = tf.nn.sampled_sparse_softmax_loss(
      weights=weights,
      biases=biases,
      labels=labels,
      inputs=inputs,
      ...,
      partition_strategy="div")
elif mode == "eval":
  logits = tf.matmul(inputs, tf.transpose(weights))
  logits = tf.nn.bias_add(logits, biases)
  loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
      labels=tf.squeeze(labels),
      logits=logits)
```

See our [Candidate Sampling Algorithms Reference]
(https://www.tensorflow.org/extras/candidate_sampling.pdf)

Also see Section 3 of [Jean et al., 2014](http://arxiv.org/abs/1412.2007)
([pdf](http://arxiv.org/pdf/1412.2007.pdf)) for the math.

#### Args:


* <b>`weights`</b>: A `Tensor` of shape `[num_classes, dim]`, or a list of `Tensor`
    objects whose concatenation along dimension 0 has shape
    [num_classes, dim].  The (possibly-sharded) class embeddings.
* <b>`biases`</b>: A `Tensor` of shape `[num_classes]`.  The class biases.
* <b>`labels`</b>: A `Tensor` of type `int64` and shape `[batch_size, 1]`.
    The index of the single target class for each row of logits.  Note that
    this format differs from the `labels` argument of
    <a href="/api_docs/python/tf/nn/sparse_softmax_cross_entropy_with_logits"><code>nn.sparse_softmax_cross_entropy_with_logits</code></a>.
* <b>`inputs`</b>: A `Tensor` of shape `[batch_size, dim]`.  The forward
    activations of the input network.
* <b>`num_sampled`</b>: An `int`.  The number of classes to randomly sample per batch.
* <b>`num_classes`</b>: An `int`. The number of possible classes.
* <b>`sampled_values`</b>: a tuple of (`sampled_candidates`, `true_expected_count`,
    `sampled_expected_count`) returned by a `*_candidate_sampler` function.
    (if None, we default to `log_uniform_candidate_sampler`)
* <b>`remove_accidental_hits`</b>:  A `bool`.  whether to remove "accidental hits"
    where a sampled class equals one of the target classes.  Default is
    True.
* <b>`partition_strategy`</b>: A string specifying the partitioning strategy, relevant
    if `len(weights) > 1`. Currently `"div"` and `"mod"` are supported.
    Default is `"mod"`. See `tf.nn.embedding_lookup` for more details.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `batch_size` 1-D tensor of per-example sampled softmax losses.
