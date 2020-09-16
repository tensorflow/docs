description: Given a path to new and old vocabulary files, returns a remapping Tensor of

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.GenerateVocabRemapping" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.GenerateVocabRemapping

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Given a path to new and old vocabulary files, returns a remapping Tensor of

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.GenerateVocabRemapping`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.GenerateVocabRemapping(
    new_vocab_file, old_vocab_file, new_vocab_offset, num_new_vocab,
    old_vocab_size=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

length `num_new_vocab`, where `remapping[i]` contains the row number in the old
vocabulary that corresponds to row `i` in the new vocabulary (starting at line
`new_vocab_offset` and up to `num_new_vocab` entities), or `-1` if entry `i`
in the new vocabulary is not in the old vocabulary.  The old vocabulary is
constrained to the first `old_vocab_size` entries if `old_vocab_size` is not the
default value of -1.

`num_vocab_offset` enables
use in the partitioned variable case, and should generally be set through
examining partitioning info.  The format of the files should be a text file,
with each line containing a single entity within the vocabulary.

For example, with `new_vocab_file` a text file containing each of the following
elements on a single line: `[f0, f1, f2, f3]`, old_vocab_file = [f1, f0, f3],
`num_new_vocab = 3, new_vocab_offset = 1`, the returned remapping would be
`[0, -1, 2]`.

The op also returns a count of how many entries in the new vocabulary
were present in the old vocabulary, which is used to calculate the number of
values to initialize in a weight matrix remapping

This functionality can be used to remap both row vocabularies (typically,
features) and column vocabularies (typically, classes) from TensorFlow
checkpoints.  Note that the partitioning logic relies on contiguous vocabularies
corresponding to div-partitioned variables.  Moreover, the underlying remapping
uses an IndexTable (as opposed to an inexact CuckooTable), so client code should
use the corresponding index_table_from_file() as the FeatureColumn framework
does (as opposed to tf.feature_to_id(), which uses a CuckooTable).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`new_vocab_file`
</td>
<td>
A `Tensor` of type `string`. Path to the new vocab file.
</td>
</tr><tr>
<td>
`old_vocab_file`
</td>
<td>
A `Tensor` of type `string`. Path to the old vocab file.
</td>
</tr><tr>
<td>
`new_vocab_offset`
</td>
<td>
An `int` that is `>= 0`.
How many entries into the new vocab file to start reading.
</td>
</tr><tr>
<td>
`num_new_vocab`
</td>
<td>
An `int` that is `>= 0`.
Number of entries in the new vocab file to remap.
</td>
</tr><tr>
<td>
`old_vocab_size`
</td>
<td>
An optional `int` that is `>= -1`. Defaults to `-1`.
Number of entries in the old vocab file to consider.  If -1,
use the entire old vocabulary.
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
A tuple of `Tensor` objects (remapping, num_present).
</td>
</tr>
<tr>
<td>
`remapping`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`num_present`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr>
</table>

