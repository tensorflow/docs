description: Generates labels for candidate sampling with a learned unigram distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.AllCandidateSampler" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.AllCandidateSampler

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
<p>`tf.compat.v1.raw_ops.AllCandidateSampler`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AllCandidateSampler(
    true_classes, num_true, num_sampled, unique, seed=0, seed2=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See explanations of candidate sampling and the data formats at
go/candidate-sampling.

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
An `int` that is `>= 1`. Number of candidates to produce.
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

