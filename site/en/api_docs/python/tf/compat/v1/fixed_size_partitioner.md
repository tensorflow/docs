description: Partitioner to specify a fixed number of shards along given axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.fixed_size_partitioner" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.fixed_size_partitioner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/partitioned_variables.py#L221-L237">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Partitioner to specify a fixed number of shards along given axis.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.fixed_size_partitioner(
    num_shards, axis=0
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_shards`
</td>
<td>
`int`, number of shards to partition variable.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
`int`, axis to partition on.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A partition function usable as the `partitioner` argument to
`variable_scope` and `get_variable`.
</td>
</tr>

</table>

