description: Computes the ids of the positions in sampled_candidates that match true_labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ComputeAccidentalHits" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ComputeAccidentalHits

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the ids of the positions in sampled_candidates that match true_labels.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ComputeAccidentalHits`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ComputeAccidentalHits(
    true_classes, sampled_candidates, num_true, seed=0, seed2=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

When doing log-odds NCE, the result of this op should be passed through a
SparseToDense op, then added to the logits of the sampled candidates. This has
the effect of 'removing' the sampled labels that match the true labels by
making the classifier sure that they are sampled labels.

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
The true_classes output of UnpackSparseLabels.
</td>
</tr><tr>
<td>
`sampled_candidates`
</td>
<td>
A `Tensor` of type `int64`.
The sampled_candidates output of CandidateSampler.
</td>
</tr><tr>
<td>
`num_true`
</td>
<td>
An `int`. Number of true labels per context.
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
A tuple of `Tensor` objects (indices, ids, weights).
</td>
</tr>
<tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`ids`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

