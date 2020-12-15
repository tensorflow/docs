description: Adjust the contrast of images by a random factor deterministically.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.stateless_random_contrast" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.stateless_random_contrast

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L1977-L2021">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adjust the contrast of images by a random factor deterministically.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.stateless_random_contrast(
    image, lower, upper, seed
)
</code></pre>



<!-- Placeholder for "Used in" -->

Guarantees the same results given the same `seed` independent of how many
times the function is called, and independent of global seed settings (e.g.
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>).

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
A shape [2] Tensor, the seed to the random number generator. Must have
dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
</td>
</tr>
</table>



#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...      [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> seed = (1, 2)
>>> tf.image.stateless_random_contrast(x, 0.2, 0.5, seed)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[3.4605184, 4.4605184, 5.4605184],
        [4.820173 , 5.820173 , 6.820173 ]],
       [[6.179827 , 7.179827 , 8.179828 ],
        [7.5394816, 8.539482 , 9.539482 ]]], dtype=float32)>
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

