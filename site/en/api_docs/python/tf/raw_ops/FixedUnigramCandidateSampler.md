description: Generates labels for candidate sampling with a learned unigram distribution.

robots: noindex

# tf.raw_ops.FixedUnigramCandidateSampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generates labels for candidate sampling with a learned unigram distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.FixedUnigramCandidateSampler`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.FixedUnigramCandidateSampler(
    true_classes, num_true, num_sampled, unique, range_max, vocab_file='',
    distortion=1, num_reserved_ids=0, num_shards=1, shard=0, unigrams=[], seed=0,
    seed2=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A unigram sampler could use a fixed unigram distribution read from a
file or passed in as an in-memory array instead of building up the distribution
from data on the fly. There is also an option to skew the distribution by
applying a distortion power to the weights.

The vocabulary file should be in CSV-like format, with the last field
being the weight associated with the word.

For each batch, this op picks a single set of sampled candidate labels.

The advantages of sampling candidates per-batch are simplicity and the
possibility of efficient dense matrix multiplication. The disadvantage is that
the sampled candidates must be chosen independently of the context and of the
true labels.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`true_classes`
</td>
<td>
A `Tensor` of type `int64`.
A batch_size * num_true matrix, in which each row contains the
IDs of the num_true target_classes in the corresponding original label.
</td>
</tr><tr>
<td>
`num_true`
</td>
<td>
An `int` that is `>= 1`. Number of true labels per context.
</td>
</tr><tr>
<td>
`num_sampled`
</td>
<td>
An `int` that is `>= 1`.
Number of candidates to randomly sample.
</td>
</tr><tr>
<td>
`unique`
</td>
<td>
A `bool`.
If unique is true, we sample with rejection, so that all sampled
candidates in a batch are unique. This requires some approximation to
estimate the post-rejection sampling probabilities.
</td>
</tr><tr>
<td>
`range_max`
</td>
<td>
An `int` that is `>= 1`.
The sampler will sample integers from the interval [0, range_max).
</td>
</tr><tr>
<td>
`vocab_file`
</td>
<td>
An optional `string`. Defaults to `""`.
Each valid line in this file (which should have a CSV-like format)
corresponds to a valid word ID. IDs are in sequential order, starting from
num_reserved_ids. The last entry in each line is expected to be a value
corresponding to the count or relative probability. Exactly one of vocab_file
and unigrams needs to be passed to this op.
</td>
</tr><tr>
<td>
`distortion`
</td>
<td>
An optional `float`. Defaults to `1`.
The distortion is used to skew the unigram probability distribution.
Each weight is first raised to the distortion's power before adding to the
internal unigram distribution. As a result, distortion = 1.0 gives regular
unigram sampling (as defined by the vocab file), and distortion = 0.0 gives
a uniform distribution.
</td>
</tr><tr>
<td>
`num_reserved_ids`
</td>
<td>
An optional `int`. Defaults to `0`.
Optionally some reserved IDs can be added in the range [0,
..., num_reserved_ids) by the users. One use case is that a special unknown
word token is used as ID 0. These IDs will have a sampling probability of 0.
</td>
</tr><tr>
<td>
`num_shards`
</td>
<td>
An optional `int` that is `>= 1`. Defaults to `1`.
A sampler can be used to sample from a subset of the original range
in order to speed up the whole computation through parallelism. This parameter
(together with 'shard') indicates the number of partitions that are being
used in the overall computation.
</td>
</tr><tr>
<td>
`shard`
</td>
<td>
An optional `int` that is `>= 0`. Defaults to `0`.
A sampler can be used to sample from a subset of the original range
in order to speed up the whole computation through parallelism. This parameter
(together with 'num_shards') indicates the particular partition number of a
sampler op, when partitioning is being used.
</td>
</tr><tr>
<td>
`unigrams`
</td>
<td>
An optional list of `floats`. Defaults to `[]`.
A list of unigram counts or probabilities, one per ID in sequential
order. Exactly one of vocab_file and unigrams should be passed to this op.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An optional `int`. Defaults to `0`.
If either seed or seed2 are set to be non-zero, the random number
generator is seeded by the given seed.  Otherwise, it is seeded by a
random seed.
</td>
</tr><tr>
<td>
`seed2`
</td>
<td>
An optional `int`. Defaults to `0`.
An second seed to avoid seed collision.
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
A tuple of `Tensor` objects (sampled_candidates, true_expected_count, sampled_expected_count).
</td>
</tr>
<tr>
<td>
`sampled_candidates`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`true_expected_count`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`sampled_expected_count`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

