description: Randomly changes jpeg encoding quality for inducing jpeg noise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.random_jpeg_quality" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.random_jpeg_quality

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L2533-L2578">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Randomly changes jpeg encoding quality for inducing jpeg noise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.random_jpeg_quality`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.random_jpeg_quality(
    image, min_jpeg_quality, max_jpeg_quality, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`min_jpeg_quality` must be in the interval `[0, 100]` and less than
`max_jpeg_quality`.
`max_jpeg_quality` must be in the interval `[0, 100]`.

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.random_jpeg_quality(x, 75, 95)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=...>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`image`
</td>
<td>
3D image. Size of the last dimension must be 1 or 3.
</td>
</tr><tr>
<td>
`min_jpeg_quality`
</td>
<td>
Minimum jpeg encoding quality to use.
</td>
</tr><tr>
<td>
`max_jpeg_quality`
</td>
<td>
Maximum jpeg encoding quality to use.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An operation-specific seed. It will be used in conjunction with the
graph-level seed to determine the real seeds that will be used in this
operation. Please see the documentation of set_random_seed for its
interaction with the graph-level random seed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Adjusted image(s), same shape and DType as `image`.
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
if `min_jpeg_quality` or `max_jpeg_quality` is invalid.
</td>
</tr>
</table>

