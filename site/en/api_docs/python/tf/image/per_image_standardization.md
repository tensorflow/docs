description: Linearly scales each image in image to have mean 0 and variance 1.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.per_image_standardization" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.per_image_standardization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/image_ops_impl.py#L1708-L1751">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Linearly scales each image in `image` to have mean 0 and variance 1.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.per_image_standardization`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.per_image_standardization(
    image
)
</code></pre>



<!-- Placeholder for "Used in" -->

For each 3-D image `x` in `image`, computes `(x - mean) / adjusted_stddev`,
where

- `mean` is the average of all values in `x`
- `adjusted_stddev = max(stddev, 1.0/sqrt(N))` is capped away from 0 to
  protect against division by 0 when handling uniform images
  - `N` is the number of elements in `x`
  - `stddev` is the standard deviation of all values in `x`

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`image`
</td>
<td>
An n-D Tensor with at least 3 dimensions, the last 3 of which are the
dimensions of each image.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with the same shape and dtype as `image`.
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
if the shape of 'image' is incompatible with this function.
</td>
</tr>
</table>

