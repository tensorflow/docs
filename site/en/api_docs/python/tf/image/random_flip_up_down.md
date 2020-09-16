description: Randomly flips an image vertically (upside down).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.random_flip_up_down" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.random_flip_up_down

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L323-L360">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Randomly flips an image vertically (upside down).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.random_flip_up_down`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.random_flip_up_down(
    image, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

With a 1 in 2 chance, outputs the contents of `image` flipped along the first
dimension, which is `height`.  Otherwise, output the image as-is.
When passing a batch of images, each image will be randomly flipped
independent of other images.

#### Example usage:



```
>>> import numpy as np
```

```
>>> image = np.array([[[1], [2]], [[3], [4]]])
>>> tf.image.random_flip_up_down(image, 3).numpy().tolist()
[[[3], [4]], [[1], [2]]]
```

Randomly flip multiple images.
>>> images = np.array(
... [
...     [[[1], [2]], [[3], [4]]],
...     [[[5], [6]], [[7], [8]]]
... ])
>>> tf.image.random_flip_up_down(images, 4).numpy().tolist()
[[[[3], [4]], [[1], [2]]], [[[5], [6]], [[7], [8]]]]

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
A Python integer. Used to create a random seed. See
<a href="../../tf/compat/v1/set_random_seed.md"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
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



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the shape of `image` not supported.
</td>
</tr>
</table>

