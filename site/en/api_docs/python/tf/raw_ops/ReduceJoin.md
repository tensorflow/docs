description: Joins a string Tensor across the given dimensions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ReduceJoin" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ReduceJoin

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Joins a string Tensor across the given dimensions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ReduceJoin`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ReduceJoin(
    inputs, reduction_indices, keep_dims=(False), separator='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the string join across dimensions in the given string Tensor of shape
`[\\(d_0, d_1, ..., d_{n-1}\\)]`.  Returns a new Tensor created by joining the input
strings with the given separator (default: empty string).  Negative indices are
counted backwards from the end, with `-1` being equivalent to `n - 1`.  If
indices are not specified, joins across all dimensions beginning from `n - 1`
through `0`.

#### For example:



```python
# tensor `a` is [["a", "b"], ["c", "d"]]
tf.reduce_join(a, 0) ==> ["ac", "bd"]
tf.reduce_join(a, 1) ==> ["ab", "cd"]
tf.reduce_join(a, -2) = tf.reduce_join(a, 0) ==> ["ac", "bd"]
tf.reduce_join(a, -1) = tf.reduce_join(a, 1) ==> ["ab", "cd"]
tf.reduce_join(a, 0, keep_dims=True) ==> [["ac", "bd"]]
tf.reduce_join(a, 1, keep_dims=True) ==> [["ab"], ["cd"]]
tf.reduce_join(a, 0, separator=".") ==> ["a.c", "b.d"]
tf.reduce_join(a, [0, 1]) ==> "acbd"
tf.reduce_join(a, [1, 0]) ==> "abcd"
tf.reduce_join(a, []) ==> [["a", "b"], ["c", "d"]]
tf.reduce_join(a) = tf.reduce_join(a, [1, 0]) ==> "abcd"
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A `Tensor` of type `string`.
The input to be joined.  All reduced indices must have non-zero size.
</td>
</tr><tr>
<td>
`reduction_indices`
</td>
<td>
A `Tensor` of type `int32`.
The dimensions to reduce over.  Dimensions are reduced in the
order specified.  Omitting `reduction_indices` is equivalent to passing
`[n-1, n-2, ..., 0]`.  Negative indices from `-n` to `-1` are supported.
</td>
</tr><tr>
<td>
`keep_dims`
</td>
<td>
An optional `bool`. Defaults to `False`.
If `True`, retain reduced dimensions with length `1`.
</td>
</tr><tr>
<td>
`separator`
</td>
<td>
An optional `string`. Defaults to `""`.
The separator to use when joining.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

