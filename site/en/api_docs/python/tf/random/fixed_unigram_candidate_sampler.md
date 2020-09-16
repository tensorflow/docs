description: Samples a set of classes using the provided (fixed) base distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.fixed_unigram_candidate_sampler" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.fixed_unigram_candidate_sampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/candidate_sampling_ops.py#L214-L304">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Samples a set of classes using the provided (fixed) base distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.nn.fixed_unigram_candidate_sampler`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.fixed_unigram_candidate_sampler`, `tf.compat.v1.random.fixed_unigram_candidate_sampler`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.fixed_unigram_candidate_sampler(
    true_classes, num_true, num_sampled, unique, range_max, vocab_file='',
    distortion=1.0, num_reserved_ids=0, num_shards=1, shard=0, unigrams=(),
    seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation randomly samples a tensor of sampled classes
(`sampled_candidates`) from the range of integers `[0, range_max)`.

The elements of `sampled_candidates` are drawn without replacement
(if `unique=True`) or with replacement (if `unique=False`) from
the base distribution.

The base distribution is read from a file or passed in as an
in-memory array. There is also an option to skew the distribution by
applying a distortion power to the weights.

In addition, this operation returns tensors `true_expected_count`
and `sampled_expected_count` representing the number of times each
of the target classes (`true_classes`) and the sampled
classes (`sampled_candidates`) is expected to occur in an average
tensor of sampled classes.  These values correspond to `Q(y|x)`
defined in [this
document](http://www.tensorflow.org/extras/candidate_sampling.pdf).
If `unique=True`, then these are post-rejection probabilities and we
compute them approximately.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`true_classes`
</td>
<td>
A `Tensor` of type `int64` and shape `[batch_size,
num_true]`. The target classes.
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
`num_sampled`
</td>
<td>
An `int`.  The number of classes to randomly sample.
</td>
</tr><tr>
<td>
`unique`
</td>
<td>
A `bool`. Determines whether all sampled classes in a batch are
unique.
</td>
</tr><tr>
<td>
`range_max`
</td>
<td>
An `int`. The number of possible classes.
</td>
</tr><tr>
<td>
`vocab_file`
</td>
<td>
Each valid line in this file (which should have a CSV-like
format) corresponds to a valid word ID. IDs are in sequential order,
starting from num_reserved_ids. The last entry in each line is expected
to be a value corresponding to the count or relative probability. Exactly
one of `vocab_file` and `unigrams` needs to be passed to this operation.
</td>
</tr><tr>
<td>
`distortion`
</td>
<td>
The distortion is used to skew the unigram probability
distribution.  Each weight is first raised to the distortion's power
before adding to the internal unigram distribution. As a result,
`distortion = 1.0` gives regular unigram sampling (as defined by the vocab
file), and `distortion = 0.0` gives a uniform distribution.
</td>
</tr><tr>
<td>
`num_reserved_ids`
</td>
<td>
Optionally some reserved IDs can be added in the range
`[0, num_reserved_ids)` by the users. One use case is that a special
unknown word token is used as ID 0. These IDs will have a sampling
probability of 0.
</td>
</tr><tr>
<td>
`num_shards`
</td>
<td>
A sampler can be used to sample from a subset of the original
range in order to speed up the whole computation through parallelism. This
parameter (together with `shard`) indicates the number of partitions that
are being used in the overall computation.
</td>
</tr><tr>
<td>
`shard`
</td>
<td>
A sampler can be used to sample from a subset of the original range
in order to speed up the whole computation through parallelism. This
parameter (together with `num_shards`) indicates the particular partition
number of the operation, when partitioning is being used.
</td>
</tr><tr>
<td>
`unigrams`
</td>
<td>
A list of unigram counts or probabilities, one per ID in
sequential order. Exactly one of `vocab_file` and `unigrams` should be
passed to this operation.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An `int`. An operation-specific seed. Default is 0.
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

<tr>
<td>
`sampled_candidates`
</td>
<td>
A tensor of type `int64` and shape `[num_sampled]`.
The sampled classes.
</td>
</tr><tr>
<td>
`true_expected_count`
</td>
<td>
A tensor of type `float`.  Same shape as
`true_classes`. The expected counts under the sampling distribution
of each of `true_classes`.
</td>
</tr><tr>
<td>
`sampled_expected_count`
</td>
<td>
A tensor of type `float`. Same shape as
`sampled_candidates`. The expected counts under the sampling distribution
of each of `sampled_candidates`.
</td>
</tr>
</table>

