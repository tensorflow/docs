description: Randomly crops a tensor to a given size.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.random_crop" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.random_crop

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/random_ops.py#L353-L392">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Randomly crops a tensor to a given size.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.random_crop`, `tf.compat.v1.random_crop`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.random_crop(
    value, size, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Slices a shape `size` portion out of `value` at a uniformly chosen offset.
Requires `value.shape >= size`.

If a dimension should not be cropped, pass the full size of that dimension.
For example, RGB images can be cropped with
`size = [crop_height, crop_width, 3]`.

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
Python integer. Used to create a random seed. See
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>
for behavior.
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

