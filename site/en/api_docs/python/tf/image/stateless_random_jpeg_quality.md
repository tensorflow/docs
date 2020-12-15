description: Deterministically radomize jpeg encoding quality for inducing jpeg noise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.stateless_random_jpeg_quality" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.stateless_random_jpeg_quality

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L2581-L2635">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Deterministically radomize jpeg encoding quality for inducing jpeg noise.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.stateless_random_jpeg_quality(
    image, min_jpeg_quality, max_jpeg_quality, seed
)
</code></pre>



<!-- Placeholder for "Used in" -->

Guarantees the same results given the same `seed` independent of how many
times the function is called, and independent of global seed settings (e.g.
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>).

`min_jpeg_quality` must be in the interval `[0, 100]` and less than
`max_jpeg_quality`.
`max_jpeg_quality` must be in the interval `[0, 100]`.

#### Usage Example:



```
>>> x = [[[1, 2, 3],
...       [4, 5, 6]],
...      [[7, 8, 9],
...       [10, 11, 12]]]
>>> x_uint8 = tf.cast(x, tf.uint8)
>>> seed = (1, 2)
>>> tf.image.stateless_random_jpeg_quality(x_uint8, 75, 95, seed)
<tf.Tensor: shape=(2, 2, 3), dtype=uint8, numpy=
array([[[ 0,  4,  5],
        [ 1,  5,  6]],
       [[ 5,  9, 10],
        [ 5,  9, 10]]], dtype=uint8)>
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
A shape [2] Tensor, the seed to the random number generator. Must have
dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
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

