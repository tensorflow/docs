description: Adjust the hue of RGB images by a random factor deterministically.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.stateless_random_hue" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.stateless_random_hue

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L2414-L2462">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adjust the hue of RGB images by a random factor deterministically.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.stateless_random_hue(
    image, max_delta, seed
)
</code></pre>



<!-- Placeholder for "Used in" -->

Equivalent to `adjust_hue()` but uses a `delta` randomly picked in the
interval `[-max_delta, max_delta)`.

Guarantees the same results given the same `seed` independent of how many
times the function is called, and independent of global seed settings (e.g.
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>).

`max_delta` must be in the interval `[0, 0.5]`.

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...      [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> seed = (1, 2)
>>> tf.image.stateless_random_hue(x, 0.2, seed)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 1.6514902,  1.       ,  3.       ],
        [ 4.65149  ,  4.       ,  6.       ]],
       [[ 7.65149  ,  7.       ,  9.       ],
        [10.65149  , 10.       , 12.       ]]], dtype=float32)>
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
`max_delta`
</td>
<td>
float. The maximum value for the random delta.
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
if `max_delta` is invalid.
</td>
</tr>
</table>

