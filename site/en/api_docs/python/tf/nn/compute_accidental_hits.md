description: Compute the position ids in sampled_candidates matching true_classes.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.compute_accidental_hits" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.compute_accidental_hits

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/candidate_sampling_ops.py#L343-L389">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compute the position ids in `sampled_candidates` matching `true_classes`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.compute_accidental_hits`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.compute_accidental_hits(
    true_classes, sampled_candidates, num_true, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

In Candidate Sampling, this operation facilitates virtually removing
sampled classes which happen to match target classes.  This is done
in Sampled Softmax and Sampled Logistic.

See our [Candidate Sampling Algorithms
Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf).

We presuppose that the `sampled_candidates` are unique.

We call it an 'accidental hit' when one of the target classes
matches one of the sampled classes.  This operation reports
accidental hits as triples `(index, id, weight)`, where `index`
represents the row number in `true_classes`, `id` represents the
position in `sampled_candidates`, and weight is `-FLOAT_MAX`.

The result of this op should be passed through a `sparse_to_dense`
operation, then added to the logits of the sampled classes. This
removes the contradictory effect of accidentally sampling the true
target classes as noise classes for the same example.

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
`sampled_candidates`
</td>
<td>
A tensor of type `int64` and shape `[num_sampled]`.
The sampled_candidates output of CandidateSampler.
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
`indices`
</td>
<td>
A `Tensor` of type `int32` and shape `[num_accidental_hits]`.
Values indicate rows in `true_classes`.
</td>
</tr><tr>
<td>
`ids`
</td>
<td>
A `Tensor` of type `int64` and shape `[num_accidental_hits]`.
Values indicate positions in `sampled_candidates`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
A `Tensor` of type `float` and shape `[num_accidental_hits]`.
Each value is `-FLOAT_MAX`.
</td>
</tr>
</table>

