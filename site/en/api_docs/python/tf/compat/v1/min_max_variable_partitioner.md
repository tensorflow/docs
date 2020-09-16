description: Partitioner to allocate minimum size per slice.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.min_max_variable_partitioner" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.min_max_variable_partitioner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/partitioned_variables.py#L157-L218">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Partitioner to allocate minimum size per slice.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.min_max_variable_partitioner(
    max_partitions=1, axis=0, min_slice_size=(256 << 10),
    bytes_per_string_element=16
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a partitioner that partitions the variable of given shape and dtype
such that each partition has a minimum of `min_slice_size` slice of the
variable. The maximum number of such partitions (upper bound) is given by
`max_partitions`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`max_partitions`
</td>
<td>
Upper bound on the number of partitions. Defaults to 1.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Axis along which to partition the variable. Defaults to 0.
</td>
</tr><tr>
<td>
`min_slice_size`
</td>
<td>
Minimum size of the variable slice per partition. Defaults
to 256K.
</td>
</tr><tr>
<td>
`bytes_per_string_element`
</td>
<td>
If the `Variable` is of type string, this provides
an estimate of how large each scalar in the `Variable` is.
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

