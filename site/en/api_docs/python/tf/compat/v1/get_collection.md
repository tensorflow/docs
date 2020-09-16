description: Wrapper for Graph.get_collection() using the default graph.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.get_collection" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.get_collection

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/framework/ops.py#L6155-L6181">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Wrapper for `Graph.get_collection()` using the default graph.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.get_collection(
    key, scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See <a href="../../../tf/Graph.md#get_collection"><code>tf.Graph.get_collection</code></a>
for more details.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`key`
</td>
<td>
The key for the collection. For example, the `GraphKeys` class contains
many standard names for collections.
</td>
</tr><tr>
<td>
`scope`
</td>
<td>
(Optional.) If supplied, the resulting list is filtered to include
only items whose `name` attribute matches using `re.match`. Items without
a `name` attribute are never returned if a scope is supplied and the
choice or `re.match` means that a `scope` without special tokens filters
by prefix.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The list of values in the collection with the given `name`, or
an empty list if no value has been added to that collection. The
list contains the values in the order under which they were
collected.
</td>
</tr>

</table>




#### Eager Compatibility
Collections are not supported when eager execution is enabled.

