description: Randomly crops a tensor to a given size in a deterministic manner.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.stateless_random_crop" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.stateless_random_crop

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/random_ops.py#L395-L445">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Randomly crops a tensor to a given size in a deterministic manner.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.stateless_random_crop(
    value, size, seed, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Slices a shape `size` portion out of `value` at a uniformly chosen offset.
Requires `value.shape >= size`.

If a dimension should not be cropped, pass the full size of that dimension.
For example, RGB images can be cropped with
`size = [crop_height, crop_width, 3]`.

Guarantees the same results given the same `seed` independent of how many
times the function is called, and independent of global seed settings (e.g.
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>).

#### Usage Example:



```
>>> image = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
>>> seed = (1, 2)
>>> tf.image.stateless_random_crop(value=image, size=(1, 2, 3), seed=seed)
<tf.Tensor: shape=(1, 2, 3), dtype=int32, numpy=
array([[[1, 2, 3],
        [4, 5, 6]]], dtype=int32)>
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
Input tensor to crop.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
1-D tensor with size the rank of `value`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A shape [2] Tensor, the seed to the random number generator. Must have
dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
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
A cropped tensor of the same rank as `value` and shape `size`.
</td>
</tr>

</table>

