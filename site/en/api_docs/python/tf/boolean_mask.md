description: Apply boolean mask to tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.boolean_mask" />
<meta itemprop="path" content="Stable" />
</div>

# tf.boolean_mask

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/array_ops.py#L1696-L1746">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Apply boolean mask to tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.boolean_mask(
    tensor, mask, axis=None, name='boolean_mask'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Numpy equivalent is `tensor[mask]`.

```python
# 1-D example
tensor = [0, 1, 2, 3]
mask = np.array([True, False, True, False])
boolean_mask(tensor, mask)  # [0, 2]
```

In general, `0 < dim(mask) = K <= dim(tensor)`, and `mask`'s shape must match
the first K dimensions of `tensor`'s shape.  We then have:
  `boolean_mask(tensor, mask)[i, j1,...,jd] = tensor[i1,...,iK,j1,...,jd]`
where `(i1,...,iK)` is the ith `True` entry of `mask` (row-major order).
The `axis` could be used with `mask` to indicate the axis to mask from.
In that case, `axis + dim(mask) <= dim(tensor)` and `mask`'s shape must match
the first `axis + dim(mask)` dimensions of `tensor`'s shape.

See also: <a href="../tf/ragged/boolean_mask.md"><code>tf.ragged.boolean_mask</code></a>, which can be applied to both dense and
ragged tensors, and can be used if you need to preserve the masked dimensions
of `tensor` (rather than flattening them, as <a href="../tf/boolean_mask.md"><code>tf.boolean_mask</code></a> does).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
N-D tensor.
</td>
</tr><tr>
<td>
`mask`
</td>
<td>
K-D boolean tensor, K <= N and K must be known statically.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A 0-D int Tensor representing the axis in `tensor` to mask from. By
default, axis is 0 which will mask from the first dimension. Otherwise K +
axis <= N.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
(N-K+1)-dimensional tensor populated by entries in `tensor` corresponding
to `True` values in `mask`.
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
If shapes do not conform.
</td>
</tr>
</table>



#### Examples:



```python
# 2-D example
tensor = [[1, 2], [3, 4], [5, 6]]
mask = np.array([True, False, True])
boolean_mask(tensor, mask)  # [[1, 2], [5, 6]]
```