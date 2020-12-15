description: Rotate image(s) counter-clockwise by 90 degrees.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.rot90" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.rot90

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/image_ops_impl.py#L561-L608">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Rotate image(s) counter-clockwise by 90 degrees.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.rot90`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.rot90(
    image, k=1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### For example:



```
>>> a=tf.constant([[[1],[2]],
...                [[3],[4]]])
>>> # rotating `a` counter clockwise by 90 degrees
>>> a_rot=tf.image.rot90(a)
>>> print(a_rot[...,0].numpy())
[[2 4]
 [1 3]]
>>> # rotating `a` counter clockwise by 270 degrees
>>> a_rot=tf.image.rot90(a, k=3)
>>> print(a_rot[...,0].numpy())
[[3 1]
 [4 2]]
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
`k`
</td>
<td>
A scalar integer. The number of times the image is rotated by 90 degrees.
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
A rotated tensor of the same type and shape as `image`.
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

