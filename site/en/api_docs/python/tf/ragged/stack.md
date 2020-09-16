description: Stacks a list of rank-R tensors into one rank-(R+1) RaggedTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.stack" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.stack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ragged/ragged_concat_ops.py#L73-L118">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Stacks a list of rank-`R` tensors into one rank-`(R+1)` `RaggedTensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.stack`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.stack(
    values, axis=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a list of tensors or ragged tensors with the same rank `R`
(`R >= axis`), returns a rank-`R+1` `RaggedTensor` `result` such that
`result[i0...iaxis]` is `[value[i0...iaxis] for value in values]`.

#### Examples:

```
>>> # Stacking two ragged tensors.
>>> t1 = tf.ragged.constant([[1, 2], [3, 4, 5]])
>>> t2 = tf.ragged.constant([[6], [7, 8, 9]])
>>> tf.ragged.stack([t1, t2], axis=0)
<tf.RaggedTensor [[[1, 2], [3, 4, 5]], [[6], [7, 8, 9]]]>
>>> tf.ragged.stack([t1, t2], axis=1)
<tf.RaggedTensor [[[1, 2], [6]], [[3, 4, 5], [7, 8, 9]]]>
```

```
>>> # Stacking two dense tensors with different sizes.
>>> t3 = tf.constant([[1, 2, 3], [4, 5, 6]])
>>> t4 = tf.constant([[5], [6], [7]])
>>> tf.ragged.stack([t3, t4], axis=0)
<tf.RaggedTensor [[[1, 2, 3], [4, 5, 6]], [[5], [6], [7]]]>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
A list of <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>.  May not be empty. All
`values` must have the same rank and the same dtype; but unlike
<a href="../../tf/stack.md"><code>tf.stack</code></a>, they can have arbitrary dimension sizes.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A python integer, indicating the dimension along which to stack.
(Note: Unlike <a href="../../tf/stack.md"><code>tf.stack</code></a>, the `axis` parameter must be statically known.)
Negative values are supported only if the rank of at least one
`values` value is statically known.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` with rank `R+1`.
`result.ragged_rank=1+max(axis, max(rt.ragged_rank for rt in values]))`.
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
If `values` is empty, if `axis` is out of bounds or if
the input tensors have different ranks.
</td>
</tr>
</table>

