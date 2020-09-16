description: Generate the set of all classes.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.all_candidate_sampler" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.all_candidate_sampler

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/candidate_sampling_ops.py#L312-L345">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generate the set of all classes.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.nn.all_candidate_sampler`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.all_candidate_sampler`, `tf.compat.v1.random.all_candidate_sampler`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.all_candidate_sampler(
    true_classes, num_true, num_sampled, unique, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Deterministically generates and returns the set of all possible classes.
For testing purposes.  There is no need to use this, since you might as
well use full softmax or full logistic regression.

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
An `int`.  The number of possible classes.
</td>
</tr><tr>
<td>
`unique`
</td>
<td>
A `bool`. Ignored.
unique.
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
This operation deterministically returns the entire range
`[0, num_sampled]`.
</td>
</tr><tr>
<td>
`true_expected_count`
</td>
<td>
A tensor of type `float`.  Same shape as
`true_classes`. The expected counts under the sampling distribution
of each of `true_classes`. All returned values are 1.0.
</td>
</tr><tr>
<td>
`sampled_expected_count`
</td>
<td>
A tensor of type `float`. Same shape as
`sampled_candidates`. The expected counts under the sampling distribution
of each of `sampled_candidates`. All returned values are 1.0.
</td>
</tr>
</table>

