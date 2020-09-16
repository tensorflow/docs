description: Randomly shuffles a tensor along its first dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RandomShuffle" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RandomShuffle

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Randomly shuffles a tensor along its first dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RandomShuffle`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RandomShuffle(
    value, seed=0, seed2=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

  The tensor is shuffled along dimension 0, such that each `value[j]` is mapped
  to one and only one `output[i]`. For example, a mapping that might occur for a
  3x2 tensor is:

```
[[1, 2],       [[5, 6],
 [3, 4],  ==>   [1, 2],
 [5, 6]]        [3, 4]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A `Tensor`. The tensor to be shuffled.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An optional `int`. Defaults to `0`.
If either `seed` or `seed2` are set to be non-zero, the random number
generator is seeded by the given seed.  Otherwise, it is seeded by a
random seed.
</td>
</tr><tr>
<td>
`seed2`
</td>
<td>
An optional `int`. Defaults to `0`.
A second seed to avoid seed collision.
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
A `Tensor`. Has the same type as `value`.
</td>
</tr>

</table>

