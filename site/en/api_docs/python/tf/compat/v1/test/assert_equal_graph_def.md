description: Asserts that two GraphDefs are (mostly) the same.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.test.assert_equal_graph_def" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.test.assert_equal_graph_def

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/test_util.py#L186-L208">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Asserts that two `GraphDef`s are (mostly) the same.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.test.assert_equal_graph_def(
    actual, expected, checkpoint_v2=(False), hash_table_shared_name=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Compares two `GraphDef` protos for equality, ignoring versions and ordering of
nodes, attrs, and control inputs.  Node names are used to match up nodes
between the graphs, so the naming of nodes must be consistent.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`actual`
</td>
<td>
The `GraphDef` we have.
</td>
</tr><tr>
<td>
`expected`
</td>
<td>
The `GraphDef` we expected.
</td>
</tr><tr>
<td>
`checkpoint_v2`
</td>
<td>
boolean determining whether to ignore randomized attribute
values that appear in V2 checkpoints.
</td>
</tr><tr>
<td>
`hash_table_shared_name`
</td>
<td>
boolean determining whether to ignore randomized
shared_names that appear in HashTableV2 op defs.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`AssertionError`
</td>
<td>
If the `GraphDef`s do not match.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If either argument is not a `GraphDef`.
</td>
</tr>
</table>

