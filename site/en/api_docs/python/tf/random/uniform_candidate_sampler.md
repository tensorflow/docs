description: Samples a set of classes using a uniform base distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.uniform_candidate_sampler" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.uniform_candidate_sampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/candidate_sampling_ops.py#L31-L88">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Samples a set of classes using a uniform base distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.uniform_candidate_sampler`, `tf.compat.v1.random.uniform_candidate_sampler`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.uniform_candidate_sampler(
    true_classes, num_true, num_sampled, unique, range_max, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation randomly samples a tensor of sampled classes
(`sampled_candidates`) from the range of integers `[0, range_max)`.

The elements of `sampled_candidates` are drawn without replacement
(if `unique=True`) or with replacement (if `unique=False`) from
the base distribution.

The base distribution for this operation is the uniform distribution
over the range of integers `[0, range_max)`.

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
An `int`.  The number of classes to randomly sample. The
`sampled_candidates` return value will have shape `[num_sampled]`. If
`unique=True`, `num_sampled` must be less than or equal to `range_max`.
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
A tensor of type `int64` and shape `[num_sampled]`.  The
sampled classes, either with possible duplicates (`unique=False`) or all
unique (`unique=True`). In either case, `sampled_candidates` is
independent of the true classes.
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

