description: Randomly flip an image vertically (upside down) deterministically.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.stateless_random_flip_up_down" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.stateless_random_flip_up_down

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L445-L473">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Randomly flip an image vertically (upside down) deterministically.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.stateless_random_flip_up_down(
    image, seed
)
</code></pre>



<!-- Placeholder for "Used in" -->

Guarantees the same results given the same `seed` independent of how many
times the function is called, and independent of global seed settings (e.g.
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>).

#### Example usage:



```
>>> image = np.array([[[1], [2]], [[3], [4]]])
>>> seed = (2, 3)
>>> tf.image.stateless_random_flip_up_down(image, seed).numpy().tolist()
[[[3], [4]], [[1], [2]]]
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
4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
of shape `[height, width, channels]`.
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
A tensor of the same type and shape as `image`.
</td>
</tr>

</table>

