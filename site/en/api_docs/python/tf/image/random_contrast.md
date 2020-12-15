description: Adjust the contrast of an image or images by a random factor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.random_contrast" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.random_contrast

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L1937-L1974">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adjust the contrast of an image or images by a random factor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.random_contrast`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.random_contrast(
    image, lower, upper, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Equivalent to `adjust_contrast()` but uses a `contrast_factor` randomly
picked in the interval `[lower, upper)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`image`
</td>
<td>
An image tensor with 3 or more dimensions.
</td>
</tr><tr>
<td>
`lower`
</td>
<td>
float.  Lower bound for the random contrast factor.
</td>
</tr><tr>
<td>
`upper`
</td>
<td>
float.  Upper bound for the random contrast factor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A Python integer. Used to create a random seed. See
<a href="../../tf/compat/v1/set_random_seed.md"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
</td>
</tr>
</table>



#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.random_contrast(x, 0.2, 0.5)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=...>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The contrast-adjusted image(s).
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
if `upper <= lower` or if `lower < 0`.
</td>
</tr>
</table>

