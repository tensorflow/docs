description: Adjust the saturation of RGB images by a random factor deterministically.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.stateless_random_saturation" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.stateless_random_saturation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L2735-L2782">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adjust the saturation of RGB images by a random factor deterministically.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.stateless_random_saturation(
    image, lower, upper, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Equivalent to `adjust_saturation()` but uses a `saturation_factor` randomly
picked in the interval `[lower, upper)`.

Guarantees the same results given the same `seed` independent of how many
times the function is called, and independent of global seed settings (e.g.
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>).

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...      [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> seed = (1, 2)
>>> tf.image.stateless_random_saturation(x, 0.5, 1.0, seed)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 1.1559395,  2.0779698,  3.       ],
        [ 4.1559396,  5.07797  ,  6.       ]],
       [[ 7.1559396,  8.07797  ,  9.       ],
        [10.155939 , 11.07797  , 12.       ]]], dtype=float32)>
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
RGB image or images. The size of the last dimension must be 3.
</td>
</tr><tr>
<td>
`lower`
</td>
<td>
float.  Lower bound for the random saturation factor.
</td>
</tr><tr>
<td>
`upper`
</td>
<td>
float.  Upper bound for the random saturation factor.
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
if `upper <= lower` or if `lower < 0`.
</td>
</tr>
</table>

