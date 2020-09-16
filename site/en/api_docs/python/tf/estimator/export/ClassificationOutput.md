description: Represents the output of a classification head.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.export.ClassificationOutput" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="as_signature_def"/>
</div>

# tf.estimator.export.ClassificationOutput

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/saved_model/model_utils/export_output.py#L102-L167">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents the output of a classification head.

Inherits From: [`ExportOutput`](../../../tf/estimator/export/ExportOutput.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.export.ClassificationOutput`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.export.ClassificationOutput(
    scores=None, classes=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Either classes or scores or both must be set.

The classes `Tensor` must provide string labels, not integer class IDs.

If only classes is set, it is interpreted as providing top-k results in
descending order.

If only scores is set, it is interpreted as providing a score for every class
in order of class ID.

If both classes and scores are set, they are interpreted as zipped, so each
score corresponds to the class at the same index.  Clients should not depend
on the order of the entries.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`scores`
</td>
<td>
A float `Tensor` giving scores (sometimes but not always
interpretable as probabilities) for each class.  May be `None`, but
only if `classes` is set.  Interpretation varies-- see class doc.
</td>
</tr><tr>
<td>
`classes`
</td>
<td>
A string `Tensor` giving predicted class labels.  May be `None`,
but only if `scores` is set.  Interpretation varies-- see class doc.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if neither classes nor scores is set, or one of them is not a
`Tensor` with the correct dtype.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`classes`
</td>
<td>

</td>
</tr><tr>
<td>
`scores`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="as_signature_def"><code>as_signature_def</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/saved_model/model_utils/export_output.py#L158-L167">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_signature_def(
    receiver_tensors
)
</code></pre>

Generate a SignatureDef proto for inclusion in a MetaGraphDef.

The SignatureDef will specify outputs as described in this ExportOutput,
and will use the provided receiver_tensors as inputs.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`receiver_tensors`
</td>
<td>
a `Tensor`, or a dict of string to `Tensor`, specifying
input nodes that will be fed.
</td>
</tr>
</table>





