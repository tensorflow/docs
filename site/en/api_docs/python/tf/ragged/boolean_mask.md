description: Applies a boolean mask to data without flattening the mask dimensions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.boolean_mask" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.boolean_mask

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ragged/ragged_array_ops.py#L41-L201">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies a boolean mask to `data` without flattening the mask dimensions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.boolean_mask`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.boolean_mask(
    data, mask, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a potentially ragged tensor that is formed by retaining the elements
in `data` where the corresponding value in `mask` is `True`.

* `output[a1...aA, i, b1...bB] = data[a1...aA, j, b1...bB]`

   Where `j` is the `i`th `True` entry of `mask[a1...aA]`.

Note that `output` preserves the mask dimensions `a1...aA`; this differs
from <a href="../../tf/boolean_mask.md"><code>tf.boolean_mask</code></a>, which flattens those dimensions.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A potentially ragged tensor.
</td>
</tr><tr>
<td>
`mask`
</td>
<td>
A potentially ragged boolean tensor.  `mask`'s shape must be a prefix
of `data`'s shape.  `rank(mask)` must be known statically.
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
A potentially ragged tensor that is formed by retaining the elements in
`data` where the corresponding value in `mask` is `True`.

* `rank(output) = rank(data)`.
* `output.ragged_rank = max(data.ragged_rank, rank(mask) - 1)`.
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
if `rank(mask)` is not known statically; or if `mask.shape` is
not a prefix of `data.shape`.
</td>
</tr>
</table>


#### Examples:

```
>>> # Aliases for True & False so data and mask line up.
>>> T, F = (True, False)
```

```
>>> tf.ragged.boolean_mask(  # Mask a 2D Tensor.
...     data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
...     mask=[[T, F, T], [F, F, F], [T, F, F]]).to_list()
[[1, 3], [], [7]]
```

```
>>> tf.ragged.boolean_mask(  # Mask a 2D RaggedTensor.
...     tf.ragged.constant([[1, 2, 3], [4], [5, 6]]),
...     tf.ragged.constant([[F, F, T], [F], [T, T]])).to_list()
[[3], [], [5, 6]]
```

```
>>> tf.ragged.boolean_mask(  # Mask rows of a 2D RaggedTensor.
...     tf.ragged.constant([[1, 2, 3], [4], [5, 6]]),
...     tf.ragged.constant([True, False, True])).to_list()
[[1, 2, 3], [5, 6]]
```