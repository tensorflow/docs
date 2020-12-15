description: Returns a given flattened sequence packed into a given structure.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nest.pack_sequence_as" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nest.pack_sequence_as

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/util/nest.py#L545-L579">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a given flattened sequence packed into a given structure.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nest.pack_sequence_as`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nest.pack_sequence_as(
    structure, flat_sequence, expand_composites=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `structure` is a scalar, `flat_sequence` must be a single-element list;
in this case the return value is `flat_sequence[0]`.

If `structure` is or contains a dict instance, the keys will be sorted to
pack the flat sequence in deterministic order. This is true also for
`OrderedDict` instances: their sequence order is ignored, the sorting order of
keys is used instead. The same convention is followed in `flatten`.
This correctly repacks dicts and `OrderedDict`s after they have been
flattened, and also allows flattening an `OrderedDict` and then repacking it
back using a corresponding plain dict, or vice-versa.
Dictionaries with non-sortable keys cannot be flattened.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`structure`
</td>
<td>
Nested structure, whose structure is given by nested lists,
tuples, and dicts. Note: numpy arrays and strings are considered
scalars.
</td>
</tr><tr>
<td>
`flat_sequence`
</td>
<td>
flat sequence to pack.
</td>
</tr><tr>
<td>
`expand_composites`
</td>
<td>
If true, then composite tensors such as
<a href="../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> and <a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> are expanded into their
component tensors.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`packed`
</td>
<td>
`flat_sequence` converted to have the same recursive structure as
`structure`.
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
If `flat_sequence` and `structure` have different
element counts.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
`structure` is or contains a dict with non-sortable keys.
</td>
</tr>
</table>

