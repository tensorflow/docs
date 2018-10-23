

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.sampled_softmax_loss

``` python
sampled_softmax_loss(
    weights,
    biases,
    labels,
    inputs,
    num_sampled,
    num_classes,
    num_true=1,
    sampled_values=None,
    remove_accidental_hits=True,
    partition_strategy='mod',
    name='sampled_softmax_loss'
)
```



Defined in [`tensorflow/python/ops/nn_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/nn_impl.py).

See the guide: [Neural Network > Candidate Sampling](../../../../api_guides/python/nn#Candidate_Sampling)

Computes and returns the sampled softmax training loss.

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
  loss = tf.nn.sampled_softmax_loss(
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

See our [Candidate Sampling Algorithms Reference](https://www.tensorflow.org/extras/candidate_sampling.pdf)

Also see Section 3 of [Jean et al., 2014](http://arxiv.org/abs/1412.2007)
([pdf](http://arxiv.org/pdf/1412.2007.pdf)) for the math.

#### Args:

* <b>`weights`</b>: A `Tensor` of shape `[num_classes, dim]`, or a list of `Tensor`
      objects whose concatenation along dimension 0 has shape
      [num_classes, dim].  The (possibly-sharded) class embeddings.
* <b>`biases`</b>: A `Tensor` of shape `[num_classes]`.  The class biases.
* <b>`labels`</b>: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes.  Note that this format differs from
      the `labels` argument of `nn.softmax_cross_entropy_with_logits`.
* <b>`inputs`</b>: A `Tensor` of shape `[batch_size, dim]`.  The forward
      activations of the input network.
* <b>`num_sampled`</b>: An `int`.  The number of classes to randomly sample per batch.
* <b>`num_classes`</b>: An `int`. The number of possible classes.
* <b>`num_true`</b>: An `int`.  The number of target classes per training example.
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