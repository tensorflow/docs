description: Return a slice from 'input'.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Slice" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Slice

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Return a slice from 'input'.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Slice`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Slice(
    input, begin, size, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The output tensor is a tensor with dimensions described by 'size'
whose values are extracted from 'input' starting at the offsets in
'begin'.

*Requirements*:
  0 <= begin[i] <= begin[i] + size[i] <= Di  for i in [0, n)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`begin`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
begin[i] specifies the offset into the 'i'th dimension of
'input' to slice from.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A `Tensor`. Must have the same type as `begin`.
size[i] specifies the number of elements of the 'i'th dimension
of 'input' to slice. If size[i] is -1, all remaining elements in dimension
i are included in the slice (i.e. this is equivalent to setting
size[i] = input.dim_size(i) - begin[i]).
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

